# Sulbha Aggarwal - NLP Homework 2
# Prof Alla Rozovskaya

import json
import math

def convertList(count):
    word_occurance = []
    for key, value in count.items():
        for i in range(value):
            word_occurance.append(key)
    return word_occurance


def bagOfWords(trainData, testData, classes, data):
    processed_feature_vectors = open(data, 'r', encoding="utf8")
    for line in processed_feature_vectors.readlines():
        vector = json.loads(line)

        if data == "movie-review-train.NB" or data == "movie-review-small-train.NB" :
            trainData.append(vector)

        word = list(vector.keys())[0]

        if data == "movie-review-train.NB" or data == "movie-review-small-train.NB" :
            if word in classes:
                classes[word].append(vector[word])
            else:
                classes[word] = [vector[word]]
        else:
            if word in testData:
                testData[word].append(convertList(vector[word]))
            else:
                testData[word] = [convertList(vector[word])]

    processed_feature_vectors.close()


def nb_train(each_label_probability, each_word_probability, bag_of_words, totalReviews, classes, vocabulary, ):
    total_words_of_each_label = {}
    for label, feature_values in classes.items():
        reviews_in_a_class = len(feature_values)
        each_label_probability[label] = math.log2(reviews_in_a_class / totalReviews)
        bag_of_words[label] = {}
        total_words_of_each_label[label] = 0
        for words in feature_values:
            for word, value in words.items():
                total_words_of_each_label[label] += value
                if word in bag_of_words[label]:
                    bag_of_words[label][word] += value
                else:
                    bag_of_words[label][word] = value

        for word in vocabulary:
            total_of_each_word = 0
            if word in bag_of_words[label]:
                total_of_each_word = bag_of_words[label][word]
            each_word_probability[(word, label)] = math.log2( (total_of_each_word + 1 ) / ( total_words_of_each_label[label] + len(vocabulary) ) )

def nb_test( review , classes , vocabulary , each_label_probability, each_word_probability ):
    sum_each_label_probability = {}
    for label, reviews in classes.items():
        sum_each_label_probability[label] = each_label_probability[label]
        for word in review:
            if word in vocabulary:
                sum_each_label_probability[label] += each_word_probability[(word, label)]
    return sum_each_label_probability

def argmax(sum_each_label_probability):
    value = list( sum_each_label_probability.values() )
    key = list( sum_each_label_probability.keys() )
    return key[value.index(max(value))]

def pretty_print(each_label_probability ,each_word_probability ):
    store = "Log probability of each label:\n" + str(each_label_probability) + '\n\nLog likelihood of each word: \n'
    for key, val in each_word_probability.items():
        word = str(key[0])
        label = str(key[1])
        store += 'P(' + word + ' | ' + label + ') = ' + str(val) + '\n'
    return store

def for_naive_bayes( train , test , vocab , paramterFile, predictionsFile ):
    trainData = []
    testData = {}
    classes = {}

    bagOfWords(trainData, testData, classes, train )
    bagOfWords(trainData, testData, classes, test )

    # The vocab file actual data is
    vocabulary = set([line.rstrip() for line in open(vocab)])

    each_label_probability = {}
    each_word_probability = {}
    bag_of_words = {}

    nb_train(each_label_probability, each_word_probability, bag_of_words, len(trainData), classes, vocabulary)

    results = {True: 0, False: 0}
    predictions = "Document # \t Predicted Label \t Actual Label\n"

    i = 1
    for label, reviews in testData.items():
        for review in reviews:
            probability_set_by_label = nb_test( review , classes , vocabulary , each_label_probability, each_word_probability )
            naive_bayes_assign = argmax(probability_set_by_label)
            results[naive_bayes_assign == label] += 1
            predictions += "\t" + str(i) + "\t\t\t\t\t Predicted Class: " + naive_bayes_assign + "\t\t\t\t" + " Actual Class: " + label + "\n"
            i += 1

    output_file = open( paramterFile , 'w', encoding="utf8")
    output_file.write(pretty_print(each_label_probability , each_word_probability))
    output_file.close()
    output_file1 = open( predictionsFile  , 'w', encoding="utf8")
    accuracy = (results[True]/(results[False] + results[True])) *100
    predictions += "\n\n Total Reviews: " + str(results[False] + results[True])
    predictions += "\n Documents Predicted Correctly: " + str(results[True])
    predictions += "\n Documents Predicted Incorrectly: " + str(results[False])
    predictions += "\n Accuracy: " + str(accuracy) + "%"
    if train == 'movie-review-small-train.NB':
        predictions += "\n\n Label Probability:  Action: " + str(each_label_probability["action"]) + "\n Comedy: " + str(each_label_probability["comedy"])
    else:
        predictions += "\n\n Label Probability:  Negative: " + str(each_label_probability["neg"]) + "\n\t\t\t Positive: " +str(each_label_probability["pos"])
    output_file1.write(predictions)
    output_file1.close()

for_naive_bayes( 'movie-review-train.NB' , 'movie-review-test.NB' , 'movie-review-HW2/aclImdb/imdb.vocab' , 'movie-review-BOW.NB' , 'movie-review-Prediction.NB' )
for_naive_bayes( 'movie-review-small-train.NB' , 'movie-review-small-test.NB' , 'movie-review-small/imdb.vocab' ,  'movie-review-small-BOW.NB' , 'movie-review-small-Prediction.NB' )
