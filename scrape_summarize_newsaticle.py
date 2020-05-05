#Description: Scrape and Summarize News Articles

#pip install nltk
#pip install newspaper3k

#Resources: Documentation: https://newspaper.readthedocs.io/en/latest/?source=post_page---------------------------
#           Medium Article: https://towardsdatascience.com/scrape-and-summarize-news-articles-in-5-lines-of-python-code-175f0e5c7dfc
#           Article Website: https://www.washingtonpost.com/technology/2019/07/17/you-downloaded-faceapp-heres-what-youve-just-done-your-privacy/?noredirect=on&utm_term=.f8b0b55b2805

#Import the libraries
import nltk
from newspaper import Article

#Get the article
url = 'https://www.vox.com/2020/4/17/21224866/coronavirus-update-trump-china-wuhan-bolsonaro-mandetta'
article = Article(url)

# Do some NLP
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
#Get the authors
print(article.authors)
#Get the publish date
print(article.publish_date)
print(article.top_image)
#Get the article text
# print(article.text)
#Get a summary of the article
print(article.summary)