import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.impute import SimpleImputer


def accuracies(Xmat, yvec):

    onescolumn = np.ones((Xmat.shape[0], 1))
    Xmat = np.concatenate((Xmat, onescolumn), axis=1)

    eta = 0.001

    weightVector = perceptronLearningRule(Xmat, yvec, eta)


    weightVector = weightVector.ravel()


    weightVector = weightVector / np.linalg.norm(weightVector)

    zvec = np.dot(Xmat, weightVector)
    perceptronPred = zvec >= 0

    accuracy = np.sum(perceptronPred == yvec.flatten()) / len(yvec)

    return accuracy


def perceptronLearningRule(Xaug, yvec, eta=1):
    imax = 15000
    samples, features = Xaug.shape
    weights = np.ones(features).reshape(-1, 1)

    for _ in range(imax):
        missed = 0

        scores = np.dot(Xaug, weights)

        qvec = scores >= 0

        rvec = yvec - qvec.flatten()

        weights = weights + eta * np.dot(Xaug.T, rvec).reshape(-1, 1)
        
        missed = np.linalg.norm(rvec, 1) > 0

        if not missed:
            break

    return weights


pca = PCA(n_components= 2)
Xraw = pd.read_csv("datasets/allStatsFiltered.csv")
ycoll = Xraw.pop('isallstar')

Xraw = Xraw.to_numpy()

ycoll = ycoll.to_numpy()

imputer = SimpleImputer(strategy='mean')

Xrawimputed = imputer.fit_transform(Xraw)

scaler = StandardScaler()

scaledData = scaler.fit_transform(Xrawimputed)

principalcomponents = pca.fit_transform(scaledData)

print(accuracies(principalcomponents, ycoll))







