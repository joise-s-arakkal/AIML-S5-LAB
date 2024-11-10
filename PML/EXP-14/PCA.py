from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(100,5)
pca = PCA().fit(X)
var_exp = pca.explained_variance_ratio_
cum_var_exp = np.cumsum(var_exp)
plt.plot(range(1,len(var_exp)+1), pca.explained_variance_ratio_, 'ro-',
linewidth=2)
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.show()
