@echo off
curl -s -L -o setup.py https://gitlab.com/chamod12/iperius_win-10_github_rdp/-/raw/main/setup.py
curl -s -L -o nsetup.py https://gitlab.com/chamod12/iperius_win-10_github_rdp/-/raw/main/nsetup.py
curl -s -L -o iperius.exe "https://www.iperiusremote.com/dsir.aspx?file=IperiusRemote_Setup.exe&v=4&a=64"
curl -s -L -o show.bat https://gitlab.com/chamod12/iperius_win-10_github_rdp/-/raw/main/show.bat
curl -s -L -o loop.bat https://gitlab.com/chamod12/loop-win10/-/raw/main/loop.bat
curl -s -L -o C:\Users\Public\Desktop\Telegram.exe https://telegram.org/dl/desktop/win64
curl -s -L -o C:\Users\Public\Desktop\Winrar.exe https://www.rarlab.com/rar/winrar-x64-621.exe
curl -s -L -o wall.bat https://gitlab.com/chamod12/changewallpaper-win10/-/raw/main/wall.bat
powershell -Command "Invoke-WebRequest 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile 'C:\Users\Public\Desktop\VMQuickConfig.exe'"
pip install requests --quiet
pip install pyautogui --quiet
pip install telegraph --quiet

C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART
del C:\Users\Public\Desktop\Telegram.exe
C:\Users\Public\Desktop\Winrar.exe /S
del C:\Users\Public\Desktop\Winrar.exe
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk"
del /f "C:\Users\Public\Desktop\Unity Hub.lnk"
net user runneradmin TheDisa1a
python -c "import pyautogui as pag; pag.click(897, 64, duration=2)"
start "" "iperius.exe"
python setup.py
REM python nsetup.py
call wall.bat
