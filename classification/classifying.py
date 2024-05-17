import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

pca = PCA(n_components= 2)
Xraw = pd.read_csv("datasets/allStatsFiltered.csv")
ycoll = Xraw.pop('isallstar')

scaler = StandardScaler()

scaledData = scaler.fit_transform

Xstand = pd.DateFrame(scaledData , columns = Xraw.columns)

principalcomponents = pca.fit_transform(Xstand)


def accuracies(Xmat, yvec):
    Xmat['augment'] = 1
    eta = 0.001

    weightVector , iterations = perceptronLearningRule(Xmat, yvec , eta)


    pass
    



def perceptronLearningRule(Xaug, yvec, eta):


    pass







