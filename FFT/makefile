#
#
#

fft : fft.o
	gcc fft.o -lfftw3 -lsndfile -lm -o fft

fft.o : fft.c
	gcc -std=gnu99 -Wall -c fft.c -o fft.o

clean :
	-rm -rf fft.o fft
