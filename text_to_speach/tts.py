import requests
import os
import vlc
import time
from dotenv import load_dotenv
import tkinter as tk

"""
this is my tts application =D

- note: its quite slow when hitting the freetts.org api endpoint
        the application looks like its 'freezing' when this 
        process happens.

- to use it you need:
    -- create a .env file inside /text_to_speach
    -- create an account at https://freetts.org/
    -- under 'developers --> api keys', create ur key there 
    -- paste the key inside .env
    -- .env should be 1 line only, with: TTS_API=api key here
"""

load_dotenv()
api_key = os.getenv("TTS_API")

def play_tts(text):
    response = requests.post(
        "https://freetts.org/api/v1/tts",
        headers={f"x-api-key": api_key},
        json={
            "text": text,
            "voice": "en-US-JennyNeural",
            "style": "cheerful",
            "output_format": "mp3" })

    mp3_url = response.json()["audio_url"]
    response_2 = requests.get(mp3_url)
    mp3_tts = response_2.content

    print(mp3_url)

    player = vlc.MediaPlayer(mp3_url)
    player.play()
    time.sleep(10) 

#play_tts("bladee is the best artist")
class Tts:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text-to-Speech Application by @digse")

        self.root.configure()

        self.tts_heading = tk.Label(self.root, text="TTS by @digse", font=("Arial", 16))
        self.tts_heading.pack(padx=10, pady=10)

        self.text_input = tk.Text(self.root, height=3, font=("Arial", 16))
        self.text_input.pack(padx=10, pady=10)

        self.speak_btn = tk.Button(self.root, text="speak", font=("Arial", 16), command=self.get_text)
        self.speak_btn.pack(padx=5, pady=5)

        self.check_state = tk.IntVar()

        self.root.mainloop()

    def get_text(self):
        self.user_text = self.text_input.get("1.0", "end-1c")

        self.get_tts(self.user_text)

        print(self.user_text)
        return self.user_text

    def get_tts(self, text):
        text = text
        print(text)
        response = requests.post(
        "https://freetts.org/api/v1/tts",
        headers={f"x-api-key": api_key},
        json={
            "text": f"{text}",
            "voice": "en-US-JennyNeural",
            "style": "cheerful",
            "output_format": "mp3" })

        mp3_url = response.json()["audio_url"]
        response_2 = requests.get(mp3_url)
        mp3_tts = response_2.content

        print(mp3_url)

        player = vlc.MediaPlayer(mp3_url)
        player.play()
        time.sleep(10) 

    #def play_tts

Tts()