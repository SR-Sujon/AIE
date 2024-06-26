from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5)

classifier.fit(movie_dataset, labels)

movies = [
  [.45, .2, .5], 
  [.25, .8, .9], 
  [.1, .1, .9]
]
guess = classifier.predict(movies)
print(guess)