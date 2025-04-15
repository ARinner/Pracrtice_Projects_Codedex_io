# Pracrtice_Projects_Codedex_io

# This area is to show my work (practice projects/coding checks) and growth through the codedex.io learning course.

# 📝 Blog with AI – GPT-3.5 Powered Blog Paragraph Generator

## 🚀 Project Overview
This project is a **command-line blog paragraph generator** built with Python and OpenAI's GPT-3.5 API. The goal was to create a simple CLI tool that generates blog-style paragraphs based on user input prompts.

## 📚 What I Learned
- How to **securely manage API keys** using `.env` files and environment variables
- How to **integrate and work with third-party APIs**, specifically OpenAI's chat-based completions
- How to design a **clean user input loop** to allow users to generate multiple paragraphs in a single session

## 🐞 Challenges & Fixes
- **Outdated Method Usage**  
  ❌ Issue: Initially used a deprecated method (`openai.Completion.create()`)  
  ✅ Fix: Updated to `chat.completions.create()` using OpenAI’s current library

- **Environment Variable Errors**  
  ❌ Issue: Encountered `KeyError: 'API_KEY'` due to improper loading of `.env`  
  ✅ Fix: Switched to `load_dotenv()` and `os.getenv()` for reliable parsing

- **Quota & Authentication Errors**  
  ❌ Issue: Faced rate limits and expired API keys  
  ✅ Fix: Replaced keys, checked API quota, and verified billing access

## 💡 Key Takeaways
- API integration requires attention to **version compatibility**, **rate limits**, and **error handling**
- Proper **environment management** is critical for working on real-world projects
- Debugging with clear logs and documentation helps overcome most roadblocks
- Patience and iteration are key — **build, test, debug, repeat**
