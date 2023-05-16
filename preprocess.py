import string
import nltk
import helpers
import re
import emoji


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
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in splitted]
    lemm_text = ' '.join(lemm_text)
    return lemm_text

def remove_smilies(text):
    text_without_emojis = emoji.demojize(text, delimiters=(" ", " "))
    return text_without_emojis

def remove_hashtag(text):
    # Remove hashtags with the text following them
    text_without_hashtags = re.sub(r'#\w+\s*', '', text)
    return text_without_hashtags

def remove_urls(text):
    # Remove URLs from the string
    text_without_urls = re.sub(r'http\S+|www\S+|https\S+', '', text)
    return text_without_urls

df = helpers.load_data_exp_1('tweets.csv')

df["content"] = df["content"].apply(remove_smilies)
df["content"] = df["content"].apply(remove_hashtag)
df["content"] = df["content"].apply(remove_urls)
df["content"] = df["content"].apply(remove_punctuation)
df["content"] = df["content"].apply(lower)
df["content"] = df["content"].apply(remove_stopwords)
df["content"] = df["content"].apply(lemmatizer)


df.to_csv('preprocessed_tweets.csv',index=False)


#example
# a = "Very hard Earthquake in Syria!! The President saves the people! #earthquake."

# a = remove_punctuation(a)
# print(a)
# a = lower(a)
# print(a)
# a = remove_stopwords(a)
# print(a)
# a = lemmatizer(a)
# print(a)

