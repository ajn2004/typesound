from pynput import keyboard
import time

class KeyRecorder:
    def __init__(self):
        self.listener = None
        self.recording = False
        self.file = None

    def on_press(self, key: keyboard.KeyCode):
        try:
            print(f'Key pressed: {key.char}')
            if self.file:
                self.file.write(str(time.time_ns()) + ',' + str(key.char) +"\n")
        except AttributeError:
            print(f"Special key pressed: {key}")
            if self.file:
                self.file.write(str(time.time_ns()) + ',' + str(key) + "\n")
            
    def start_recording(self, output_file: str = "key-events"):
        self.file = open(output_file, 'w')
        self.recording = True
        self.listener = keyboard.Listener(on_press = self.on_press)
        self.listener.start()

    def stop_recording(self):
        if self.recording and self.listener is not None:
            self.listener.stop()
            self.listener = None
            self.recording = False
            if self.file:
                self.file.close()
            print("Stopped recording keyboard strokes.")
