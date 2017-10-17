# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:33:53 2017

@author: SACHIN
"""
from flask import Flask, render_template, json, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('LNchatbot.html')

#NLP Logic starts
import csv
import nltk #pip install nltk
#nltk.download() # will prompt to download stanford nl corpora so download corpora and packages
from nltk.stem.lancaster import LancasterStemmer
# word stemmer
stemmer = LancasterStemmer()
#nltk.download('punkt')
training_data = []

with open('training_data.csv',  "rt", encoding='utf-8') as csvfile:
    crawledFilesReader = csv.reader(csvfile, delimiter=',')
    for row in crawledFilesReader:
        training_data.append({"classVal":row[0],"sentenceVal":row[1]})
print ("%s sentences of training data" % len(training_data))
print(training_data)

corpus_words_list = {}
class_words_list = {}
# turn a list into a set (of unique items) and then a list again (this removes duplicates)
classes = list(set([a['classVal'] for a in training_data]))
for classVal in classes:
    # prepare a list of words within each class
    class_words_list[classVal] = []

# loop through each sentence in our training data
for dataVal in training_data:
    # tokenize each sentence into words
    for word in nltk.word_tokenize(dataVal['sentenceVal']):
        # ignore a some things
        if word not in ["?", "'s"]:
            # stem and lowercase each word
            stemmed_word_val = stemmer.stem(word.lower())
            # have we not seen this word already?
            if stemmed_word_val not in corpus_words_list:
                corpus_words_list[stemmed_word_val] = 1
            else:
                corpus_words_list[stemmed_word_val] += 1

            # add the word to our words in class list
            class_words_list[dataVal['classVal']].extend([stemmed_word_val])

# we now have each stemmed word and the number of occurances of the word in our training corpus (the word's commonality)
print ("Corpus words and counts: %s \n" % corpus_words_list)
# also we have all words in each class
print ("Class words: %s" % class_words_list)


def getclass_score(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for word in nltk.word_tokenize(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words_list[class_name]:
            # treat each word with same weight
            score += 1
            
            if show_details:
                print ("   match: %s" % stemmer.stem(word.lower() ))
    return score


# finding class with the highest score
def getClassified(sentence):
    defaultClassScore=0
    classReturnVal=""
    for classKey in class_words_list.keys():
        maxClassscore=getclass_score(sentence, classKey)
        print("defaultClassScore is %s" %defaultClassScore)
        print ("Class: %s  Score: %s \n" % (classKey,maxClassscore ))
        if defaultClassScore < maxClassscore:
           defaultClassScore=maxClassscore
           classReturnVal=classKey
    print ("classreturnval is:")
    print(classReturnVal)   
    return classReturnVal 
#NLP Logic ends

keysMap={'lps':'Litigation Profile Suite','tax':'Lexis Advance Tax','icw':'Interactive Citation Workstation'}
@app.route('/getChatData',methods=['POST','GET'])
def getChatData():
    inputData =  request.form["inputChat"]
    classiFiedData= getClassified(inputData)
    classTopVal=classiFiedData.split("audience=",1)[1]
    return json.dumps({'UserInput':inputData,'BotResponse':classiFiedData,'InputCategory':keysMap[classTopVal]})

if __name__ == "__main__":
    app.run(port=5002)
