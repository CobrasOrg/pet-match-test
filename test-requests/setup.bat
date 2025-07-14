@echo off
echo ========================================
echo   SETUP PRUEBAS DE SOLICITUDES
echo   Universidad Nacional de Colombia
echo ========================================

echo.
echo Instalando dependencias de Python...
pip install -r requirements.txt

echo.
echo Verificando estructura de carpetas...
if not exist "reports\" mkdir reports

echo.
echo Copiando geckodriver si es necesario...
if not exist "geckodriver.exe" (
    if exist "..\geckodriver.exe" (
        copy "..\geckodriver.exe" .
        echo Geckodriver copiado exitosamente
    ) else (
        echo ADVERTENCIA: geckodriver.exe no encontrado
        echo Descarga geckodriver desde: https://github.com/mozilla/geckodriver/releases
    )
)

echo.
echo ========================================
echo Setup completado!
echo.
echo Para ejecutar las pruebas:
echo   python test_requests.py
echo.
echo Para ejecutar solo la generacion de PDF:
echo   python test_pdf.py
echo ========================================
