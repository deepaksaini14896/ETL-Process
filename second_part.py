import pandas as pd
from nltk.tokenize import word_tokenize
import re

# Extract the data form directory
def extract():
    # Read article
    try:
        # Read file
        data = pd.read_csv("Input_Data/articles.csv")
        transformation(data)
        
    except Exception as e:
        print("Data extract error" + str(e))

# Transformation the data from data provider
def transformation(data):
    # Count word from article text
    try:
        text = data['text'].tolist()
        data = {}
        
        for i in range(len(text)):
            word = re.sub('[^A-Z]', ' ', text[i].upper())
            tokenize_word = word_tokenize(word)
            
            for w in tokenize_word:
                if w in data.keys():
                    data[w] +=1
                else:
                    data[w] = 1
        
        word = list(data.keys())
        count = list(data.values())
        new_data = {'Word' : word, 'Count': count}
        data = pd.DataFrame(new_data).sort_values(by=['Word'])
        load(data)

    except Exception as e:
        print("Data transformation error" + str(e))

# Write data provided by transformer
def load(data):
    # Write article data
    try:
        data.to_csv('Output_Data/output_2.csv',index=False)

    except Exception as e:
        print("Data load error" + str(e))
        
extract()