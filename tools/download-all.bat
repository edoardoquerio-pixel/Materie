@echo off
title FAD Downloader - ITS ICT Piemonte
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0download-fad.ps1" -CourseId all
echo.
echo ============================================
echo Operazione completata! Premi un tasto per chiudere.
echo ============================================
pause
