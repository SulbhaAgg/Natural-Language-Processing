# Sulbha Aggarwal 

How to Run:
1) Put everything in one folder, File Names: pre-process.py, NB.py, folder: movie-review-HW2 and movie-review-small
2) open pre-process.py using a python IDE or thru command-line
	Command-Line: use 'cd' to open the directory where the files are saved.
		• For running small corpus 
            Type "pre-process.py movie-review-small/train movie-review-small/test movie-review-small-train.NB 
            movie-review-small-test.NB movie-review-small/imdb.vocab
        • For running Actual data
            Type "python pre-process.py movie-review-HW2/aclImdb/train movie-review-HW2/aclImdb/test 
            movie-review-train.NB movie-review-test.NB movie-review-HW2/aclImdb/imdb.vocab"
DO run both the commands in terminal before going to NB.py file.
3) Open NB.py
    • IDE: Run module button
    or
    • Command-Line: use 'cd' to open the directory where the files are saved.
        type 'python NB.py' then press ENTER