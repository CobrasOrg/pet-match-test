# Pruebas Automatizadas para PetMatch

Este directorio contiene las pruebas automatizadas para el sistema PetMatch usando Selenium con Python y Firefox.

## 📁 Estructura del Proyecto

```
pet-match-test/
├── test-auth/              # 🔐 Pruebas de Autenticación (Login/Registro)
│   ├── test_auth.py        # Script principal de pruebas
│   ├── pdf_generator.py    # Generador de reportes PDF
│   ├── requirements.txt    # Dependencias específicas
│   ├── README.md          # Documentación específica
│   └── reports/           # Reportes PDF generados
├── test-donations/         # 🩸 Pruebas de Donación de Sangre
│   ├── test_donations.py   # Script principal de pruebas
│   ├── pdf_generator.py    # Generador de reportes PDF
│   ├── requirements.txt    # Dependencias específicas
│   ├── README.md          # Documentación específica
│   └── reports/           # Reportes PDF generados
├── assets/                 # Recursos compartidos
│   └── university_logo.png # Logo de la Universidad Nacional
├── geckodriver.exe        # Driver para Firefox
├── CONTRIBUTING.md        # Guía de contribución
├── simple_gitflow_guide.md # Guía de flujo Git
└── README.md             # Esta documentación
```

## Configuración General

### Prerrequisitos

- Python 3.7 o superior
- Firefox instalado
- GeckoDriver descargado y en el PATH
- Frontend de PetMatch ejecutándose en http://localhost:5173

### Instalación Global de Dependencias

```bash
# Para pruebas de autenticación
cd test-auth
pip install -r requirements.txt

# Para pruebas de donación
cd test-donations
pip install -r requirements.txt
```

## 📊 Reportes PDF

Ambos módulos generan automáticamente reportes PDF profesionales que incluyen:

- 🏛️ **Logo de la Universidad Nacional de Colombia**
- 📊 **Gráficos de torta y barras** con resultados y tiempos
- 📋 **Resumen estadístico** de pruebas ejecutadas
- 📝 **Tabla detallada** de cada prueba con descripción
- 🎨 **Diseño temático** específico para cada módulo

### Ubicaciones de Reportes:

- **Autenticación**: `test-auth/reports/reporte_resumen_autenticacion_*.pdf`
- **Donación**: `test-donations/reports/reporte_resumen_donaciones_*.pdf`

## 🚀 Módulos de Pruebas Disponibles

### 🔐 Test-Auth: Pruebas de Autenticación

- **Ubicación**: `test-auth/`
- **Funcionalidad**: Login y registro de usuarios y clínicas
- **Ejecución**: `cd test-auth && python test_auth.py`
- **Características**:
  - ✅ Login de usuarios dueños de mascotas
  - ✅ Login de clínicas veterinarias
  - ✅ Registro de nuevos usuarios
  - ✅ Registro de nuevas clínicas
  - ✅ Validación de formatos y navegación

### 🩸 Test-Donations: Pruebas de Donación

- **Ubicación**: `test-donations/`
- **Funcionalidad**: Sistema completo de donación de sangre
- **Ejecución**: `cd test-donations && python test_donations.py`
- **Características**:
  - ✅ Flujo completo con primera solicitud disponible
  - ✅ Flujo completo con solicitud aleatoria (2da-última)
  - ✅ Detección inteligente de postulaciones duplicadas
  - ✅ Manejo de modales y navegación automática
  - ✅ Selección aleatoria para mayor cobertura

## 📊 Características de las Pruebas

✅ **Reportes PDF Profesionales** con logo universitario y gráficos  
✅ **Estructura Modular** separada por tipos de funcionalidad  
✅ **Documentación Completa** de cada módulo independiente  
✅ **Navegador Persistente** para eficiencia en pruebas múltiples  
✅ **Detección Inteligente** de estados y errores  
✅ **Análisis Visual** con gráficos de resultados y tiempos  
✅ **Selección Aleatoria** para mayor cobertura de casos  
✅ **Manejo de Duplicados** y casos edge automático

## ⏱️ Tiempos de Ejecución

### Test-Auth (4 pruebas):

- Login Usuario: ~15-20 segundos
- Login Clínica: ~15-20 segundos
- Registro Usuario: ~20-25 segundos
- Registro Clínica: ~20-25 segundos
- **Total**: ~70-90 segundos

### Test-Donations (2 pruebas):

- Primera Solicitud: ~35 segundos
- Solicitud Aleatoria: ~17 segundos
- **Total**: ~52 segundos

## Instalación de GeckoDriver (Firefox)

Para evitar los mensajes de error de PowerShell, descarga geckodriver manualmente:

