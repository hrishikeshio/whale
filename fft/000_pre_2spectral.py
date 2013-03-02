# vi: spell spl=en
import sys
import scipy
import numpy         # For array manipulation
import scipy.fftpack # For Fast Fourier Transform
import aifc          # For reading AIFF files
import struct        # For converting binary data inside the AIFF files.
#import pylab         # To make plots.
#import csv           # To read csv files.
#import re            # 
#import sklearn

# Each clip is 2 seconds long with  2000 samples per second.
number_of_samples = 4000

def read_single_clip( filename ) :
    """Read a sinle aiff file"""
    f = aifc.open( '../Raw/data/' + filename )
    n = f.getnframes()
    assert n == number_of_samples
    signal = scipy.zeros( n )
    # TODO this is the slow way of doing it.
    # Unpacking an entire byte string might be faster.
    for i in range(0,n) :
        # Samples are stored Big indian '>'
        signal[ i ] = struct.unpack(">h", f.readframes( 1 ) )[0]

    return signal


def read_two_clips( kind, n, last ):
    """Read two consecutive clips."""
    filename_cur  = '%s/%s%d.aiff' % ( kind, kind, n )
    filename_post = '%s/%s%d.aiff' % ( kind, kind, n+1 )

    s2 = read_single_clip( filename_cur )
    if ( last ) :
        s3 = read_single_clip( filename_cur )
    else :
        s3 = read_single_clip( filename_post )

    signal = numpy.concatenate( (s2, s3) )
    return signal


# Compute the spectrum of a clip
# This is done by repeatedly computing a fft with a short
# window, while sliding the window of the whole example.
#
def get_spectrum( clip_id, kind, last ):
    signal   = read_two_clips( kind, clip_id, last )
    t        = scipy.linspace(0,4,2*number_of_samples)
    spectrum = scipy.zeros( (400, number_of_samples/100 ) ) 
    n = 0
    for i in range(0, number_of_samples, 100) :
        sub_signal = signal[i:(i+400)] # number_of_samples]
        spectrum[:,n]= abs(scipy.fft(sub_signal))
        n = n + 1
    return spectrum

def reduce( clip_id, kind, last=False ) :
    """Reduce the information in from a clip to a single row of numbers
    that can be fed to a learning algorithm
    """

    # Compute the spectrum of the clip
    spectrum = get_spectrum( clip_id, kind, last )
    # Use only part of the spectrum (Filter hight and low frequences)
    spectrum = spectrum[20:50,0:number_of_samples]
    # Compute a wheighted average for each sample.

    for x in numpy.nditer(spectrum, flags=['external_loop'], order='F'):
        tot_sum = numpy.sum( x )
        i = 0.0
        w_avg = 0.0
        for el in x :
            w_avg =  w_avg + el/tot_sum*i
            i = i + 1

        print ("%.1f" % w_avg),
    print


def reduce_set( kind, count ):
    """Reduce a set of clips"""
    for clip_id in xrange(1,count) :
        reduce( clip_id, kind )
    reduce( count, kind, last=True )

if len( sys.argv ) == 2 :
    kind = sys.argv[1]
    if  kind == 'test' :
        reduce_set( 'test', 54503 )
    elif kind == 'train' :
        reduce_set( 'train', 30000 )
    else:
        exit(1)

