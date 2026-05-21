# 🚀 AI Content Summarizer - Setup Guide

## Quick Setup Instructions

### 1️⃣ Prerequisites
- Python 3.8 or higher installed
- pip package manager
- Groq API key (free account)

### 2️⃣ Installation Steps

#### Windows
```powershell
# Open PowerShell in the project directory

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### macOS/Linux
```bash
# Open Terminal in the project directory

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Get Groq API Key

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up for a free account (or login if you have one)
3. Click on **API Keys** in the left sidebar
4. Click **Create API Key**
5. Copy the generated API key

### 4️⃣ Configure Environment

1. Open the `.env` file in the project root
2. Replace `your_groq_api_key_here` with your actual API key
3. Save the file

Example `.env` file:
```
GROQ_API_KEY=gsk_abcdefghijklmnopqrstuvwxyz123456
```

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501`

---

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file configured with API key
- [ ] Streamlit runs without errors
- [ ] Web interface loads in browser
- [ ] API status shows "Connected" in sidebar

---

## 📁 Project File Structure

```
ai-content-summarizer/
├── app.py                      # Main application
├── requirements.txt            # Dependencies
├── .env                        # Your API key (keep private!)
├── .env.example                # Example template
├── README.md                   # Full documentation
├── SETUP.md                    # This file
│
└── utils/
    ├── __init__.py
    ├── summarizer.py          # Groq API wrapper
    ├── pdf_reader.py          # PDF extraction
    ├── web_scraper.py         # URL scraping
    └── helpers.py             # Utility functions
```

---

## 🎯 First Use Guide

1. **Text Tab**: Paste some text and click "Generate Summary"
2. **File Tab**: Upload a PDF or TXT file
3. **URL Tab**: Enter a website URL

Try each tab with sample content to understand the features!

---

## 🔧 Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: Make sure virtual environment is activated and run:
```bash
pip install -r requirements.txt
```

### Issue: "GROQ_API_KEY not found"
**Solution**: 
1. Check that `.env` file exists in the project root
2. Verify it contains `GROQ_API_KEY=your_key_here`
3. Restart the Streamlit app

### Issue: "Invalid API key"
**Solution**:
1. Check if your API key is correct (copy-paste again from Groq console)
2. Make sure there are no extra spaces or quotes around the key

### Issue: App doesn't open in browser
**Solution**: Manually open `http://localhost:8501` in your browser

### Issue: "Connection refused" for URLs
**Solution**: Check your internet connection and ensure the URL is valid

---

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Recommended for Beginners)
1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and select your repo
4. Add API key in **Settings → Secrets**
5. Deploy!

### Option 2: Heroku
Requires Heroku account. See README.md for details.

### Option 3: Local Machine
Just run `streamlit run app.py` anytime!

---

## 📊 Features Overview

| Feature | Input Type | Output |
|---------|-----------|--------|
| Text Summarizer | Plain text | Summary |
| PDF Summarizer | PDF files | Summary |
| File Summarizer | Text files | Summary |
| URL Summarizer | Website URL | Summary |

All outputs include:
- Customizable summary type (Short/Detailed/Bullet)
- Tone selection (Professional/Simple/Academic/Casual)
- Word count statistics
- Download as TXT
- Copy to clipboard

---

## 💡 Tips for Best Results

1. **For PDFs**: Ensure PDF is not scanned image (text-based)
2. **For URLs**: Some JavaScript-heavy sites may not extract all content
3. **For TXT Files**: Use UTF-8 encoding
4. **For Long Content**: Use "Short" or "Bullet" summary types
5. **For Best Quality**: Use "Detailed" with relevant content

---

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Documentation](https://console.groq.com/docs)
- [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide)
- [Git Basics](https://git-scm.com/book/en/v2)

---

## 🆘 Need Help?

1. Check the main README.md for detailed information
2. Review the code comments (all functions are well-documented)
3. Check Groq API status: [status.groq.com](https://status.groq.com)
4. Create an issue on GitHub if you find bugs

---

## 🎉 You're All Set!

Start summarizing with:
```bash
streamlit run app.py
```

Enjoy! 🚀

---

**Questions? Open an issue on GitHub!**
