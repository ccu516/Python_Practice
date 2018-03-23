:: --------------------------------------
:: Interpret Python Exercise in One Click
:: --------------------------------------


:: Set project directory 
set py_folder=D:\"Google Sync"\Python_Practice
:: Change directory
cd %py_folder%
cls 


:: Enter a number to executed exercise, or empty to executed python.exe 
set num=none
set file_name=none
set /p num="Enter a number:":
IF %num% EQU none (
	cls
)ELSE (
    for %%i in (%num%*.py) DO @set file_name=%%i  
    cls
)


:: let 1 can be recognized as 01
IF %file_name% EQU none (
	set num=0%num%
)
IF %num% EQU none (
	cls
)ELSE (
    for %%i in (%num%*.py) DO @set file_name=%%i  
    cls
)

python %file_name%

cmd