import gensim

def saveModel(filename, topicCount, outFile="out.lda"):
    corpus = gensim.corpora.MalletCorpus(filename)
    model = gensim.models.LdaModel(corpus, id2word=corpus.id2word, alpha='auto', num_topics=topicCount)
    model.save(outFile)