1. Ve a: https://github.com/mozilla/geckodriver/releases
2. Descarga la versión para Windows (geckodriver-vX.XX.X-win64.zip)
3. Extrae el archivo `geckodriver.exe`
4. Colócalo en una de estas ubicaciones:
   - En la misma carpeta que `test_petmatch.py`
   - En tu carpeta `C:\Windows\System32`
   - En cualquier carpeta que esté en tu variable PATH

Alternativamente, puedes agregar la carpeta donde está geckodriver a tu PATH de Windows.

## 📋 Descripción de Funcionalidades por Módulo

### 🔐 Test-Auth: Sistema de Autenticación

#### Prueba 1: Login Usuario Dueño

- **Credenciales**: juan@example.com / Password123
- **Flujo**: Login → Verificar redirección a `/public` → Logout
- **Objetivo**: Verificar autenticación de dueños de mascotas

#### Prueba 2: Login Clínica Veterinaria

- **Credenciales**: veterinaria@sanpatricio.com / Clinic123
- **Flujo**: Login → Verificar redirección a `/requests` → Logout
- **Objetivo**: Verificar autenticación de clínicas veterinarias

#### Prueba 3: Registro de Nuevo Dueño

- **Datos de prueba**: Carlos Rodríguez, carlos.rodriguez@email.com, etc.
- **Flujo**: Registro → Validación de formulario → Cierre
- **Objetivo**: Verificar formulario de registro para dueños

#### Prueba 4: Registro de Nueva Clínica

- **Datos de prueba**: Veterinaria Los Andes, info@veterinarialosandes.com, etc.
- **Flujo**: Registro → Validación de formulario → Cierre
- **Objetivo**: Verificar formulario de registro para clínicas

### 🩸 Test-Donations: Sistema de Donación

#### Prueba 1: Flujo Completo - Primera Solicitud

- **Flujo**: Login → Navegación → Selección primera solicitud → Postulación
- **Características**: Detecta duplicados HTTP 409 como comportamiento esperado
- **Objetivo**: Verificar flujo completo con solicitud fija

#### Prueba 2: Flujo Completo - Solicitud Aleatoria

- **Flujo**: Login → Navegación → Selección aleatoria (2da-última) → Postulación
- **Características**: Mayor variabilidad en pruebas
- **Objetivo**: Verificar robustez con diferentes solicitudes

## 🔧 Características Técnicas

- **Selenium WebDriver 4.x**: Automatización web robusta
- **Firefox**: Navegador principal para estabilidad
- **ReportLab**: Generación de PDFs profesionales
- **Aislamiento**: Cada prueba maneja su propio contexto
- **Limpieza automática**: Cierre de sesiones y cleanup
- **Manejo de alertas**: JavaScript alerts automáticos
- **Esperas inteligentes**: WebDriverWait para elementos dinámicos
- **Logging detallado**: Progreso paso a paso visible
- **Navegador persistente**: Entre pruebas del mismo módulo (donations)
- **Detección de estados**: Login automático y gestión de sesiones

## 🚨 Notas Importantes

### Para ambos módulos:

1. **Servidor frontend**: Debe ejecutarse en `http://localhost:5173`
2. **Firefox**: Instalación requerida en el sistema
3. **GeckoDriver**: Necesario en PATH o carpeta del proyecto
4. **Ventana maximizada**: Navegador se abre en pantalla completa
5. **Timeouts**: Esperas de hasta 10 segundos para carga dinámica

### Específico para Test-Donations:

- **Postulaciones duplicadas**: HTTP 409 es comportamiento esperado
- **Navegador persistente**: Se mantiene entre las 2 pruebas
- **Selección aleatoria**: Varía según solicitudes disponibles

### Específico para Test-Auth:

- **Navegador independiente**: Cada prueba abre/cierra su navegador
- **Datos de prueba**: No se guardan permanentemente
- **Formularios**: Validación completa de campos

## 🛠️ Solución de Problemas

### Error: "geckodriver not found"

- Descarga geckodriver desde: https://github.com/mozilla/geckodriver/releases
- Colócalo en tu PATH o en la misma carpeta del módulo

### Error: "Firefox not found"

- Instala Firefox desde: https://www.mozilla.org/firefox/

### Error: "element not found"

- Verifica que el frontend esté ejecutándose en `localhost:5173`
- Comprueba que no hayan cambios en los selectores CSS
- Aumenta los timeouts si es necesario

### Error: "Port already in use"

- Asegúrate de que solo una instancia del frontend esté ejecutándose
- Verifica que no haya otros servicios en el puerto 5173

### PDF no se genera

- Verifica permisos de escritura en la carpeta `reports/`
- Comprueba que ReportLab esté instalado: `pip install reportlab`
