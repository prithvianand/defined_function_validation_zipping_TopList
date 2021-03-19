# For using this function need to install few packages that are:
'''
- file name must not contain "." instead of dots use "_".
- python-docx - using command prompt pip install pip install python-docx
- pandas - pip install pandas
'''
# then we need to import libraries:
'''
- Document From docx
- pandas
'''
from docx import Document
import pandas as pd

# this function gives us the top 10 IP Addresses providing .docx formate file name
def top_searched_IP(filename):
    # This line reads the text present in the filename
    doc =Document(filename)
    # all the paragraphs iterated one by one appended in the empty list
    p = [] # this the empty list created for appending
    for i in range(len(para)):
        x = doc.paragraphs[i].text.split() # it will separate all data by columns
        p.append(x)
    # the list is converted into the DataFrame using pandas library for data manipulation
    df = pd.DataFrame(p) # using pandas list is converted into DataFrame for easy data manipulation
    df['IP'] = df[0]
    IP_df = df['IP'].value_counts().head(10)
    IP_df.columns = ['IP','log_count']
    return IP_df # this will return top 10 IP Addresses and count