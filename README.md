Kaggle Whale Competition
========================

Code for the 
[Kaggle Whale Detection challenge](http://www.kaggle.com/c/whale-detection-challenge).

Directory Structure
===================

This repository contains the following directories:

* Raw - raw data as received from kaggle.
* Subset - small subset of the raw data to debug the algorithms.
* FFT - Code for Fast Fourier Transform to convert the data from
  the time to the frequency domain.
* Tools - common tools.

Plan
====

hrishi:

Step 1 : Preprocessing
-----------------------

I like learning algorithms. Thats I want to make their job easier.
I am going to spend time googling around and trying different tools/libraries to 

* Remove the noise with noise-removal
* Remove frequencies which do not correspong to up-call
* Removing click noises with click-removal

I will also be playing with audacity, which I highly recommend since it has a GUI, to play around with different settings 
of noise reduction, high-pass and low-pass filter.

Step 2 : Conversion
--------------------

We need to convert the resulting files in csv files. Might need to do pca / other preprocessing.


Step 3 : Learning
------------------
Aplly learning algorithms