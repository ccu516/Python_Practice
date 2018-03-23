########### Command ###########

# Command1

'''
Command2
Command3
'''

"""
Command4
Command5
"""



############## Print ##############
# seperator and end 
print(1, 2, 3, sep='|', end='\r\n\n')

# write to a file
print(1, 2, 3, file = open('data.txt', 'w'))
# read from a file
name = input('請輸入檔名：')
file = open(name, 'r', encoding='UTF-8')
content = file.read()
print(content)
file.close()


# formated print
text = '%d %.2f %s' % (1, 99.3, 'Justin')
print(text)
>> 1 99.30 Justin

print('%d %.2f %s' % (1, 99.3, 'Justin'))
>>> 1 99.30 Justin



############## If else ##############

#If Else
print ("---------------")
if True:
    print ("True")
else:
    print ("False")
print ("---------------")


if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")

############## Get Version ##############
import sys
sys.version
import pandas
pandas.__version__
import request 
request.__version__

############## List imported modules ##############
import sys
sys.modules.keys()

############## Get a module summary ##############
heip()
modules
modules pandas #List pandas API for example

############## To escape python cmd ##############
quit() #bad to use in production code. See why: https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
exit() #bad to use in production code.
sys.exit() # better way to exit code.

############## Use python command in CMD mode(w/o getting into python environment) ##############
python -c "print('Hello! Python!')"



############## Import file and attributes ##############
# Execute people.py once
import people
print(people.name)

# Get attribute from import file
from people import name
print(name)

# The second time you import won't execute code, if you want to reload:
import imp
imp.reload(people)


############## Execute specific .py file w/o loading attributes ##############
exec(open('people.py').read())

