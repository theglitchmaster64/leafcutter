import random

class HeapItem:
    def __init__(self,priority,data=None):
        self.priority = priority
        self.data = data

    def __repr__(self):
        return str(str(self.priority)+':'+str(self.data))

class Heap:
    def __init__(self,type='max'):
        if type == 'max':
            self.mul = 1
        elif type == 'min':
            self.mul = -1
        else:
            return 'invalid type: type must be min or max'
        self.array = []
        self.top = -1

    def insert(self,item):
        self.array.append(item)
        self.top +=1
        self.heapify(self.top)

    #bottom up heapify
    def heapify(self,index):
        while(index > 0):
            parent = (index-1)//2
            if (self.array[parent].priority*self.mul < self.array[index].priority*self.mul):
                (self.array[parent],self.array[index])=(self.array[index],self.array[parent])
            index = parent
        return 'done'

    #top down heapify
    def heapify2(self):
        index = 0
        while(True):
            left = index*2 + 1
            right = index*2 + 2
            try:
                if (self.mul*self.array[index].priority > self.mul*self.array[right].priority and self.mul*self.array[index].priority > self.mul*self.array[left].priority):
                    return 'done'
                if self.mul==1:
                    largest = max((self.array[right].priority,right),(self.array[left].priority,left))[1]
                else:
                    largest = min((self.array[right].priority,right),(self.array[left].priority,left))[1]
                (self.array[index],self.array[largest])=(self.array[largest],self.array[index])
                index = largest
            except IndexError:
                if (left > self.top):
                    return 'done'
                else:
                    if (self.mul*self.array[index].priority>self.mul*self.array[left].priority):
                        pass
                    else:
                        (self.array[index],self.array[left])=(self.array[left],self.array[index])
                return 'done'


    def get_top(self):
        if (self.top <0 ):
            return 'heap is empty'
        else:
            (self.array[0],self.array[-1])=(self.array[-1],self.array[0])
            top_item = self.array.pop()
            self.top -=1
            self.heapify2()
            return top_item

    def __repr__(self):
        ret_str=''
        for i in range(0,len(self.array)):
            ret_str+=str(self.array[i])+'\n'
        return ret_str
