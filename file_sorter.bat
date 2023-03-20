@echo off
setlocal enabledelayedexpansion

:: Set the source and destination folders
set "src_folder=C:\Users\Rau\Downloads\Telegram Desktop\ChatExport_2023-03-19\files"
set "dest_folder=C:\Users\Rau\Desktop\Dest"
set "7zip_path=C:\Program Files\7-Zip\7z.exe"

:: Loop through all files in the source folder
for /r "%src_folder%" %%f in (*) do (
    :: Extract the file extension
    for /f "delims=" %%a in ("%%xf") do set "ext=%%a"


@REM     :: Create a subfolder for the file type if it doesn't exist
@REM     if not exist "%dest_folder%\!ext!" mkdir "%dest_folder%\!ext!"

@REM     :: Move the file to the appropriate subfolder
@REM     move "%%f" "%dest_folder%\!ext!\"

@REM     :: Check if the file is an archive and extract it
@REM     if "!ext!"==".zip" (
@REM         "%7zip_path%" x -o"%dest_folder%\!ext!" "%dest_folder%\!ext!\%%~nxf"
@REM     ) else if "!ext!"==".rar" (
@REM         "%7zip_path%" x -o"%dest_folder%\!ext!" "%dest_folder%\!ext!\%%~nxf"
@REM     ) else if "!ext!"==".7z" (
@REM         "%7zip_path%" x -o"%dest_folder%\!ext!" "%dest_folder%\!ext!\%%~nxf"
@REM     )
@REM )

:end
echo Done!
pause
