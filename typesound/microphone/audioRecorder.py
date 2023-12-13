import os
import subprocess
import signal

class AudioRecorder:
    def __init__(self):
        self.process = None
        self.recording = False
            
    def grab_audio(self,
                  output_file="audio.wav",
                  duration=0, rate=48000,
                  audioFormat="S16_LE"):
        command = ['arecord',
                   '-d', str(duration),
                   '-r', str(rate),
                   '-c', str(2),
                   '-f', audioFormat, output_file]
        print(command)
        # Start the command using Popen
        self.process = subprocess.Popen(command)
        self.recording = True

    def stop_recording(self):
        if self.process is not None:
            print(self.process)
            if self.process.poll() is None:
                # os.killpg(self.process.pid, signal.SIGTERM)
                self.process.terminate()  # Terminate the subprocess
                self.process = None
                self.recording = False
                print("Stopped the recording")
            else:
                self.process = None
