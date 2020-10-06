from queue import Queue
from stack import Stack

class GraphNode:
    def __init__(self,name,data=None):
        self.index = None
        self.name = name
        self.data = data

    def __repr__(self):
        ret_str = {'index':self.index,'name':self.name,'data':str(self.data)}
        return str(ret_str)

class Graph:
    def __init__(self,vertices=1):
        self.vertices = vertices
        self.top_index = -1
        #0=linked to self, None=not linked
        self.matrix = [[None]*vertices]*vertices
        self.nodes = []

    def grow_by_one(self):
        tmp_row = [None]*(len(self.matrix[0])+1)
        for i in self.matrix:
            i.append(None)
        self.matrix.append(tmp_row)
        self.vertices+=1

    def add_node(self,node):
        if (self.top_index + 1 >= self.vertices):
            self.grow_by_one()
            self.add_node(node)
        else:
            node.index = self.top_index + 1
            self.top_index += 1
            self.nodes.append(node)
            self.matrix[node.index][node.index]=0
        return True

    def add_link_by_index(self,index1,index2,wt=1,directed=False):
        if (index1 > self.top_index) or (index2 > self.top_index):
            return False
        else:
            if (directed == True):
                self.matrix[index1][index2] = wt
            if (directed == False):
                self.matrix[index1][index2] = wt
                self.matrix[index2][index1] = wt
            return True

    def add_link_by_name(self,name1,name2,wt=1,directed=False):
        index1 = None
        index2 = None
        for i in self.nodes:
            if i.name == name1:
                index1 = i.index
            if i.name == name2:
                index2 = i.index
        if (index1 == None):
            return '{name} does not exist in graph'.format(name=name1)
        if (index2 == None):
             return '{name} does not exist in graph'.format(name=name2)
        return self.add_link_by_index(index1,index2,wt=wt,directed=directed)

    def get_link_by_index(self,index1,index2):
        if (index1 > self.top_index or index2 > self.top_index):
            return False
        else:
            return self.matrix[index1][index2]

    def get_link_by_name(self,name1,name2):
        index1 = None
        index2 = None
        for i in self.nodes:
            if i.name == name1:
                index1 = i.index
            if i.name == name2:
                index2 = i.index
        if (index1 == None):
            return '{name} does not exist in graph'.format(name=name1)
        if (index2 == None):
            return '{name} does not exist in graph'.format(name=name2)
        return self.matrix[index1][index2]

    def get_link(self,node1,node2):
        found = [False,False]
        for i in self.nodes:
            if node1 == i:
                found[0] = True
            if node2 == i:
                found[1] = True
        if (found[0] or found[1] == False):
            return False
        else:
            return self.matrix[node1.index][node2.index]

    def build_from_dict(self,dic,directed=False):
        ''' build a graph from a dictionary adjacency list of the form {node0:[(wt,node1),(wt,node2),...etc],...etc}'''
        if (len(self.nodes) != 0):
            return 'graph is not empty'
        else:
            keys = list(dic.keys())
            for key in keys:
                self.add_node(GraphNode(str(key)))
            for key in keys:
                for item in dic[key]:
                    self.add_link_by_name(name1=str(key),name2=str(item[1]),wt=int(item[0]),directed=directed)

    def __repr__(self):
        ret_str = ''
        for i in range(0,self.vertices):
            ret_str += '\t'+self.nodes[i].name
        ret_str += '\n\n'
        for i in range(0,self.vertices):
            ret_str += self.nodes[i].name+'\t'
            for j in range(0,self.vertices):
                ret_str +=str(g.matrix[i][j])+'\t'
            ret_str +='\n'
        return ret_str

    def get_neighbors(self,node):
        for i in self.matrix[node.index]:
            print(i)

if __name__=='__main__':
    g=Graph()
    #dic = {'a':[(1,'b'),(2,'c'),(3,'d')],'b':[(1,'c'),(2,'d')],'c':[(7,'d')],'d':[(3,'a')]}
    nodes = [GraphNode(s) for s in 'abcdef']
    for node in nodes:
        g.add_node(node)
    links = [('a','b'),('b','c'),('c','d'),('e','f'),('f','a')]
    for link in links:
        g.add_link_by_name(*link,wt=2)
