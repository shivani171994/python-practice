#taking name and age as in input from user and telling on which year the person will turn 100

import datetime

name = input('Enter your name : ')
age = int(input ('Enter your age : '))
now = datetime.datetime.now()
diff = 100-age

print ('Hello {0} currently your age is {1} and you will be on you age of 100 after {2}'.format(name,age,now.year+diff))
