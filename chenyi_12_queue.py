#coding：utf-8

class Queue(object):
    def __init__(self):
        self.__list=[]
    def is_empty(self):
        """判断列表是否为空"""
        return self.__list==[]
    def enqueue(self,item):
        """进队列"""
        self.__list.append(item)
    def dequeue(self):
        """出队列"""
        return self.__list.pop(0 )

    def size(self):
        """队列的大小"""
        return len(self.__list)

if __name__=="__main__":
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.is_empty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())