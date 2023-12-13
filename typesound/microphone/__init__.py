import time
from typesound.microphone.audioRecorder import AudioRecorder

def record(fileName: str = "audio.wav",
              duration: int = 5):
    # Record system default mic for duration to fileName
    audioRec = AudioRecorder()
    audioRec.grab_audio(fileName)
    if duration <= 0:
        duration = 1
    time.sleep(duration)
    audioRec.stop_recording()
