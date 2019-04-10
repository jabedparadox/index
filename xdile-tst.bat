echo Author               : Md Jabed Ali(jabed)
@echo off
set urlfile=url.txt
if exist %urlfile% (echo Preparing.............) else echo ########--  Url file dose not exist  --######## & pause
for /f %%v in ('grep -c "." url.txt ') do (set "urlcount=%%v")

rem xidel needs to placed in root directory or in environmental path.
rem wget needs to placed in root directory or in environmental path.
rem sed -i "s/\(.*\),/\1~/g" *.txt
rem xidel http://www.google.de/search?q=query --extract "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"

:b
set link=err
set tit=err
set /a a+=1
echo Getting like count from soundcloud.......... url %a%
for /f %%v in ('sed -n %a%p url.txt ') do (set "name=%%v")

curl --trace-time --retry 5 --retry-delay 3 -c cookie.txt -d "search=%name%" --dump-header headers.txt --user-agent "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0" --referer http://www.com http://www.com -o page.html



findstr /L /O /N /C:"Sorry, your search returned no results, please try again!" page.html
if /i %ERRORLEVEL% EQU 0 echo %name%,error>>fin.txt & goto :b


sed -i "s/\&//g" page.html
sed -i "s/\"//g" page.html

for /f "delims=" %%v in ('grep -o "href=http:\/\/.*" page.html') do (set "link=%%v")
for /f "delims=" %%v in ('grep -o "href=http:\/\/.*" page.html ^| grep -o ">[^<].*"') do (set "tit=%%v")
for /f "delims=" %%v in ('grep -o "<br>[ 0-9.].*" page.html ^| grep "[0-9.].*"') do (set "price=%%v")
echo "%name%","%link%","%tit%","%price%">>fin.txt
Del *.
timeout 3
goto b
sed -i "s/\&//g" page.html
sed -i "s/\"//g" page.html
grep -o "<br>[ 0-9.].*" page.html | grep "[0-9.].*"
grep -o "href=http:\/\/.*" page.html

pause
