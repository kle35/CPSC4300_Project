import pandas as pd
import translators.server as tss

data = pd.read_csv('again2.csv')
'''
for i in range(len(data)):
    text = data.loc[i, 'review']
    english_text = tss.google(text, from_language="es", to_language="en")
    data.loc[i, 'English_text'] = english_text

# save the translated data to a new CSV file
data.to_csv('translated_data.csv', index=False)
'''

for i in data.loc[data['country'] == 'United States', 'review'].index:
    text = data.loc[i, 'review']
    english_text = tss.google(text, from_language="es", to_language="en")
    data.loc[i, 'review'] = english_text

for i in data.loc[data['country'] == 'United States', 'initial_statement'].index:
    text = data.loc[i, 'initial_statement']
    english_text = tss.google(text, from_language="es", to_language="en")
    data.loc[i, 'initial_statement'] = english_text

# save the translated data to a new CSV file
data.to_csv('airpods_reviews_cleaned.csv', index=False)

'''
for i in data.loc[data['country'] == 'Mexico', ['review', 'initial_statement']].index:
    review = data.loc[i, 'review']
    statement = data.loc[i, 'initial_statement']
    english_review = tss.google(review, from_language='es', to_language='en')
    english_statement = tss.google(statement, from_language='es', to_language='en')
    data.loc[i, 'review'] = english_review
    data.loc[i, 'initial_statement'] = english_statement
'''


# save the translated data to a new CSV file
print(data)