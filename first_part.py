import pandas as pd

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
    # Capitalize article text
    try:
        title = data['title'].tolist()
        text = data['text'].tolist()
        
        for i in range(len(text)):
            text[i] = text[i].upper()
        
        new_data = {'Title' : title, 'Text': text}
        data = pd.DataFrame(new_data)
        load(data)

    except Exception as e:
        print("Data transformation error" + str(e))

# Write data provided by transformer
def load(data):
    # Write article data
    try:
        data.to_csv('Output_Data/output_1.csv',index=False)

    except Exception as e:
        print("Data load error" + str(e))
        
extract()