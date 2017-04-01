
# coding: utf-8

# In[1]:

import newspaper


# In[2]:

def extractArticle(link, getKeywords=False, getAuthors=False):
    article = newspaper.Article(url=link)
    article.download()
    article.parse()
    ans = [article.title, article.text]
    if getKeywords:
        ans += [article.keywords]
    if getAuthors:
        ans += [article.authors]
    return tuple(ans)


# In[24]:

link = "http://timesofindia.indiatimes.com/home/environment/pollution/after-nitish-jibe-centre-ropes-in-private-companies-to-clean-ganga/articleshow/57420309.cms"
print extractArticle(link, getKeywords=True)

