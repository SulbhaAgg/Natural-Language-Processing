import os
import json


def bagOfWords( trainData , testData , classes ):
    processedFeatureVectors = open( "movie-review-test.NB", 'r', encoding="utf8")
    for line in processedFeatureVectors.readlines():
        vector = json.loads(line)
        trainData.append(vector)
        word = list(vector.keys())[0]
        if word in classes:
            classes[word].append(vector[word])
        else:
            classes[word]  = [vector[word]]
    processedFeatureVectors.close()

trainData = []
testData = {}
classes = {}

bagOfWords( trainData , testData , classes )