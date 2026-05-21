# ⚡ Quick Start (5 Minutes)

## 🎯 Your First Summary in 5 Minutes

### Step 1: Get Groq API Key (2 minutes)
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (free account)
3. Go to **API Keys** → **Create API Key**
4. Copy the key

### Step 2: Setup Project (2 minutes)

**Windows PowerShell:**
```powershell
# Create environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Add your API key
# Edit .env file and paste your key
notepad .env
```

**macOS/Linux:**
```bash
# Create environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Add your API key
# Edit .env file and paste your key
nano .env
```

### Step 3: Run App (1 minute)
```bash
streamlit run app.py
```

**Done! 🎉**

Your browser will open at `http://localhost:8501`

---

## 🚀 Try It Now

### Example 1: Summarize Text
1. Click "📝 Text Summarizer" tab
2. Paste this text:
```
Artificial intelligence is transforming industries worldwide. 
Machine learning models can now process images, text, and audio. 
Companies are investing billions in AI development. 
The technology brings both opportunities and challenges for society.
```
3. Select "Short" summary and "Professional" tone
4. Click "Generate Summary"
5. See the magic happen! ✨

### Example 2: Summarize a URL
1. Click "🌐 URL Summarizer" tab
2. Paste: `https://en.wikipedia.org/wiki/Artificial_intelligence`
3. Click "Generate Summary"
4. Download the result!

### Example 3: Upload a File
1. Click "📄 File Summarizer" tab
2. Upload any PDF or TXT file
3. Click "Generate Summary"
4. Copy or download!

---

## 📋 .env File Template

```
GROQ_API_KEY=gsk_your_actual_key_here
```

That's it! The rest of the configuration is automatic.

---

## ✅ Verification

If you see this in the sidebar:
```
✅ Groq API - Connected
```

**Everything works!** 🚀

---

## 🆘 Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| "Module not found" | Run: `pip install -r requirements.txt` |
| "API Key error" | Add key to `.env` file |
| "App won't load" | Try: `streamlit run app.py --logger.level=debug` |
| App crashes | Check internet connection |

---

## 📚 Next Steps

1. Try all 3 tabs (Text, File, URL)
2. Experiment with different summary types
3. Test different tones
4. Download and save summaries
5. Deploy to Streamlit Cloud (see README.md)

---

## 🎓 Learn More

- Full guide: [README.md](README.md)
- Setup help: [SETUP.md](SETUP.md)
- User guide: [USER_GUIDE.md](USER_GUIDE.md)

---

**Questions? Check the documentation or GitHub issues!**

Happy Summarizing! 🚀
