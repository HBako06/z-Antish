@echo off
setlocal enabledelayedexpansion

for %%A in (1 2 3 4 5 6 7 8 9) do (
    md "%%A"
)

echo Carpetas creadas de la A a la Z.
pause
