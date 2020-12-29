# Here are all the installs and imports you will need for your word cloud script and uploader widget
'''
!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
'''
# Final Project
# Create a dictionary with words and word frequencies that 
# can be passed to the generate_from_frequencies function of the WordCloud class.

# Once you have the dictionary, use this code to generate the word cloud image:
'''
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")
'''

file = open('774-0.txt')
file_contents = file.read()
file.close()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
    "www", "org", "com", "ltd", "co", "ebook", "email"]
    
    # LEARNER CODE START HERE
    #    
    # Removing punctuation from text/string
    clean_file_contents = ""
    
    for character in file_contents:
        if character.isalpha() is True:
            clean_file_contents = clean_file_contents + character
        else:
            clean_file_contents = clean_file_contents + " "

    # Seperate the text into Words
    # list_file_contents = []
    list_file_contents = clean_file_contents.split()

    #Check for uninteresting Words in list
    clean_list = []
    for word in list_file_contents:
        if word.lower() not in uninteresting_words:
            clean_list.append(word.lower())
        
    #Creating frequencies dictionary
    frequencies = {}
    for word in clean_list:
        if word not in frequencies:
            frequencies[word] = 0
        frequencies[word] += 1
'''    
    for key, value in frequencies:
        if key <= 9:
            del frequencies[item]
   
'''
print (calculate_frequencies(file_contents))
  
 #DO NOT return frequencies


    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()