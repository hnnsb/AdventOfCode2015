@echo off
IF ["%1"]==[""] GOTO ERROR

:CREATE 
MKDIR day%1
COPY "templates\template3.py" "day%1\day%1.py"
set num=%1
set num=%num:0=%


START "" https://adventofcode.com/2015/day/%num%
echo Successfully created Day %num%
exit
GOTO END

:ERROR
echo No day was specified

:END