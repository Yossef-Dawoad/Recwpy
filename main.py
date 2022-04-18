from record import Mic

mic = Mic()


# data = mic.output #* return Live output as real time data as  -> numpy array

mic.plot() ## live plot the ouput data from your microphone

# mic.record_toFile(duration=5, output_file="newfile.wav") ## record 5 second wav file

#? New Functionality
# mic.analysis.getfft() #* apply fourier transform to the output of the data -> numpy array

