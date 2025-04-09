# 🌀 Twisync – Twitter/X Auto Bot (Replies, Threads, and More)

Twisync is a Python bot designed to automate your interactions on X (formerly Twitter).  
It can auto-reply to tweets, and will soon support auto-threading and more.

---

## 🚀 Features

- ✅ Auto-reply to a specific tweet
- 🧵 Future: auto-create threads
- 📸 Screenshots before and after posting
- 🆔 Extract reply tweet ID
- 📊 Logs performance (CPU, memory, execution time)

---

## 🛠️ Setup Instructions

### 1. Start a `screen` session

Keep the script running even after closing your terminal:

```bash
screen -S twisync
```

---

### 2. Create & activate a virtual environment

```bash
python3 -m venv twisync
source twisync/bin/activate
```

---

### 3. Install required packages

```bash
pip install playwright psutil
playwright install
```

---

### 4. Add your Twitter/X session config

Place a file named `auth.json` in the same directory.  
This file contains your session login state.

Example `auth.json` structure:
```json
{
  "cookies": [
    {
      "name": "auth_token",
      "value": "FILL_YOUR_X_AUTH_TOKEN_HERE", 
      "domain": ".x.com",
      "path": "/",
      "expires": 9999999999, 
      "httpOnly": true,
      "secure": true,
      "sameSite": "None"
    }
  ],
  "origins": []
}
```

---

### 5. Run the bot

```bash
python tweet.py
```

---

## 🗂️ Files Created

- `before_typing.png` – Before typing your reply
- `before_click.png` – After typing but before posting
- `tweet_success.png` – After tweet is posted
- `tweet_error.png` – If an error occurred
- `reply_tweet_id.txt` – Contains the ID of your posted reply

---

## ❗ Tips

- Run on a VPS or server with stable internet
- If using headless mode on Linux, make sure `xvfb` is installed
- To detach screen session:
  ```bash
  Ctrl + A, then press D
  ```
- To return later:
  ```bash
  screen -r twisync
  ```

---

## 💡 Coming Soon

- [x] Auto-reply
- [ ] Auto-thread support
- [ ] Multiple account handling
- [ ] Scheduled posting

---

Crafted with ❤️ using Playwright + Python.
