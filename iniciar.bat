@echo off
REM Depois de rodar o instalar.bat uma vez, use este arquivo para ligar o site.
call venv\Scripts\activate
python manage.py runserver
