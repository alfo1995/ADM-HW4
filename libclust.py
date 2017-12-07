# -*- coding: utf-8 -*-

class SingleLinkage:

    def __init__(self, x, k):

        '''Cluster points in k clusters'''

        self.data = x 

        n = x.shape[0]

        self.clusters = {i :[i] for i in range(n)}

        while len(self.clusters) != k:

            close = self.findClosest()

            self.merge(close[0],close[1])

        aux = {}

        idx = 0

        for k,v in self.clusters.items():

            aux[idx]=v

            idx += 1

        self.clusters = aux

        for j in self.clusters.keys():

            self.clusters[j] = sorted(self.clusters[j])



        

        

    def euc(self, x, y):

        return np.sqrt(np.sum((x-y)**2))

    

    def clustDist(self, i, j):

        '''Returns the distance between cluster i and j,

        by definition: the distance between their closest pair'''

        cd = np.Inf

        for idx in self.clusters[i]:

            for idy in self.clusters[j]:

                cd = min(cd, self.euc(self.data[idx], self.data[idy]))

        return cd

    def findClosest(self):

        '''Returns the indices of the closest clusters'''

        cd = np.Inf

        cc = None

        for i in self.clusters:

            for j in self.clusters:

                if i != j and self.clustDist(i, j) < cd:

                    cc = (i,j)

                    cd = self.clustDist(i, j)

        return cc

    def merge(self, i, j):

        '''Merge cluster i with cluster j'''

        self.clusters[i] += self.clusters[j]

        self.clusters.pop(j)