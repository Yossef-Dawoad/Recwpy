# Recwpy

## Record with Python 
a simple python file that enables you to record live from your microphone, record to wav file 
and even plot live data from your microphone
## **Note**: for now I am building a python package that wraps this module and a lot of useful functions so if you want to contribute feel free to check out the library which is being developed

### How to Setup
Clone the repo and you need to have pyaudio install
```
pip install pyaudio
```
or if you are in windows 
```Shell
pip install pipwin
pipwin install pyaudio
```
it provides you with prebuild pyaudio package

### how to Run
 cd to Recwpy Folder and type:
 ```PowerShell
 python main.py
 ```

## Docs

you first need to init the Record Class
```python
from record import Mic
mic = Mic()
```
after initializing the class you can get direct data from your microphone
```python
mic.output
```
mic.output is numpy array that contains the first chunk of information about the mic input

if you need just to record to wav file run

```python
mic.record_toFile(duration = 3, output_file="outputfile.wav", informitiveMode=True, stop_stream=True)
```
`informitiveMode=True`
is your friend if you want to get a glance of what happening behind the scene

<hr>

Now the Cool part How to Plot Your Mic Output Live just as simple as Writing:
```python
  mic = Mic()
  mic.plot()
```

# New Functionality of the Class

```python
mic = Mic() 
mic.analysis.getfft()
```
`mic.analysis` a class add new functionality to perform some audio analysis in the output you getting from your microphone
as of now, it's in development and just has one function which is `getfft()`

