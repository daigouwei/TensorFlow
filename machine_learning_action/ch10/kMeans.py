import numpy as np

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float, curLine))
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))

def randCent(dataSet, k):
    n = np.shape(dataSet)[1]
    # centroids = np.zeros((k, n)) # 是数组不是矩阵
    centroids = np.mat(np.zeros((k, n)))
    for j in range(n):
        minJ = np.min(dataSet[:, j])
        rangeJ = np.float(np.max(dataSet[:, j]) - minJ)
        centroids[:, j] = minJ + rangeJ * np.random.rand(k, 1)
    return centroids

if __name__ == '__main__':
    dataMat = loadDataSet('testSet.txt')
    dataMat1 = np.mat(dataMat)
    min = np.min(dataMat1[:, 0])
    max = np.max(dataMat1[:, 0])
    randCent(dataMat1, 2)
    res1 = dataMat1[0]
    res2 = dataMat1[1]
    res3 = dataMat1[0, :]
    res4 = dataMat1[1, :]
    res = distEclud(dataMat1[0], dataMat1[1])
    print('hello')