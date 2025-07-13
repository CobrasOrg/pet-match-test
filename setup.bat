@echo off
echo Instalando dependencias para las pruebas de frontend...
pip install -r requirements.txt

echo.
echo =====================================================
echo   Pruebas de PetMatch Frontend - Configuración
echo =====================================================
echo.
echo 1. Asegúrate de que tu frontend esté ejecutándose en http://localhost:5173
echo 2. Instala Firefox si no lo tienes instalado
echo 3. Descarga GeckoDriver para evitar errores de PowerShell:
echo    - Ve a: https://github.com/mozilla/geckodriver/releases
echo    - Descarga geckodriver-vX.XX.X-win64.zip
echo    - Extrae geckodriver.exe en esta carpeta o en tu PATH
echo.
echo 4. Ejecuta las pruebas con:
echo    python test_petmatch.py
echo.
echo NOTA: Las pruebas de registro solo verifican el formulario.
echo Los datos no se guardan permanentemente.
echo.
echo ¡Listo para ejecutar las pruebas!
pause
