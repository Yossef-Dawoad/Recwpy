# Recwpy

## Record with Python 
a simple python file that enable you to record live from your microphone,record to wav file 
and even plot live data from your microphone

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
it provide you with prebuild pyaudio package

### how to Run
 cd to Recwpy Folder and type:
 ```PowerShell
 python main.py
 ```

## Docs

you frist need t init the Record Class
```python
from record import Mic
mic = Mic()
```
after inializ the class you can get dirctly data form your microphone
```python
mic.ouput
```
mic.data is numpy array contain the frist chunk of infromation about the mic input

if you need just to record to wav file run

```python
mic.record_toFile(duration = 3, output_file="outputfile.wav", informitiveMode=True, stop_stream=True)
```
`informitiveMode=True`
is your friend if you want to get glance of what happening behind the seen

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
as of now it's in devlopment and just has one function witch is `getfft()`

