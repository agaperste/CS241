def binarysearch (value, mylist):
    left= 0
    right= len(mylist)-1
    mid= int((left+right)/2)
	
    while left!=right:
	    if mylist[mid]<value:
		left = mid + 1
	    elif mylist[mid]>value:
		right = mid -1
	    else:
		pass
	    mid= int((left+right)/2)
	    
    if mylist[mid] == value:
	return mid
    else:
	return None
    
def recbinarysearch (value, mylist, left, right):
    #recursive is a function within a function
    mid  = (left + right) // 2
    if left > right:
	return None
    elif mylist[mid] < value:
	return recbinarysearch (value, mylist, mid+1, right)
    elif mylist[mid] < value:
	return recbinarysearch (value, mylist, left, mid-1)
    elif mylist[mid] == value:
	return mid
    else:
	return None


a = [1,3,5,7,9,11,13,15]
index = binarysearch (9,a)
print index

index2 = recbinarysearch (11, a, 0, 7)
print index2
