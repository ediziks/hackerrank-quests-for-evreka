# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
from heapq import heappush, heappop


heap = []
item_lookup = set()

def push(v):
    heappush(heap, v)
    item_lookup.add(v)

def discard(v):
    item_lookup.discard(v)

def printMin():
    while heap[0] not in item_lookup:
        heappop(heap)

    print(heap[0])

cmds = {
    1: push,
    2: discard,
    3: printMin
}

n = int(stdin.readline())
for _ in range(n):
    data = list(map(int,stdin.readline().split(" ")))
    cmds[data[0]](*data[1:])
