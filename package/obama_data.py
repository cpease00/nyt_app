
# import pandas
# obama_data = pandas.read_excel(dir_path+'/all_obama.csv', names=["id", "president_id", "headline", "url", "section", "word_count", "date", "keywords"])
# clean_obama = obama_data.to_dict()
import pandas as pd
df = pd.read_csv('./package/obama_clean_csv.csv', encoding='latin-1')
df = df[['id', 'president_id', 'headline', 'url', 'section', 'word_count',
       'date', 'keywords']]
obama_data = df.to_dict('records')

#then data = df.to_dict()
