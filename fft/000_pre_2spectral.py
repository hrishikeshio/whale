import scipy
import numpy         # For array manipulation
import scipy.fftpack # For Fast Fourier Transform
import aifc          # For reading AIFF files
import struct        # For converting binary data inside the AIFF files.
import pylab         # To make plots.


# 2 seconds, 2000 samples per second.
number_of_samples = 4000


def read_single( filename ) :
    f = aifc.open( 'train19050.aiff' )
    n = f.getnframes()
    assert n == number_of_samples
    signal = scipy.zeros( n )
    # TODO this is the slow way of doing it.
    for i in range(0,n) :
        # Big indian '>'
        signal[ i ] = struct.unpack(">h", f.readframes( 1 ) )[0]

    return signal


def read_samples( kind, n ):
    filename_pre  = '%s%d.aiff' % ( kind, n-1 )
    filename_cur  = '%s%d.aiff' % ( kind, n )
    filename_post = '%s%d.aiff' % ( kind, n+1 )

    s1 = read_single( filename_pre )
    s2 = read_single( filename_cur )
    s3 = read_single( filename_post )

    signal = numpy.concatenate( (s1, s2, s3) )
    return signal


def example() :
    f = aifc.open( 'train19050.aiff' )

    print f.getnchannels()
    print f.getsampwidth()
    n = f.getnframes()

    # Time ranges is from 0 to 2 seconds.
    t      = scipy.linspace(0,2,n)
    signal = scipy.zeros( n )

    # Compute the range of frequences
    freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])

    # TODO this is the slow way of doing it.
    for i in range(0,n) :
        # Big indian '>'
        signal[ i ] = struct.unpack(">h", f.readframes( 1 ) )[0]

    FFT = abs(scipy.fft(signal))

    # Make a time and frequence plot
    pylab.subplot(211)
    pylab.plot(t,signal)
    pylab.subplot(212)
    pylab.plot(freqs,20*scipy.log10(FFT),'x')
    pylab.show()





signal = read_samples( 'train', 19050 )
t      = scipy.linspace(0,6,3*number_of_samples)

spectrum = scipy.zeros( (100, number_of_samples ) ) # number_of_samples) )
for i in range(0, number_of_samples ) :
    print (i,i+number_of_samples) 
    sub_signal = signal[i:i+ 100] # number_of_samples]
    spectrum[:,i]= abs(scipy.fft(sub_signal))

pylab.pcolor(spectrum)
pylab.colorbar()
pylab.show()


