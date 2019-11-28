"""
Small program to see the performance of the Euclidean gcd algorithm in
recursive and iterative implementations.

Results unconclusive as calculations require wildly different time scales
with large spikes in data, tempted to call it bimodal but I'm no statistician
so I don't really know.
"""

from random import randint
from matplotlib import pyplot as plt
from time import time
from pandas import DataFrame as df
from gcd_iter import gcd_iter
from gcd_rec import gcd_rec

iterlist = []
reclist = []
testlist = sorted([(i, j) for i in range(1000) for j in range(i)],
           key = lambda tup : ((tup[0] + tup[1])/2))

def iter():
    for tup in testlist:
        start = time()
        res = gcd_iter(tup[0], tup[1])
        end = time()
        iterlist.append(end-start)
        
def rec():
    for tup in testlist:
        start = time()
        res = gcd_rec(tup[0], tup[1])
        end = time()
        reclist.append(end-start)
        
def main():

    iter()
    rec()
    
    new_df = df({'x': range(len(testlist)), 'iter': iterlist, 'rec': reclist})
    
    f1 = plt.figure(1)
    plt.plot('x', 'iter', data=new_df, label = 'iterative', color = 'blue')
    plt.plot('x', 'rec', data=new_df, label = 'recursive', color = 'green')
    plt.legend(loc='upper left')
    plt.show()
    
    new_new_df = df({'x': range(len(iterlist)), 'iter': sorted(iterlist), 'rec': sorted(reclist)})
    
    f2 = plt.figure(2)
    plt.plot('x', 'iter', data=new_new_df, label = 'iterative', color = 'blue')
    plt.plot('x', 'rec', data=new_new_df, label = 'recursive', color = 'green')
    plt.legend(loc='upper left')
    
    plt.show()
    
if __name__ == '__main__':
    main()