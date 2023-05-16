import string
import nltk


def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree

def lower(text):
    return text.lower()

def remove_stopwords(text):
    stopwords = nltk.corpus.stopwords.words('english')
    splitted = text.split(" ")
    output= [i for i in splitted if i not in stopwords]
    output = ' '.join(output)
    return output



def lemmatizer(text):
    wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()
    splitted = text.split(" ")
    print(splitted)
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in splitted]
    lemm_text = ' '.join(lemm_text)
    return lemm_text

#example
a = "Very hard Earthquake in Syria!! The President saves the people! #earthquake."

a = remove_punctuation(a)
print(a)
a = lower(a)
print(a)
a = remove_stopwords(a)
print(a)
a = lemmatizer(a)
print(a)

