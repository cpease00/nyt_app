import pandas as pd
df = pd.read_csv('./package/all_trump_clean_csv.csv', encoding='latin-1')
df = df[['id', 'president_id', 'headline', 'url', 'section', 'word_count',
       'date', 'keywords']]
trump_data = df.to_dict('records')
