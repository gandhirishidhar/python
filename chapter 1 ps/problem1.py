print(''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')

import os

print("--- OFFLINE ROBOT SPEAKER ---")

# 1. Define what you want to say
text_to_speak = "Hello Rishi. I am running offline without any extra installation."

# 2. The Engineering Trick: 
# We build a command string that tells Windows PowerShell to speak.
command = f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text_to_speak}\');"'

# 3. Execute the command
os.system(command)

import comtypes.client

print("--- INITIALIZING ROBOT ---")

try:
    # 1. Access the Windows "Voice" Object directly
    speaker = comtypes.client.CreateObject("SAPI.SpVoice")
    
    # 2. Define text
    text = "Hello Rishi. This is the com-types module speaking."
    print(f"Speaking: {text}")

    # 3. Speak
    speaker.Speak(text)

except Exception as e:
    print("Error found:", e)
    from gtts import gTTS
import os

# 1. The Setup
text = "Hello Rishi. System checks passed. Moving to next chapter."

# 2. The Conversion (Online)
print("Talking...")
audio = gTTS(text=text, lang='en', slow=False)

# 3. The Playback
audio.save("voice.mp3")
os.system("start voice.mp3")
