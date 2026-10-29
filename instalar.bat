@echo off
REM Instala tudo e deixa o site pronto. Rode UMA vez (duplo clique).
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py makemigrations base reserva
python manage.py migrate
echo.
echo === Agora crie o usuario administrador (para acessar /admin) ===
python manage.py createsuperuser
echo.
echo Pronto! Para ligar o site, de dois cliques em iniciar.bat
pause
