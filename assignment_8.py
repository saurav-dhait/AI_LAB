path = '/kaggle/input/sentiment-analysis-for-mental-health/Combined Data.csv'
dataset = pd.read_csv(path)

print("Dataset Info:")
print(dataset.info())

print("Missing Values:")
print(dataset.isnull().sum())

import plotly.express as px
fig = px.histogram(dataset, x='status', title='Distribution of Mental Health Status')
fig.show()
dataset['statement'] = dataset['statement'].fillna('')
print("Missing Values:")
print(dataset.isnull().sum())
dataset['text_length'] = dataset['statement'].apply(lambda x: len(str(x).split()))

fig = px.scatter(dataset, x='status', y='text_length', title='Text Length vs Mental Health Status')
fig.show()
