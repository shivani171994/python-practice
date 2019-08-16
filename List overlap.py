#list comparrision of 2 different sized list in one line code

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = list(dict.fromkeys(a))                      #converting the list element as a dict key so that it will remove dublicate and than converting back into lis
mylist=[x for x in a for y in b if x == y]
print (mylist)

