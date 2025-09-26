@echo off
echo === Cleaning LemniChainStatic for GitHub upload ===

:: Delete Python cleanup scripts
del /q clean_html_for_static.py 2>nul
del /q fix_navbar_loader.py 2>nul

:: Delete backup files from scripts
del /q *.bak 2>nul
del /q *.orig.html 2>nul
del /q *keep.html 2>nul
del /q *good_*.html 2>nul

:: Delete navbar duplicates
del /q "navbar - Copy.html" 2>nul
del /q "navbar - Copy (2).html" 2>nul

:: Delete misc logs
del /q dir_structure.txt 2>nul
del /q restructure.bat 2>nul

echo === Cleanup complete! ===
pause
