# TYPESOUND
A keylogger and audio recorder paired together for the creation of clean data sets for machine learning experiments.

### Quick Start
Download and install the project with the following command
```shell
git clone https://github.com/ajn2004/typesound
cd typesound
poetry install
```
Once installed, you should be able to run the gui with 
```shell
poetry run gui
```
From there you can set the save directory and file name, choose which data stream to record, and toggle recording.

### Introduction
Typesound is a program meant to record audio and keystrokes to build a dataset of waveforms associated with various keystrokes. We use lower level API's to stream the data to accessible files with key timestamps.

### Audio Recording
We're using the `arecord` api to stream audio to a specified file.

### Keyboard Recording
Here we initialize a listening event to write each key press along with the timestamp to a specified text file. 

### Analysis
Given the timestamp information we can align the audio recording and select a temporal window around the key events. The analysis folder shows an example jupyter notebook for carrying out this analysis.
