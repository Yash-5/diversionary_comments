
# coding: utf-8

# In[1]:

from goose import Goose


# In[2]:

def extractArticle(link):
    g = Goose()
    article = g.extract(url=link)
    return article.title, article.cleaned_text