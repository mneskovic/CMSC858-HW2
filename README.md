# CMSC858-HW2

## Overview
This is a suffix array implementation done in Python.
The main external libraries used are fasta-reader-py for reading FASTA files, and pydivsufsort for creation of the suffix array itself. NumPy is also used to ensure the prefix table takes less space. For the prefix table, strings are hashed using a python dictionary and for each prefix key, there is a numpy array representing the interval for the prefix in the suffix array.
## Outside Sources
The only other source besides the class notes that I used for this project was the Suffix Array slides created by Ben Langmead (https://www.mimuw.edu.pl/~szczurek/TSG2/04_suffix_arrays.pdf). In particular, my original implementation had the second query binary search (finding the end of the range) done using the actual prefix (which required a different binary search as the prefix is the same for the entire range) which I replaced using their methodology (increasing the last character by 1). This allowed me to do the same type of binary search for both the start and end which made my code cleaner and more logical.
## Instructions for Running
Simply give the buildsa and querysa scripts permission to run using `chmod +x` for both scripts. Then run them as intended.