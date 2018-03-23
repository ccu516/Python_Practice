
## >python 04.InputOutput.py AA BB CC

import sys
print('Hello '+sys.argv[0]+'!') ## Hello 04.InputOutput.py!



print('Hello '+sys.argv[1]+'!') ## Hello AA!
print('Hello '+sys.argv[2]+'!') ## Hello BB!
print('Hello '+sys.argv[3]+'!') ## Hello CC!



## Input

name = input('Please enter your name:')
print('Welcome',name)




## Print Syntax

print('Test'+'\r\n')
print(1, 2, 3, sep='|', end='\r\n\n')



## Write string to a file data.txt
print(1, 2, 3, sep='\n', file = open('data.txt', 'w'))


## Write string to a file data.txt
file = open('data.txt', 'w', encoding = 'UTF-8')
file.write('test')
file.close()


## Read from a file
print('Read from a file')
file = open('data.txt', 'r', encoding='UTF-8')
content = file.read()
print(content)
file.close()

## Read one line at a time
print('Read one line at a time')
file = open('data.txt', 'r', encoding='UTF-8')
while True:
    line = file.readline()
    if not line: break
    print(line, end='')
file.close()

## Read one line at a time 2
file = open('data.txt', 'r', encoding='UTF-8')
for line in file.readlines():
    print(line, end='')
file.close()