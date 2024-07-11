from movies import movie_dataset, movie_ratings

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def predict(unknown, dataset, movie_ratings, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  numerator, denominator = 0, 0
  for neighbor in neighbors:
    rating = movie_ratings[neighbor[1]]
    distance_to_neighbor = neighbor[0]
    result = rating / distance_to_neighbor
    numerator += result
    denominator += (1/distance_to_neighbor)
  return numerator/denominator

inc_2 = [0.016, 0.300, 1.022]
result = predict(inc_2, movie_dataset, movie_ratings, 5)
print(result)
