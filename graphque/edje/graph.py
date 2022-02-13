# class Graph:
#     def __init__(self):
#         self.edg_list={}
#         with open('graph.txt','r') as fp:
#             n=int(fp.readline())
#             e_list=[]
#             for i in range(n):
#                 (sv,ev,w)=fp.readline().split()

#     def transformEdges(self):
#         pass
#     def sortEdges(self):
#         pass

def edg_w(t):
    return t[2]
class Graph:
    def __init__(self):
        self.edg_list = {}
        with open('graph.txt', 'r') as fp:
            n = int(fp.readline())
            e_list = []
            for i in range(n):
                (sv, ev, w) = fp.readline().split()
                self.edg_list[(sv,ev)]=w
    def transformEdges(self):
        e_list = [(sv, ev, int(w)) for (sv, ev), w in self.edg_list.items()]
        return(e_list)
    def sortEdges(self):
        G = sorted(g.transformEdges(), key = edg_w)
        return G
g = Graph()
