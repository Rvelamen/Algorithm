from sortedcontainers import SortedList


def priority_queue():
    """
    相当于优先队列
    """
    price = SortedList()
    price.add(1)
    print(price[-1])
    print(price[0])
    price.remove(1)


from heapq import *
def heapq_func():
    """
    优先队列
    """
    heap = []
    x = 1
    n = 2
    heappush(heap, x)       #将x压入堆中
    heappop(heap)           #从堆中弹出最小的元素
    heapify(heap)           #让列表具备堆特征
    heapreplace(heap, x)    #弹出最小的元素，并将x压入堆中
    nlargest(n, iter)       #返回iter中n个最大的元素
    nsmallest(n, iter)      #返回iter中n个最小的元素

