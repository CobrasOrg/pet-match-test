@echo off
echo ========================================
echo   SETUP PRUEBAS DE AUTENTICACION
echo   Universidad Nacional de Colombia
echo ========================================

echo.
echo Instalando dependencias de Python...
pip install -r requirements.txt

echo.
echo Verificando estructura de carpetas...
if not exist "reports\" mkdir reports

echo.
echo ========================================
echo Setup completado!
echo.
echo Para ejecutar las pruebas:
echo   python test_auth.py
echo.
echo Para ejecutar prueba individual:
echo   python test_auth.py test_login_usuario
echo ========================================
pause
