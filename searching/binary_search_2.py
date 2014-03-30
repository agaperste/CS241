def binarysearch (value, mylist):
    l= 0
    r= len(mylist)-1
    m= int((l+r)/2)
	
    while l<r:
	if mylist[m]<value:
	    l = m + 1
	else:
	    r = m - 1
	m= int((l+r)/2)
	    
    if mylist[m] == value:
	return m
    else:
	return None


a = [1,3,5,7,9,11,13,15]
index = binarysearch (1,a)
print index
