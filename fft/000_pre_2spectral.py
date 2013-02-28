import scipy
import numpy         # For array manipulation
import scipy.fftpack # For Fast Fourier Transform
import aifc          # For reading AIFF files
import struct        # For converting binary data inside the AIFF files.
import pylab         # To make plots.
import csv           # To read csv files.
import re            # 
import sklearn

# Each example is 2 seconds long with  2000 samples per second.
number_of_samples = 4000


def read_single( filename ) :
    f = aifc.open( '../Raw/data/' + filename )
    n = f.getnframes()
    assert n == number_of_samples
    signal = scipy.zeros( n )
    # TODO this is the slow way of doing it.
    for i in range(0,n) :
        # Samples are stored Big indian '>'
        signal[ i ] = struct.unpack(">h", f.readframes( 1 ) )[0]

    return signal


def read_samples( kind, n ):
    filename_cur  = '%s/%s%d.aiff' % ( kind, kind, n )
    filename_post = '%s/%s%d.aiff' % ( kind, kind, n+1 )

    s2 = read_single( filename_cur )
    s3 = read_single( filename_post )

    signal = numpy.concatenate( (s2, s3) )
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

# Compute the spectrum of a training example.
# This is done by repeatedly computing a fft with a short
# window, while sliding the window of the whole example.
#
def get_spectrum( ex_id, kind ):
    signal   = read_samples( kind, ex_id )
    t        = scipy.linspace(0,4,2*number_of_samples)
    spectrum = scipy.zeros( (400, number_of_samples/100 ) ) 
    n = 0
    for i in range(0, number_of_samples, 100) :
        sub_signal = signal[i:(i+400)] # number_of_samples]
        spectrum[:,n]= abs(scipy.fft(sub_signal))
        n = n + 1
    return spectrum


def spectogram( ex_id ) :
    spectrum = get_spectrum( ex_id )
    print "Plotting"

    spectrum = spectrum[20:50,0:number_of_samples:10]
    pylab.imshow(spectrum, aspect="auto")
    pylab.show()


def slide_show() :
    with open( '../Raw/data/train.csv', 'r' ) as truefalsefile:
        trainreader = csv.reader( truefalsefile, delimiter=',' )
        trainreader.next() # Skip header
        for row in trainreader:
            print row[0], row[1]
            filename = row[0]
            score    = row[1]
            print filename
            match = re.match( r"train(\d+).aiff", filename )
            if match is None :
                exit(0)
            else :
                ex_id = match.group(1)
                if score == '1' :
                    spectogram( int( ex_id ) )


def reduce( ex_id, kind ) :

    spectrum = get_spectrum( ex_id, kind )
    # Use only part of the spectrum (Filter hight and low frequences)
    # and take a sample every 0.1 second
    spectrum = spectrum[20:50,0:number_of_samples]
    # Compute a wheighted average for each sample.

    for x in numpy.nditer(spectrum, flags=['external_loop'], order='F'):
        tot_sum = numpy.sum( x )
        i = 0.0
        w_avg = 0.0
        n = 0
        for el in x :
            w_avg =  w_avg + el/tot_sum*i
            i = i + 1

        print ("%.1f" % w_avg),
    print


def reduce_training_set():
    n = 0
    with open( '../Raw/data/train.csv', 'r' ) as truefalsefile:
        trainreader = csv.reader( truefalsefile, delimiter=',' )
        trainreader.next() # Skip header
        for row in trainreader:
            filename = row[0]
            score    = row[1]
            match = re.match( r"train(\d+).aiff", filename )
            if match is None :
                exit(0)
            else :
                ex_id = match.group(1)
                reduce( int( ex_id ), 'train' )
            n = n + 1
#            if n == 300 :
#                break

def reduce_test_set():
    for ex_id in xrange(1,54504) :
    # for ex_id in xrange(1,5) :
        reduce( int( ex_id ), 'test' )

# reduce_training_set()
reduce_test_set()

