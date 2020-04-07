# importing packages for data pre processing functionalities

import nltk
nltk.download('stopwords')
nltk.download('punkt')
import csv
import pandas
import math
import numpy
from nltk.corpus import *
from nltk.tokenize import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# opening and reading through each line of review file

with open('yelp_kimos.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:

        #textual i.e., comments column of review data is being processed
        rev = row[2]

        sentence = ' '

        # setup the stop words to be removed

        stop_words = nltk.corpus.stopwords.words('english')

        #tokenize the words to ensure words are not brokendown further while removing stopwords
        word_tokens = word_tokenize(rev)

        
        #looping through each word in the csv file
        for w in word_tokens: 
            #eliminating the stop words
            if w not in stop_words:
                #removing special characters
                # if (w.isalnum() is True): 
                
                #appending List of words to string
                    
                sentence += w
                sentence += ' '
        
        

        #vaderSentiment has been imported to recognise the polarity of each review
        analyser = SentimentIntensityAnalyzer()
        score = analyser.polarity_scores(sentence)
        print(score)
        # print("{:-<40} {}".format(sentence, str(score)))

        #working with the ratings of customers
        stars = row[1]
        rating = stars[:3]
        


        with open('cleandata.csv', 'a', newline='') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow([sentence, rating])
        
