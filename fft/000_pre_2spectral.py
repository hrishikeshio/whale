import scipy
import scipy.fftpack
import aifc      # For reading AIFF files
import struct    # For converting binary data inside the AIFF files.
import pylab

f = aifc.open( 'train19050.aiff' )

print f.getnchannels()
print f.getsampwidth()
n = f.getnframes()

t      = scipy.linspace(0,2,n)
signal = scipy.zeros( n )

freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])

# TODO this is the slow way of doing it.
for i in range(0,n) :
    # Big indian '>'
    signal[ i ] = struct.unpack(">h", f.readframes( 1 ) )[0]

FFT = abs(scipy.fft(signal))

pylab.subplot(211)
pylab.plot(t,signal)
pylab.subplot(212)
pylab.plot(freqs,20*scipy.log10(FFT),'x')
pylab.show()

