import time
import tkinter as tk
import os
import datetime
from typesound.microphone import AudioRecorder
from typesound.keys import KeyRecorder

YPAD = 3

class Window:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Type Sound")
        self.recording = False
        self.keys = True
        self.audioRecord = AudioRecorder()
        self.keyboardRecord = KeyRecorder()
        self.audio = True
        self.setupInterface()

    def setupInterface(self) -> None:
        self.recordFrame = tk.Frame(self.root, bd=2, relief = "sunken")
        self.setupFiles()
        self.setupCheckBoxes()
        self.makeRecordButton()
        self.recordFrame.grid(column=0, row=0)

    def setupCheckBoxes(self) -> None:
        self.checkFrame = tk.Frame(self.recordFrame, border=2)
        self.keyCheck = tk.Button(self.checkFrame, text="Keyboard", command=self.keyboardButton, bg='green', activebackground='green')
        self.audioCheck = tk.Button(self.checkFrame, text = "Audio", command=self.audioButton, bg='green', activebackground='green')
        self.keyCheck.grid(row=0, column=1)
        self.audioCheck.grid(row=1, column=1)
        self.checkFrame.grid(row = 0, column=1)
               
    def setupFiles(self) -> None:
        self.fileFrame = tk.Frame(self.recordFrame, bd = 2, relief= "groove")
        self.fileName = tk.StringVar()
        self.dirName = tk.StringVar()
        self.dirName.set("data")
        self.currentDir = tk.Entry(self.fileFrame, textvariable=self.dirName)
        self.resetFileName()
        self.currentFile = tk.Entry(self.fileFrame, textvariable=self.fileName)

        self.dirLabel = tk.Label(self.fileFrame, text="Directory")
        self.fileLabel = tk.Label(self.fileFrame, text="File")

        self.dirLabel.grid(row=0, column=0, pady= YPAD)
        self.currentDir.grid(row=0, column=1, pady=YPAD)
        self.fileLabel.grid(row=1, column=0, sticky='E', pady=YPAD)
        self.currentFile.grid(row=1, column=1, pady=YPAD)
        self.fileFrame.grid(row=0, padx=5, pady=YPAD)

    def audioButton(self) -> None:
        self.audio = not self.audio
        if self.audio:
            self.audioCheck.config(bg='green', activebackground='green')
        else:
            self.audioCheck.config(bg='magenta', activebackground='magenta')

    def keyboardButton(self) -> None:
        self.keys = not self.keys
        if self.keys:
            self.keyCheck.config(bg='green', activebackground='green')
        else:
            self.keyCheck.config(bg='magenta', activebackground='magenta')

    def makeRecordButton(self) -> None:
        self.buttonFrame = tk.Frame(self.root, relief='ridge')
        self.recordButton = tk.Button(self.buttonFrame,
            text='REC',
            command=self.record,
            bg='magenta', activebackground='magenta',
            width=30, height=2)
        self.recordButton.pack()
        self.buttonFrame.grid(row=1, columnspan=2)

    def record(self) -> None:
        # negate recording and run appropriate logic
        self.resetFileName()
        self.recording = not self.recording
        if self.recording:
            # get file name for recording
            # start recording
            if self.audio:
                self.audioRecord.grab_audio(output_file=self.audioFile)
            if self.keys:
                self.keyboardRecord.start_recording(output_file = self.keyFile)
                pass
            self.recordButton.config(bg='green', activebackground='green')
        else:
            if self.audio:
                # end audio
                self.audioRecord.stop_recording()
                pass
            if self.keys:
                # end keyboard
                self.keyboardRecord.stop_recording()
                pass
            # end recording
            self.recordButton.config(bg='magenta', activebackground='magenta')
        
    def runStateReport(self):
        print("-= State Report =-")
        print("keyboard: " + str(self.keys))
        print("   audio: " + str(self.audio))
        print("    file: " + str(self.fileName.get()))
        print("     dir: " + str(self.dirName.get()))
        print("  record: " + str(self.recording))
        print(" audioFi: " + str(self.audioFile))

    def resetFileName(self):
        self.fileName.set(f"recording_{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}:{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}")
        self.audioFile = f"{os.path.expanduser('~')}/.cache/typesound/{self.currentDir.get()}/{self.fileName.get()}.wav"
        self.keyFile  =  f"{os.path.expanduser('~')}/.cache/typesound/{self.currentDir.get()}/{self.fileName.get()}.key"
                                            
def runGui() -> None:
    # Start the event loop.
    root = tk.Tk()
    window = Window(root)
    root.mainloop()
