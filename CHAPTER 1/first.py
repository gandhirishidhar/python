print("Hello Rishi")
import pyjokes
from gtts import gTTS
import os

print("--- AI JOKE TELLER ---")

# 1. Get the joke
joke = pyjokes.get_joke()
print(f"The Joke: {joke}")

# 2. Convert text to audio (This might take 1-2 seconds)
print("Generating audio...")
my_audio = gTTS(text=joke, lang='en', slow=False)

# 3. Save it as a file
my_audio.save("joke_audio.mp3")

# 4. Play the file
print("Playing audio...")
os.system("start joke_audio.mp3")

"""'''
why i going to add comment
comment are somethig which should be made 
so here is comment and the last commnent
the last comment
"""