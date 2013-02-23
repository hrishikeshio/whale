Kaggle Whale Competition
========================

Code for the 
[Kaggle Whale Detection challenge](http://www.kaggle.com/c/whale-detection-challenge).

Directory Structure
===================

This repository contains the following directories:

* raw - raw data as received from kaggle.
* processed - Processed data files
* Subset - small subset of the raw data to debug the algorithms.
* FFT - Code for Fast Fourier Transform to convert the data from
  the time to the frequency domain.
* tools - common tools.
* models - All learning models go here
* sample - sample data files by kaggle. Out here for quick testing

Note to Frans:
Use file naming in order of running them so it is easier for others to follow
eg. 00_preprocess.py
01_pca.py
02_rf.py
03_postprocessing.py
Also I would prefer to use small caps for file and folder names



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
Apply learning algorithms

Note: We could use this file as a blog entry. 

Preprocessing
--------------

hrishi :
I am going to create a python script to separate out files which are negative (no whale upcall). Concatenate them using audacity
 and use it to train a noise reduction algorithm in audacity or elsewhere. Then use this profile on positive train files and see result.

