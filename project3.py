#importing all the libraries
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#getting the data from the dataframe
df = pd.read_csv("EPLStandings.csv", encoding ="latin-1")
#checking the dataframe
print(df.head())
#making a smaller data frame with only team name and coefficient
nomin=df[['Team','Coeff']]
#making a dictionary from the dataframe
d={}
for a, x in nomin.values:
    d[a]=x

#wordcloud formatting
wordcloud = WordCloud(mode="RGB",background_color='blue' ,width=1920, height=1080, colormap= 'Reds', prefer_horizontal=1, min_font_size=35 )
#plotting the word cloud with the coeffecients set as frequencies for teams 
wordcloud.generate_from_frequencies(frequencies=d)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
#a bar graph to show the coefficient disparity
nomin.plot.bar(x='Team')
plt.show()
