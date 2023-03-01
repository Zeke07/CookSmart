import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv('food_coded.csv')
print(df)
print()

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

# Extract keywords from the desired columns
keywords = []
for column in ['diet_current']:
	text = ""

	for item in df[column]:
		text += str(item)

	tokens = word_tokenize(text.lower())
	keywords += [word for word in tokens if word.isalpha() and word not in stop_words]

# Create a word cloud
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10, colormap='copper').generate(' '.join(keywords))

# Display the word cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()