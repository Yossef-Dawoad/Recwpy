from record import Recorder
from scipy.fftpack import fft
mic = Recorder()

data = mic.data
fft_data = mic.analysis.getfft() 
print(fft_data)
mic.LivePlot()