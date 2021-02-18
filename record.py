from numpy import fft
import pyaudio
import numpy as np
import wave
from scipy.fftpack import fft
import matplotlib.pyplot as plt




class Mic:
    def __init__(self,CHANNELS=1,nCHUNK=4,RATE = 44100):
        self.CHUNK = 1024 * nCHUNK
        self.FORMAT = pyaudio.paInt16
        self.RATE = RATE
        self.CHANNELS = CHANNELS
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK)


    @property   
    def analysis(self):
        return self.AudioAnalysis(self)

            
    @property
    def output(self,informitiveMode=False,dtype=np.int16): 
        ''' return Live output as real time data -> numpy array'''
        first_time = 1
        if informitiveMode and first_time == 1:
            first_time=0
            print("Live recording ...")
            
        #????? THE  AUCTUAL FUNCTION
        byte_data = self.stream.read(self.CHUNK)
        data = np.frombuffer(byte_data, dtype=dtype)
        if dtype == np.int16:return data
        else: return data[::2] + 127


    def record_output(self,duration=2,asFloat=False,dtype=np.int16):
        '''return numpy concat array of --duration-- raw output   {default:2 sec}'''
        
        FRAMES = [np.frombuffer(self.stream.read(self.CHUNK), dtype=dtype) for _ in range(0,int(self.RATE/self.CHUNK*duration))]
        FRAMES = np.concatenate(FRAMES,axis=0)
        if asFloat: return FRAMES.astype(np.float32)
        return FRAMES


    def record_toFile(self,duration=3,output_file="outputfile.wav",informitiveMode=True,stop_stream=True):
        '''record --duration-- long to the --outputfile-- you provide as default it's outputfile.wav  '''

        if informitiveMode: print("Start recording ...")

        #storing output to list 
        FRAMES = [self.stream.read(self.CHUNK) for _ in range(0,int(self.RATE/self.CHUNK*duration))]
        

        #close every stream open
        if stop_stream:
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
        if informitiveMode: print("Saving The recording ...")

        # svaing  the list to a file
        wf = wave.open(output_file,'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(FRAMES))
        if informitiveMode: print("Complete")



    def plot(self,ylim=2**15,figSize=(10, 5)):
        plt.ion()
        fig, ax = plt.subplots(figsize=figSize)
        x = np.arange(0, 2*self.CHUNK, 2)
        line, = ax.plot(x,np.random.rand(self.CHUNK))
        ax.set_ylim(-ylim, ylim)
        ax.set_xlim(0, self.CHUNK)
        #?? #process 
        while True:
            line.set_ydata(self.output)
            fig.canvas.draw()
            fig.canvas.flush_events()


    class AudioAnalysis:
        '''an experment class to perform some audio opration in the audio data'''
        def __init__(self,outerSelf):
            self.outerSelf = outerSelf
        
        def getfft(self):
            '''apply fourier transform to the output of the data -> numpy array'''
            return fft(self.outerSelf.output)
        
        

        
           
    










    

    


        





    
