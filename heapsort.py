#!/usr/bin/env python3.3
# heapsort.py -- Implements heapsort on a list of numbers

def heapsort(l):
 
  for start in range((len(l)-2)/2, -1, -1):
    siftdown(l, start, len(l)-1)
 
  for end in range(len(l)-1, 0, -1):
    l[end], l[0] = l[0], l[end]
    siftdown(l, 0, end - 1)
  return l
 
def siftdown(l, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and l[child] < l[child + 1]:
      child += 1
    if l[root] < l[child]:
      l[root], l[child] = l[child], l[root]
      root = child
    else:
      break