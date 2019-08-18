
import queue as Q


def Prims(G,s):
	length = len(G)
	pi = [-1]*length
	dist = [100 for _ in range(length)]
	colour = ['white']*length
    colour[s] = 'gray'
    dist[s] = 0
    q = Q.PriorityQueue()
    q.puts([0,s])
    while(q.empty()):
    	u = q.get()
    	colour[u[1]]='black'
    	for i in G[u]:
    		v = i[0]
    		w = i[1]
    		if(colour[v]!='black' and w < dist[v]):
    			pi[v]=u
    			d[v]=w
    			if(colour[v]=='white'):
    				q.put([dist[v],v])
    				colour[v]='gray'
    print(dist)
    print(pre)

G = {0:[[1,4],[2,1]],1:[[4,4]],2:[[1,2],[3,4]],3:[[4,4]],4:[]}
Prims(G,0)
