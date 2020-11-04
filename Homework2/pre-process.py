import os
import json


vocabulary = set([line.rstrip() for line in open('movie-review-HW2/aclImdb/imdb.vocab')])

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
                    inputFile = open( file, 'r', encoding= 'utf-8')
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

# for test
feature_values = []

mainFolder = "movie-review-HW2/aclImdb/test"
reviewsIntoFile(mainFolder , feature_values )

output_file = open("movie-review-test" + ".NB", 'w', encoding="utf8")

for vector in feature_values:
    output_file.writelines(json.dumps(vector) + "\n")

# for train
feature_values = []
mainFolder = "movie-review-HW2/aclImdb/train"
reviewsIntoFile(mainFolder , feature_values )

output_file = open("movie-review-train" + ".NB", 'w', encoding="utf8")

for vector in feature_values:
    output_file.writelines(json.dumps(vector) + "\n")



