#get the sentiment of text from website
#pip install newspaper3k.
#pip install textblob.
#install libraries

from textblob import TextBlob
import nltk
from newspaper import Article


# In[16]:


#get the Article

url = 'https://thomasdigital.com/bad-websites'
article = Article(url)
print(article)


#do nlp
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

#get summary of the article
text =article.summary


#print the text
print(text)


#create a TextBlob object
obj = TextBlob(text)


#this returns a value between -1 and 1
sentiment = obj.sentiment.polarity
print(sentiment)
if sentiment == 0:
    print('the text is neutral')
elif sentiment > 0:
    print('the text is positive')
else:
    print('the text is negative')







