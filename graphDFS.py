#undirected graph:
#function undirectedPath which takes in array of edges and two nodes A and B
#that return a boolean indicating if there exists any path beween them or nt
def undirectedPath(graph, nodeA, nodeB):
    stack=graph[nodeA]
    processed=set()
    temp=0
    while len(stack)>0:
        elemen=stack.pop()
        if elemen==nodeB:
            return True
        processed.add(elemen)
        #print('type: {}',graph[elemen])
        for i in graph[elemen]:
            if i in stack:
                continue
            elif i not in processed:
                stack.append(i)
    return False
def buildGraph(edges):
    graph={}
    for element in edges:
        if element[0] not in graph:
            graph[element[0]]=[]
        if element[1] not in graph:
            graph[element[1]]=[]
        graph[element[0]].append(element[1])
        graph[element[1]].append(element[0])
    return graph

def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    graph = buildGraph(edges)
    return hasPath(graph, source, destination, set())

# function to convert list of edges to adjacency list graph
'''
def buildGraph(self, edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)    
    return graph '''
def hasPath( graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dst, visited) == True:
            return True
    return False
edges=[
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]
#converting edge list into adjacency list
graph1=buildGraph(edges) 
#now we got adjacency list in the form of graph
'''
{   'i': ['j', 'k'],
    'j': ['i'], 
    'k': ['i', 'm', 'l'],
    'm': ['k'], 
    'l': ['k'], 
    'o': ['n'], 
    'n': ['o'] } '''
edges2=[[0,4]]

graph3=buildGraph(edges3) 
print(graph3)
print('Size: ',len(graph3))
count=0 #199998
for i in graph3.keys():
    if len(graph3[i])>count:
        count=len(graph3[i])
print(count)
print('Start: ',graph3[59612])
print(validPath(n=100000,edges=edges3,source= 59612,destination= 79883))
print('End')
print(undirectedPath(graph=graph3,nodeA= 59612,nodeB= 79883))