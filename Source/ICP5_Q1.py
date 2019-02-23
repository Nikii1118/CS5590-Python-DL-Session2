import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")
from sklearn.metrics import silhouette_score
# Load the data in collegeData
collegeData = pd.read_csv('College.csv')
print(collegeData.head())
print(collegeData.describe())
# extracting 4 coloums from dataset college that is books,enroll,room.board,grad.rate according to position
x = collegeData.iloc[:,[11,4,10,18]]
#y = collegeData.iloc[:-1]
# to visualize the extracted columns
sns.FacetGrid(collegeData, hue="Private", size=4).map(plt.scatter, "Books", "Enroll")
sns.FacetGrid(collegeData, hue="Private", size=4).map(plt.scatter, "Room.Board", "Grad.Rate")
plt.show()
# to normalize the data
normalized_X=preprocessing.normalize(x)
# implementing clustering
kmeans=KMeans(n_clusters=4, max_iter=1000)
kmeans=kmeans.fit(x)
labels=kmeans.predict(x)
centriods=kmeans.cluster_centers_
print(centriods)
# accuracy of the normalized data
score = silhouette_score (normalized_X, labels, metric='euclidean')
print("silhoutee_score:",score)
# visualiing the plot of clustering
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title('K-Means Clustering')
plt.scatter(normalized_X[:, 0], normalized_X[:, 1], c=labels, cmap=plt.cm.Paired)
plt.show()




