from __future__ import generators
import sys
import math

class priorityDictionary(dict):
    def __init__(self):
        self.__heap = []
        dict.__init__(self)

    def smallest(self):
        '''Find smallest item after removing deleted items from front of heap.'''
        if len(self) == 0:
            raise (IndexError, "smallest of empty priorityDictionary")
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            insertionPoint = 0
            while 1:
                smallChild = 2*insertionPoint+1
                if smallChild+1 < len(heap) and heap[smallChild] > heap[smallChild+1] :
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break
                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]

    def __iter__(self):
        '''Create destructive sorted iterator of priorityDictionary.'''
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]
        return iterfn()

    def __setitem__(self,key,val):
        '''Change value stored in dictionary and add corresponding pair to heap.
Rebuilds the heap if the number of deleted items gets large, to avoid memory leakage.'''
        dict.__setitem__(self,key,val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            self.__heap.sort()  # builtin sort probably faster than O(n)-time heapify
        else:
            newPair = (val,key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and newPair < heap[(insertionPoint-1)//2]:
                heap[insertionPoint] = heap[(insertionPoint-1)//2]
                insertionPoint = (insertionPoint-1)//2
            heap[insertionPoint] = newPair

    def setdefault(self,key,val):
        '''Reimplement setdefault to pass through our customized __setitem__.'''
        if key not in self:
            self[key] = val
        return self[key]


def dist(a, b):
    y=b[1]-a[1]
    x=(b[2]-a[2]) * math.cos(math.radians((b[1]+a[1])/2))
    return(math.sqrt(x**2+y**2)*6371)


def d2(G,start,end):
    D = {}	# dictionary of final distances
    P = {}	# dictionary of predecessors
    Qu = priorityDictionary()   # est.dist. of non-final vert.
    Qu[start] = 0

    for v in Qu:
        D[v] = Qu[v]
        if v == end: break

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    w=w

            elif w not in Qu or vwLength < Qu[w]:
                Qu[w] = vwLength
                P[w] = v

    return (P)

def reconstruct_path(G, start, goal):
    flag=0
    P = d2(G,start,goal)
    current = goal
    path = [current]
    while current != start:
        if current not in P:
            print("IMPOSSIBLE")
            flag=1
            break
        else:
            current=P[current]
            path.append(current)
    if flag==0:        
       path.reverse()
       for i in path: print(stop_name[i][0])


start_point = input(); start_point = start_point[9:]
end_point = input() ;end_point = end_point[9:]
stop_name={}
route={}
arret=[0 for i in range(9)]
n = int(input())
for i in range(n):
    arret=input().split(',')
    arret[0]=arret[0][9:]; arret[1]=arret[1][1:-1]; arret[3]=float(arret[3]); arret[4]=float(arret[4])
    stop_name[arret[0]]=[arret[1],arret[3],arret[4]]
m = int(input())
for i in range(m):
    a,b=input().split(' ')
    a=a[9:]; b=b[9:]
    if a not in route: route[a] ={}
    route[a][b]=dist(stop_name[a],stop_name[b])

X3 = reconstruct_path(route,start_point,end_point)
