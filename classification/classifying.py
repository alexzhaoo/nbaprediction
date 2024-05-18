import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.impute import SimpleImputer

def accuracies(Xmat, yvec):
    onescolumn = np.ones((Xmat.shape[0], 1))
    
    Xmat = np.concatenate((Xmat, onescolumn), axis=1)
    eta = 0.001

    weightVector  = perceptronLearningRule(Xmat, yvec , eta)

    weightVector = weightVector / np.linalg.norm(weightVector)


    samples , features = Xmat.shape

    zvec = np.dot(Xmat, weightVector)

    perceptronPred = zvec >= 0

    accuracy = np.sum(perceptronPred == yvec)/ len(yvec)

    return accuracy


def perceptronLearnijngRule(Xaug, yvec, eta=1):
    imax = 10000
    estweights = np.ones((Xaug.shape[1], 1))

    for i_used in range(imax + 1):
        missed = 0
        weights = estweights
        rvec = np.zeros_like(yvec)


        scores = np.dot(Xaug, estweights)

        qvec = scores >= 0
        rvec = yvec - qvec
        estweights = estweights + eta * np.dot(Xaug.T, rvec)


        missed = np.linalg.norm(rvec, 1) > 0

        if not missed:
            weights = estweights
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







