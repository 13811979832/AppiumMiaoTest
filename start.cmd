@echo off

del test.log

rem ֻ�����������
rem python startTest.py

rem ֻ������ļ�
python startTest.py >> test.log 2>&1 

rem ͬʱ����������к��ļ�
rem powershell "python startTest.py 2>&1 | tee test.log" 

pause