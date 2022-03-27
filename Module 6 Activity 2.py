# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 06:07:20 2022

@author: User
"""
#def bellman(Interation):
    


graph = [[0,1,3],[0,2,1],[0,3,7],
         [2,1,1],[2,3,4],[2,4,2],[2,0,1],
         [1,3,1],[1,2,1],[1,0,3],
         [4,3,5],[4,5,3],[4,2,2],
         [3,4,5],[3,5,6],[3,1,1],[3,2,4],
         [5,3,6],[5,4,3]]
vertex=6
router={0:'u',1:'v',2:'x',3:'w',4:'y',5:'z'}
result=[float("Inf")] * 6
number_node=[0,0,0,0,0,0]

result[0]=0
for count in range(vertex - 1):
            print('Interation',count+1)
            for u, v, w in graph:
                if result[u] != float("Inf") and result[u] + w < result[v]:
                        result[v] = result[u] + w
                        number_node[v]=number_node[u]+1
            for i in range(6):
                print(router[i],"     ",result[i])

            
        
for i in range(6):
    x=(number_node[i]-1)
    if x<0:
        x=0
    print(router[i],"distance is ",result[i],"     number of node is",x)