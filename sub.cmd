@echo off
cls
set PATH=%PATH%;
:my_loop
IF %1=="" GOTO completed
  python E:\Git\Subtitile-Downloader-gt\abc.py %1
  SHIFT
  GOTO my_loop
:completed