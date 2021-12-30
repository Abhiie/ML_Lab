import nltk
from nltk.corpus import movie_reviews
import matplotlib.pyplot as plt # library for visualization
import random

nltk.download('movie_reviews')
print("Words ", movie_reviews.words(), "\n")
print("Words length ",len( movie_reviews.words()), "\n")
print("Category ", movie_reviews.categories(), "\n")
# Displays frequency of words in ‘movie_reviews’
print("Happy word ",nltk.FreqDist(movie_reviews.words())['happy'],"\n")
print(movie_reviews.fileids(),"\n")
# Prints file ids of positive reviews
print(movie_reviews.fileids('pos'),"\n");
# Prints file ids of negative reviews.
print(movie_reviews.fileids('neg'),"\n")
print("Negative ",len(movie_reviews.fileids('neg')),"\n")
print("Positive ",len(movie_reviews.fileids('pos')),"\n")
fig = plt.figure(figsize=(5, 5))
# labels for the two classes
labels = 'Positives', 'Negative'
# Sizes for each slide
sizes = [len(movie_reviews.fileids('neg')), len(movie_reviews.fileids('pos'))]
# Declare pie chart, where the slices will be ordered and plotted counter-clockwise:
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
# Display the chart
plt.show()