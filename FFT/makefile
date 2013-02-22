

fft : fft.o
	gcc fft.o -lfftw3 -lm -o fft

fft.o : fft.c
	gcc -Wall -c fft.c -o fft.o

clean :
	-rm -rf fft.o fft
