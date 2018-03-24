import csv
import random
import math

filename = input("Enter the filename: ")

df = []
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        df.append(row)

#Getting the lists as integers
for row in range(1, len(df)):
	df[row][:-1] = list(map(float, df[row][:-1]))

K = int(input("Enter the number of clusters to be formed: "))
iterations = int(input("Enter the number of iterations to train the algorithm: "))

#Selecting K centroids at random
centroids = []
centroid_classes = []
random.seed(1)
for i in range(K):
    rand = random.randint(1,len(df))
    centroids.append(df[rand])

#Getting the centroid for each data point
for it in range(iterations):
    data_centroids = []
    for i in range(1, len(df)):
        #Getting the closest centroids to the data points
        minimum_dist = 99999
        for centroid in centroids:
        	squared_dist = 0
        	for j in range(4):
        		squared_dist += (df[i][j] - centroid[j])**2
        		root = math.sqrt(squared_dist)
        		if root < minimum_dist:
        			minimum_dist = root
        			temp_centroid = centroid

        data_centroids.append(temp_centroid) #Contains the centroids for each data point

    #Now adjusting the centroids
    final_centroids = []
    for centroid in centroids:
        values = [list(df[i+1]) for i in range(len(data_centroids)) if data_centroids[i] == centroid]
        
        #Removing classes
        for row in values:
        	del row[-1]
        
        centroid = [float(sum(l))/len(l) for l in zip(*values)]
        final_centroids.append(centroid)

print("\n\n********* CENTROIDS GENERATED **********\n\n")
for index,i in enumerate(final_centroids):
	print("Cluster " + str(index+1) + " -> " + str(i))

feature_words = ["Sepal length", "Sepal width", "Petal length", "Petal Width"]
print("\n\nEnter an input feature to be put into a cluster: ")
features = []
for i in range(4):
	features.append(float(input("Enter " + str(feature_words[i]) + ": ")))

pred_centroid = final_centroids[0]
cluster = 0
minimum_dist = 99999
for index, centroid in enumerate(final_centroids):
	squared_dist = 0
	for j in range(4):
		squared_dist += (features[j] - centroid[j])**2
		root = math.sqrt(squared_dist)
		if root < minimum_dist:
			minimum_dist = root
			pred_centroid = centroid
			cluster = index

print("\n\nThe given features correspond to a point in ** cluster " + str(cluster+1) + " **")