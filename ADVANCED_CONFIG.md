# ⚙️ Advanced Configuration Guide

For users who want to customize and extend the application.

---

## 🎛️ Configuration File (`config.py`)

### API Configuration

**Change Groq Model:**
```python
# In config.py or .env
GROQ_MODEL = "llama3-8b-8192"  # Options: mixtral-8x7b-32768, llama3-8b-8192, gemma-7b-it
```

**Adjust API Parameters:**
```python
MAX_TOKENS = 2048  # Increase for longer summaries
TEMPERATURE = 0.5  # Lower = more consistent, Higher = more creative (0.0-1.0)
REQUEST_TIMEOUT = 60  # Increase for slow connections
```

---

## 🎨 UI Customization

### Change Colors

In `app.py`, modify the CSS section:
```python
# Change primary color
COLOR_PRIMARY = "#FF6B6B"  # Red instead of blue

# Then update CSS
st.markdown(f"""
<style>
.header-title {{ color: {COLOR_PRIMARY}; }}
</style>
""", unsafe_allow_html=True)
```

### Modify Layout

**Change sidebar position:**
```python
st.set_page_config(
    initial_sidebar_state="collapsed"  # or "expanded"
)
```

**Adjust column ratios:**
```python
# Instead of:
col1, col2 = st.columns([2, 1])

# Use:
col1, col2 = st.columns([3, 1])  # Different ratio
```

---

## 📝 Add New Summary Type

### Step 1: Update Config
```python
# In config.py
SUMMARY_TYPES = {
    "short": "...",
    "detailed": "...",
    "bullet": "...",
    "executive": "One paragraph executive summary",  # NEW
}
```

### Step 2: Update Summarizer
```python
# In utils/summarizer.py
summary_instructions = {
    "short": "...",
    "detailed": "...",
    "bullet": "...",
    "executive": "Generate a single paragraph executive summary suitable for executives and decision-makers.",  # NEW
}
```

### Step 3: Update UI
```python
# In app.py, update selectbox
summary_type_1 = st.selectbox(
    "Summary Type",
    ["short", "detailed", "bullet", "executive"],  # Add "executive"
    format_func=get_summary_type_description,
    key="text_summary_type"
)
```

---

## 🎭 Add New Tone

### Step 1: Update Config
```python
# In config.py
TONES = {
    "professional": "...",
    "simple": "...",
    "academic": "...",
    "casual": "...",
    "humorous": "Funny and entertaining tone",  # NEW
}
```

### Step 2: Update Summarizer
```python
# In utils/summarizer.py
tone_instructions = {
    "professional": "...",
    "simple": "...",
    "academic": "...",
    "casual": "...",
    "humorous": "Use humor and wit to make the content entertaining.",  # NEW
}
```

### Step 3: Update UI
```python
# In app.py, update selectbox
tone_1 = st.selectbox(
    "Tone",
    ["professional", "simple", "academic", "casual", "humorous"],  # Add "humorous"
    format_func=get_tone_description,
    key="text_tone"
)
```

---

## 📁 Add New Input Type

Example: Add "Email Summarizer" tab

### Step 1: Create Email Parser
```python
# In utils/email_parser.py
def parse_email(email_text):
    """Parse email and extract body"""
    lines = email_text.split('\n')
    # Extract just the body content
    body_start = 0
    for i, line in enumerate(lines):
        if line.strip() == "":
            body_start = i + 1
            break
    return '\n'.join(lines[body_start:])
```

### Step 2: Add Tab in App
```python
# In app.py
tab1, tab2, tab3, tab4 = st.tabs([
    "📝 Text Summarizer",
    "📄 File Summarizer",
    "🌐 URL Summarizer",
    "📧 Email Summarizer"  # NEW
])

with tab4:
    st.markdown("### 📧 Summarize Email")
    email_input = st.text_area("Paste email content", height=250)
    # ... add generate button, etc.
```

---

## 🌐 Add Support for New Languages

### Multilingual Support

```python
# In config.py
SUPPORTED_LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "zh": "Chinese",
}

# In app.py sidebar
language = st.selectbox("Language", list(SUPPORTED_LANGUAGES.values()))

# In utils/summarizer.py
prompt = f"""
Please respond in {language}.

You are an expert content summarizer...
"""
```

---

## 💾 Add Database Support

Store summaries for later access:

```python
# requirements.txt
sqlite3  # Already built-in
# or for more features:
# sqlalchemy==2.0.0

# Create utils/database.py
import sqlite3
from datetime import datetime

class SummaryDatabase:
    def __init__(self, db_path="summaries.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS summaries (
                id INTEGER PRIMARY KEY,
                input_text TEXT,
                output_summary TEXT,
                summary_type TEXT,
                tone TEXT,
                created_at TIMESTAMP,
                word_count INTEGER
            )
        """)
        self.conn.commit()
    
    def save_summary(self, input_text, output_text, summary_type, tone, word_count):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO summaries
            (input_text, output_summary, summary_type, tone, created_at, word_count)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (input_text, output_text, summary_type, tone, datetime.now(), word_count))
        self.conn.commit()
    
    def get_all_summaries(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM summaries ORDER BY created_at DESC")
        return cursor.fetchall()
```

---

## 🔐 Add User Authentication

For deployed apps:

