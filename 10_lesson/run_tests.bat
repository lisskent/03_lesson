@echo off

set RESULTS=results
set REPORT=final-report
set HISTORY=%REPORT%\history

echo Cleaning up previous results...
if exist %RESULTS% rmdir /s /q %RESULTS%

echo Running tests...
pytest . --alluredir=%RESULTS%

echo Moving history to results...
if exist %HISTORY% xcopy /E /I /Y %HISTORY% %RESULTS%\history

echo Cleaning up previous report...
if exist %REPORT% rmdir /s /q %REPORT%

echo Generating Allure report...
allure generate %RESULTS% -o %REPORT%

echo Opening Allure report...
allure open %REPORT%

echo Done!
pause