from deep_translator import MyMemoryTranslator, GoogleTranslator
import pandas as pd
import numpy as np
import concurrent.futures
import helpers


i=0
translated_dfs = []

def translate_batch(translate_session, tweet):
    translated = translate_session.translate_batch(list(tweet))

    return translated

def chunk_handling(session, chunk):
    chunk["content"] = translate_batch(session, chunk["content"])
    return chunk


def append_result(result):
    global i
    i+=1
    print(i)
    translated_dfs.append(result)



df = helpers.load_data_exp_1('part_1.csv')
#first remove eniglish
df_without_english = df[df['language'] != 'en'] 

#split in chunks of 100 for batch to google translate
chunks_df_without_english = np.array_split(df_without_english, len(df_without_english) // 100)


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit the tasks to the thread pool
    futures = [executor.submit(chunk_handling, GoogleTranslator(source='auto', target='en'), item) for item in chunks_df_without_english]

    # Add the append_result callback to each future
    for future in concurrent.futures.as_completed(futures):
        future.add_done_callback(lambda f: append_result(f.result()))


result = pd.concat(translated_dfs, ignore_index=True)
result.to_csv('out_part_1.csv',index=False)





