# Given an a sorted array , where do you insert the new element n

import bisect
def index_bisect(a,x):
    # in case when the values is aleready present in the collection , bisect.bisect returns next index., therefore should use bisect_left
    i = bisect.bisect_left(a,x)
    if (i!=len(a)) and a[i]==x:
        return i
    else:
        return bisect.bisect(a,x)

if __name__ == '__main__':
    collection = [1,2,4,5,6]
    index = bisect.bisect(collection, 3)
    print(index)
    # if want to insert into the given sorted array do the following 
    bisect.insort(collection, 3)
    print(collection)
    print(index_bisect(collection,3))

