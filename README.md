# Pruebas de Frontend para PetMatch

Este directorio contiene las pruebas automatizadas para el frontend de PetMatch usando Selenium con Python y Firefox.

## 📁 Estructura del Proyecto

```
test-frontend/
├── test-auth/              # 🔐 Pruebas de Autenticación (Login/Registro)
│   ├── test_auth.py        # Script principal de pruebas
│   ├── pdf_generator.py    # Generador de reportes PDF
│   ├── requirements.txt    # Dependencias específicas
│   ├── setup.bat          # Script de instalación
│   ├── README.md          # Documentación específica
│   └── reports/           # Reportes PDF generados
├── assets/                 # Recursos compartidos
│   └── university_logo.png # Logo de la Universidad Nacional
├── geckodriver.exe        # Driver para Firefox
└── README.md             # Esta documentación
```

## Configuración

### Prerrequisitos

- Python 3.7 o superior
- Firefox instalado
- GeckoDriver descargado y en el PATH (ver instrucciones abajo)
- Frontend de PetMatch ejecutándose en http://localhost:5173

### Instalación de dependencias

```bash
cd test-frontend
pip install -r requirements.txt
```

## 🚀 Ejecución Rápida

### Pruebas de Autenticación (Recomendado)

```bash
cd test-auth
python test_auth.py
```

### Pruebas Legacy (Archivo Original)

```bash
python test_petmatch.py
```

## 📊 Características de las Nuevas Pruebas

✅ **Reportes PDF Profesionales** con logo universitario y gráficos  
✅ **Estructura Modular** separada por tipos de prueba  
✅ **Documentación Completa** de cada módulo  
✅ **Instalación Simplificada** con scripts automatizados  
✅ **Análisis Visual** con gráficos de torta y barras  
✅ **Información Detallada** de pasos ejecutados

## Instalación de GeckoDriver (para Firefox)

Para evitar los mensajes de error de PowerShell, descarga geckodriver manualmente:

1. Ve a: https://github.com/mozilla/geckodriver/releases
2. Descarga la versión para Windows (geckodriver-vX.XX.X-win64.zip)
3. Extrae el archivo `geckodriver.exe`
4. Colócalo en una de estas ubicaciones:
   - En la misma carpeta que `test_petmatch.py`
   - En tu carpeta `C:\Windows\System32`
   - En cualquier carpeta que esté en tu variable PATH

Alternativamente, puedes agregar la carpeta donde está geckodriver a tu PATH de Windows.

## Descripción de las pruebas

### Prueba 1: Login Usuario Dueño

- **Credenciales**: juan@example.com / Password123
- **Flujo**: Login → Verificar redirección a `/public` → Logout
- **Objetivo**: Verificar que un dueño de mascota puede iniciar sesión correctamente

### Prueba 2: Login Clínica Veterinaria

- **Credenciales**: veterinaria@sanpatricio.com / Clinic123
- **Flujo**: Login → Verificar redirección a `/requests` → Logout
- **Objetivo**: Verificar que una clínica veterinaria puede iniciar sesión correctamente

### Prueba 3: Registro de Nuevo Dueño

- **Datos de prueba**:
  - Nombre: Carlos Rodríguez
  - Email: carlos.rodriguez@email.com
  - Teléfono: 3118622827 (formato colombiano)
  - Dirección: Carrera 15 #45-30, Bogotá
  - Contraseña: MiPassword123
- **Flujo**: Registro → Cerrar ventana
- **Objetivo**: Verificar que el formulario de registro para dueños funciona correctamente
- **Nota**: Los datos no se guardan permanentemente en el sistema

### Prueba 4: Registro de Nueva Clínica

- **Datos de prueba**:
  - Nombre: Veterinaria Los Andes
  - Email: info@veterinarialosandes.com
  - Teléfono: 3029876543 (formato colombiano)
  - Dirección: Avenida 68 #125-40
  - Localidad: Engativá, Suba, Usaquén, Chapinero o Kennedy (la primera disponible)
  - Contraseña: ClinicPassword123
- **Flujo**: Registro → Cerrar ventana
- **Objetivo**: Verificar que el formulario de registro para clínicas funciona correctamente
- **Nota**: Los datos no se guardan permanentemente en el sistema

## Características de las pruebas

- **Firefox**: Usa Firefox como navegador (más estable que Chrome en algunos casos)
- **Aislamiento**: Cada prueba abre y cierra su propio navegador
- **Limpieza**: Automáticamente cierra sesiones activas antes de empezar
- **Alertas**: Maneja automáticamente los alerts de JavaScript
- **Esperas inteligentes**: Usa WebDriverWait para elementos dinámicos
- **Logging detallado**: Muestra el progreso paso a paso
- **Tiempos aumentados**: Esperas más largas para mayor estabilidad

## Notas importantes

1. **Servidor frontend**: Asegúrate de que tu frontend esté ejecutándose en `http://localhost:5173`
2. **Firefox**: Debe estar instalado en el sistema
3. **GeckoDriver**: Se requiere para controlar Firefox
4. **Ventana maximizada**: El navegador se abre en ventana completa
5. **Timeouts**: Esperas de hasta 10 segundos para elementos dinámicos

## Solución de problemas

### Error: "geckodriver not found"

- Descarga geckodriver desde: https://github.com/mozilla/geckodriver/releases
- Colócalo en tu PATH o en la misma carpeta

### Error: "Firefox not found"

- Instala Firefox desde: https://www.mozilla.org/firefox/

### Error: "element not found"

- Verifica que el frontend esté ejecutándose
- Comprueba que no hayan cambios en los selectores CSS

### Versión alternativa

- Si hay problemas con `test_petmatch.py`, usa `test_petmatch_simple.py`
- La versión simple es más estable y no depende de webdriver-manager