```python
# requirements.txt
streamlit-authenticator==0.2.1

# In app.py
import streamlit_authenticator as stauth

# Setup authentication
authenticator = stauth.Authenticate(
    credentials={
        "usernames": {
            "user1": {"name": "User One", "password": "password1"},
            "user2": {"name": "User Two", "password": "password2"},
        }
    },
    cookie_name="auth_cookie",
    key="secret_key_123",
    cookie_expiry_days=1,
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    # Show app
    st.write(f"Welcome, {name}!")
elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter username and password")
```

---

## 📊 Add Analytics

Track usage statistics:

```python
# In utils/analytics.py
import json
from datetime import datetime

class Analytics:
    def __init__(self, log_file="analytics.json"):
        self.log_file = log_file
    
    def log_summary(self, summary_type, tone, input_words, output_words):
        event = {
            "timestamp": datetime.now().isoformat(),
            "type": summary_type,
            "tone": tone,
            "input_words": input_words,
            "output_words": output_words,
        }
        
        try:
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(event) + '\n')
        except:
            pass  # Silently fail if logging doesn't work
    
    def get_stats(self):
        stats = {
            "total_summaries": 0,
            "total_words_processed": 0,
            "avg_compression": 0,
        }
        
        try:
            with open(self.log_file, 'r') as f:
                events = [json.loads(line) for line in f]
                stats["total_summaries"] = len(events)
                stats["total_words_processed"] = sum(e["input_words"] for e in events)
        except:
            pass
        
        return stats
```

---

## ⚡ Performance Optimization

### Caching Results
```python
# In app.py
import streamlit as st

@st.cache_data
def get_summary(text, summary_type, tone):
    """Cache summaries to avoid reprocessing"""
    summarizer = ContentSummarizer()
    return summarizer.generate_summary(text, summary_type, tone)
```

### Lazy Loading
```python
# Load heavy imports only when needed
def get_pdf_reader():
    from utils.pdf_reader import extract_text_from_pdf
    return extract_text_from_pdf
```

### Rate Limiting
```python
# In config.py
RATE_LIMIT_ENABLED = True
RATE_LIMIT_REQUESTS_PER_MINUTE = 10

# In utils/rate_limiter.py
import time
from collections import deque

class RateLimiter:
    def __init__(self, max_requests, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
    
    def is_allowed(self):
        now = time.time()
        
        # Remove old requests
        while self.requests and self.requests[0] < now - self.time_window:
            self.requests.popleft()
        
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False
```

---

## 🔌 Add API Export

Allow users to use your app as an API:

```python
# In app_api.py (new file)
from fastapi import FastAPI
from utils.summarizer import ContentSummarizer

app = FastAPI()

@app.post("/summarize/")
async def summarize(
    text: str,
    summary_type: str = "short",
    tone: str = "professional"
):
    summarizer = ContentSummarizer()
    summary = summarizer.generate_summary(text, summary_type, tone)
    return {"summary": summary}

# Run with: uvicorn app_api:app --reload
```

---

## 🎯 Custom Themes

Create alternative color schemes:

```python
# In config.py
THEMES = {
    "light": {
        "primary": "#1f77b4",
        "secondary": "#ff7f0e",
        "success": "#2ca02c",
    },
    "dark": {
        "primary": "#00d4ff",
        "secondary": "#ff6b9d",
        "success": "#00ff88",
    },
}

# Use in app
theme = st.selectbox("Theme", list(THEMES.keys()))
colors = THEMES[theme]
```

---

## 🧪 Add Testing

```python
# In tests/test_summarizer.py
import pytest
from utils.summarizer import ContentSummarizer

def test_generate_summary():
    summarizer = ContentSummarizer()
    text = "This is a test. It should summarize correctly."
    result = summarizer.generate_summary(text)
    assert result is not None
    assert len(result) > 0

# Run with: pytest tests/
```

---

## 📱 Mobile App Version

Using Kivy or React Native:

```python
# React Native version would use similar API
# Python with Kivy:

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from utils.summarizer import ContentSummarizer

class SummarizerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # Add UI components
        return layout

if __name__ == '__main__':
    SummarizerApp().run()
```

---

## 🚀 Deployment Customization

### Environment-Specific Settings
```python
# config.py
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

if ENVIRONMENT == "production":
    DEBUG = False
    MAX_FILE_SIZE = 50 * 1024 * 1024
    REQUEST_TIMEOUT = 30
else:
    DEBUG = True
    MAX_FILE_SIZE = 500 * 1024 * 1024
    REQUEST_TIMEOUT = 60
```

### Docker Support
```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV GROQ_API_KEY=${GROQ_API_KEY}

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
```

---

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Groq API Reference](https://console.groq.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [SQLAlchemy Guide](https://docs.sqlalchemy.org)
- [Kivy Documentation](https://kivy.org)

---

## ✅ Best Practices for Customization

1. **Backup Original**: Keep original files
2. **Test Changes**: Test before deploying
3. **Document Changes**: Update README with customizations
4. **Use Version Control**: Commit changes to Git
5. **Follow Patterns**: Maintain code style
6. **Add Comments**: Document your modifications
7. **Test Performance**: Ensure changes don't slow app
8. **Security First**: Never hardcode secrets

---

## 🎓 Next Steps

1. Start with small customizations
2. Learn from existing code
3. Gradually add features
4. Share improvements with community
5. Contribute back if helpful!

---

**Happy customizing!** 🚀
