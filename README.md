

---

```markdown
# 🎵 Terminal Spotify Player

A lightweight, keyboard-driven Python script that searches and plays music on Spotify directly from your terminal. No bulky desktop apps, no open browser tabs—just pure terminal automation.

---

## ⚠️ Important Disclaimer

> 🚨 **CRITICAL REQUIREMENT:** This project **requires a Spotify Premium subscription**. 
> Spotify's Web API locks down playback control and third-party streaming integrations exclusively for Premium accounts. If you are on the free tier, the API authentication will fail or refuse to route audio.

---

## 🚀 Features

* **Zero GUI:** Control your music entirely through your terminal prompt.
* **Smart Search:** Automatically finds and queues the closest match for your query.
* **Invisible Integration:** Communicates directly with Spotify's backend servers via API.
* **Lightweight:** Consumes virtually zero CPU or RAM compared to the official desktop client.

---

## 🛠️ How It Works

This script bypasses the traditional user interface by operating as a smart remote control:

1. **Authentication (`spotipy`):** Uses OAuth 2.0 to securely log into your Spotify account via token exchange.
2. **Search Engine:** Sends your text query to the Spotify Search API endpoint and extracts the unique track URI.
3. **Playback Router:** Instructs Spotify's cloud servers to instantly target and stream that track to your active background playback engine.

---

## ⚙️ Initial Setup

Because this script connects directly to Spotify's pipeline, you need to register a free developer "app" to get API credentials.

### 1. Get Your API Credentials
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/).
2. Log in and click **Create an App**.
3. Name your app whatever you like (e.g., `Terminal Player`).
4. **CRITICAL STEP:** In the app settings, set the **Redirect URI** to: `http://localhost:8888/callback`
5. Save, then copy your **Client ID** and **Client Secret**.

### 2. Installation
Install the official Spotify Web API wrapper for Python:
```bash
pip install spotipy

```

---

## 🖥️ Usage

1. Open the script and paste your credentials into the designated configuration variables:
```python
CLIENT_ID = "YOUR_CLIENT_ID_HERE"
CLIENT_SECRET = "YOUR_CLIENT_SECRET_HERE"
REDIRECT_URI = "http://localhost:8888/callback"

```


2. Run the script:
```bash
python main.py

```


3. **First-Time Login:** On your very first run, your web browser will briefly pop open a Spotify page asking you to authorize your terminal app. Once you click authorize, it will redirect to a blank page. **Copy the URL of that blank page and paste it back into your terminal prompt.** (You only have to do this once!).
4. **Stream Music:** Type the name of any track or artist, hit enter, and enjoy the music.

---

## 💡 Pro-Tip: True 100% App-Free Streaming

By default, Spotify's API requires an active "device" to play the music on. If you don't want the heavy official Spotify app running in the background, use **`spotifyd`**.

`spotifyd` is an open-source, headless background daemon that runs silently in your OS tray. It uses almost no resources, logs into your Spotify account, and acts as an invisible wireless speaker that this Python script can instantly control.

---

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

```

```
