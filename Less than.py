# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user in one line.

num = int(input('Enter a number : '))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print ([i for i in a if i<num])

        
