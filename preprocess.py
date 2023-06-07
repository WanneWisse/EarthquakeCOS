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
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # Chinese/Japanese/Korean characters
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_hashtag(text):
    # Remove hashtags with the text following them
    text_without_hashtags = re.sub(r'#\w+\s*', '', text)
    return text_without_hashtags

def remove_urls(text):
    # Remove URLs from the string
    text_without_urls = re.sub(r'http\S+|www\S+|https\S+', '', text)
    return text_without_urls

nltk.download('stopwords')
nltk.download('wordnet')

df = helpers.load_data_exp_1('data/tweets.csv')

df= df[df['language'] == 'en'] 

df["content"] = df["content"].apply(remove_smilies)
df["content"] = df["content"].apply(remove_hashtag)
df["content"] = df["content"].apply(remove_urls)
df["content"] = df["content"].apply(remove_punctuation)
df["content"] = df["content"].apply(lower)
df["content"] = df["content"].apply(remove_stopwords)
df["content"] = df["content"].apply(lemmatizer)


df.to_csv('preprocessed_tweets_english.csv',index=False)


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

