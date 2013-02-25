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

(Frans: if you make this 010_...  020_..  ect
it makes it easier to insert a step later on. 
(BASIC use to have linenumbers, learned it there the hard way).

Also: the best way to make something reproducable is with a
shell script or even better a makefile.  The latter
allows non linear flows. i.e. tree like flow.).

Also I would prefer to use small caps for file and folder names
(Frans:  Sure. It's your repo.
I use the convention: directories start with a capital.
Filenames are always lowercase.  I find this makes it easier
to spot the directories in a terminal window.)


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




Plan Frans
==========


Step 1: Spectograms
-------------------

Compute spectograms

Results in a 4000x100 matrix for each sample.
(4000 times steps 100 frequency intencities).

Step 2: Line Up
---------------

Line up the postive training samples.
A whale call might end at the begin or end of a sample.
This makes it more difficult to train a learning algorithm on it.
So in this step the calls will be processed (possible by hand) to have the
call end at the end of the sample.

Step 3: Train
-------------

Train a RF on the training samples.
It will be trained on a small window of the sample containing the whale call.

Step 4: Predicting:
-------------------

For each test sample, slide a window over it.
For each position run the RF.  If for one of the positions the RF predicts a
whale call the prediction for the whole sample is 'Whale call'.




