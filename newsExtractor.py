import newspaper

def extractArticle(link, getKeywords=False, getAuthors=False):
    article = newspaper.Article(url=link)
    article.download()
    article.parse()
    ans = [article.title, article.text]
    if getKeywords:
        article.nlp()
        ans += [article.keywords]
    if getAuthors:
        ans += [article.authors]
    return tuple(ans)