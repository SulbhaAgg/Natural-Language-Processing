# Sulbha Aggarwal - NLP Homework 2
# Prof Alla Rozovskaya

import os
import json
import sys
import math

vocab_file = sys.argv[5]
vocabulary = set([line.rstrip() for line in open(vocab_file)])

def removeUniqueWords(words):
    return [word for word in words if word in vocabulary]

def wordMapper(str):
    counts = {}
    for word in str:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def reviewsIntoFile(mainFolder , feature_values ):
    punctuation = {'"', '*', '+', ',', '.', '/', '<', '>', '@', '^', '_', '`', '{', '|', '~', ';' , '=' , '#' }

    for subdirs in os.listdir(mainFolder):
        folder = os.path.join(mainFolder, subdirs)
        if os.path.isdir(folder):
            for filename in os.listdir(folder):
                if filename.endswith(".txt"):
                    file = os.path.join(folder, filename)
                    inputFile = open( file, 'r' )
                    Line = inputFile.read()
                    processedText = ""
                    for character in Line:
                        if character in '!?':
                            processedText += " " + character.lower()
                        elif character not in punctuation:
                            processedText += character.lower()
                    processedText = processedText.split()
                    processedText = removeUniqueWords( processedText )
                    features = wordMapper(processedText)
                    feature_values.append( { subdirs: features })
                    inputFile.close()

# for train
feature_values = []

# train folder for actual data is "movie-review-HW2/aclImdb/train" and train folder for the small corpus is "movie-review-small/train"
train_folder = sys.argv[1]

reviewsIntoFile(train_folder , feature_values )

# train output folder for actual data is movie-review-train.NB and train output folder for the small corpus is movie-review-small-train.NB
train_output = sys.argv[3]
output_file = open( train_output , 'w' )

for vector in feature_values:
    output_file.writelines(json.dumps(vector) + "\n")


# for test
feature_values = []

# test folder for actual data is "movie-review-HW2/aclImdb/test" and test folder for the small corpus is "movie-review-small/test"
test_folder = sys.argv[2]

reviewsIntoFile( test_folder , feature_values )

# test output folder for actual data is movie-review-test.NB and test output folder for the small corpus is movie-review-small-test.NB
test_output = sys.argv[4]
output_file1 = open( test_output , 'w' )

for vector in feature_values:
    output_file1.writelines(json.dumps(vector) + "\n")





