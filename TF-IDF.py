import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import helpers

df = helpers.load_data_exp_1('preprocessed_tweets.csv')
def get_tf_idf_matrix(df):
    df['content'].fillna('', inplace=True)
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    content = df['content']

    tfidf_matrix = vectorizer.fit_transform(content)
    # Create a DataFrame with the TF-IDF matrix
    tfidf_df = pd.DataFrame.sparse.from_spmatrix(tfidf_matrix, columns=vectorizer.get_feature_names_out())
    return tfidf_df

get_tf_idf_matrix(df)
