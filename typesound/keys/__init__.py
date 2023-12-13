from typesound.keys.keyRecorder import KeyRecorder
import time

def track_keys():
    keycorder = KeyRecorder()
    keycorder.start_recording()
    time.sleep(20)
    keycorder.stop_recording()
