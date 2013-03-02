#
#
#

predictions.csv : rf.r reduced_test.csv reduced_train.csv
	R --vanilla < rf2.r

reduced_test.csv : 000_pre_2spectral.py
	python $< test > $@

reduced_train.csv : 000_pre_2spectral.py
	python $< train > $@

fft : fft.o
	gcc fft.o -lfftw3 -lsndfile -lm -o fft

fft.o : fft.c
	gcc -std=gnu99 -Wall -c fft.c -o fft.o

clean :
	-rm -rf fft.o fft
	-rm predictions.csv
	-rm reduced_train.csv
	-rm reduced_test.csv

