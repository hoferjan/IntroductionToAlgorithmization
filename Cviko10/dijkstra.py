class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf') #stays only if we travel form the same vertex, probably changes
        self.previousVertex = None #stays only if we travel form the same vertex, probably changes
        self.targets = [] #gets generated in GetVertexes(), list of tuples (targetVertex, distance)


class Edge:
    def __init__(self, source, target, weight): #weight is the "cost" of travel
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.visited = []
        self.vertexes = []
        self.queue = []

    #find the shortest path to each vertex from sourceId to all other vertexes and save it as vertex.minDistance
    def computePath(self, sourceId):
        vert = self.numtovertex[sourceId]
        vert.minDistance = 0
        #source added to visited and all edges added to the queue
        temp = vert
        for edge in temp.edges:
            self.addToQueue(edge)
        while len(self.queue) != 0:
            smallest = self.getSmallest()
            previous_temp = self.numtovertex[smallest.source]
            temp = self.numtovertex[smallest.target]
            if temp.minDistance > previous_temp.minDistance + smallest.weight:
                temp.minDistance = previous_temp.minDistance + smallest.weight
                temp.previousVertex = previous_temp
            for edge in temp.edges:
                if self.numtovertex[edge.target].minDistance > temp.minDistance + edge.weight:
                    self.numtovertex[edge.target].minDistance = temp.minDistance + edge.weight
                    self.numtovertex[edge.target].previousVertex = temp
                    self.addToQueue(edge)
        # for vertex in self.vertexes:
        #     print(vertex.minDistance)

    def getShortestPathTo(self, targetId): #start from target, you go to previous node until there is no other previous node, remembering all the vertex.ids in the process
        tmp_node = self.numtovertex[targetId]
        route = []
        while tmp_node != None: #we would be at the end of the list
            route.append(tmp_node)
            tmp_node = tmp_node.previousVertex
        return route[::-1]

    # creates dicitionary from vertexes of class Vertex and edges of class Edge
    def createGraph(self, vertexes, edgesToVertexes):
        for vertex in vertexes:
            for edge in edgesToVertexes:
                if edge.source == vertex.id:
                    vertex.edges.append(edge)
            self.vertexes.append(vertex)

    def resetDijkstra(self):
        self.visited = []
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None

    #method that decides returns all vertexes from djikstra algorithm in a list, creates dictionaries(numtovertex,vertextonum)
    def getVertexes(self):
        self.createTranslation() #calls to create dictionaries
        return self.vertexes

    #unncecary method that returns ids from all vertexes in self.vertexes
    def returnId(self):
        Ids = []
        for vertex in self.vertexes:
            Ids.append(vertex.id)
        return Ids

    #method that returns targets from all vertexes in self.vertexes
    def returnTargets(self):
        targets = []
        for vertex in self.vertexes:
            targets.append(vertex.targets)
        return targets

    #sub function for computePath that returns the shortest path from source to anywhere taht has not been visited yet
    def findLightestEdge(self, sourceVertex):
        self.visitedToId()
        lightestEdge = Edge(None, None, float('inf'))
        for vertex in self.vertexes:
           if vertex == sourceVertex:
               for edge in vertex.edges:
                   if edge.target not in self.visitedIds and edge.weight < lightestEdge.weight:
                       lightestEdge = edge
        return lightestEdge #returns as an edge

    def createTranslation(self):
        vertextoid = {}
        idtovertex = {}
        for vertex in self.vertexes: #to create dictionaries of vertexes
            vertextoid[vertex] = vertex.id
            idtovertex[vertex.id] = vertex
        self.numtovertex = idtovertex
        self.vertextoid = vertextoid

    def visitedToId(self):
        ids = []
        for vertex in self.visited:
            ids.append(vertex.id)
        self.visitedIds = ids
        return self.visitedIds

    def addToQueue(self, edge):
            self.queue.append(edge)

    def getSmallest(self):
        temp = Edge(None,None,float('inf'))
        for edge in self.queue:
            if temp.weight > edge.weight:
                temp = edge
        self.queue.remove(temp)
        return temp


