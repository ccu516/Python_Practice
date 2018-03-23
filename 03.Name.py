
## different from import and execute ##


import name_read ## show: name_read
exec(open('name_read.py').read()) ## show: __main__


## show where python find .py or .pyc
import sys
print(sys.path)