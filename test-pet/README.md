# Pruebas de Mascotas - PetMatch

Este módulo contiene pruebas automatizadas end-to-end para el sistema de registro y gestión de mascotas en PetMatch, verificando el flujo completo desde autenticación hasta registro exitoso.

## 📁 Estructura del Proyecto

```
test-pet/
├── test_pet.py           # Script principal de pruebas
├── pdf_generator.py      # Generador de reportes PDF
├── requirements.txt      # Dependencias específicas
├── README.md            # Esta documentación
├── geckodriver.exe      # Driver para Firefox (opcional)
└── reports/             # Reportes PDF generados
    └── reporte_resumen_mascotas_*.pdf
```

## 🎯 Componentes Probados

- **PetRegistrationForm.jsx**: Formulario completo de registro de mascotas
- **PetSelectionModal.jsx**: Modal de selección de mascotas para donación
- **PetSelector.jsx**: Selector de mascotas registradas

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.7 o superior
- Firefox instalado
- GeckoDriver descargado y en el PATH
- Frontend de PetMatch ejecutándose en `http://localhost:5173`

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### Configuración de GeckoDriver

1. Descarga desde: https://github.com/mozilla/geckodriver/releases
2. Extrae `geckodriver.exe`
3. Colócalo en:
   - La misma carpeta que `test_pet.py`
   - Tu carpeta `C:\Windows\System32`
   - Cualquier carpeta en tu variable PATH

## 🧪 Ejecución de Pruebas

```bash
python test_pet.py
```

## � Reportes PDF

Cada ejecución genera automáticamente un reporte PDF profesional que incluye:

- 🏛️ **Logo de la Universidad Nacional de Colombia**
- 📋 **Descripción paso a paso** del flujo de prueba ejecutado
- 📊 **Información detallada** de la prueba (duración, resultado, descripción)
- 🎨 **Diseño temático** específico para pruebas de mascotas
- 📅 **Timestamp** e información académica

### Ubicación de Reportes:

`test-pet/reports/reporte_resumen_mascotas_YYYYMMDD_HHMMSS.pdf`

## � Descripción de la Prueba

### 🐾 Test-Pet: Registro Completo de Mascota

**Objetivo**: Verificar el flujo end-to-end de registro de una nueva mascota en el sistema.

#### Flujo de Prueba Detallado:

1. **🔑 Autenticación**

   - Login con credenciales: `juan@example.com` / `Password123`
   - Verificación de login exitoso
   - Manejo de alertas JavaScript

2. **🧭 Navegación**

   - Apertura del menú de perfil de usuario
   - Click en la opción "Mis Mascotas"
   - Verificación de llegada a la página correcta

3. **📝 Acceso al Formulario**

   - Click en botón "Registrar Mascota"
   - Apertura del formulario de registro
   - Verificación de elementos del formulario

4. **📋 Información Básica**

   - **Nombre**: TestPet
   - **Especie**: Perro (canine)
   - **Raza**: Mestizo
   - **Edad**: 3 años
   - **Peso**: 30 kg

5. **🏥 Información Médica**

   - **Tipo de sangre**: DEA 1.1+
   - **Última vacunación**: 01/07/2025
   - **Estado de salud**: Descripción detallada completa

6. **✅ Envío y Confirmación**
   - Envío del formulario completo
   - Manejo de respuesta del sistema
   - Aceptación de alert de confirmación

#### Validaciones Incluidas:

- ✅ Todos los campos obligatorios completados
- ✅ Formatos de datos correctos (edad, peso, fechas)
- ✅ Selección válida en dropdowns
- ✅ Texto suficiente en descripción de salud
- ✅ Fecha de vacunación dentro del rango válido

## ⏱️ Tiempos de Ejecución

- **Prueba completa**: ~45-60 segundos
- **Login y navegación**: ~10-15 segundos
- **Completar formulario**: ~20-25 segundos
- **Envío y confirmación**: ~5-10 segundos
- **Generación de PDF**: ~2-3 segundos

## 🔧 Características Técnicas

- **Selenium WebDriver 4.x**: Automatización web robusta
- **Firefox**: Navegador principal para estabilidad
- **ReportLab**: Generación de PDFs profesionales
- **Esperas inteligentes**: WebDriverWait para elementos dinámicos
- **Logging detallado**: Progreso paso a paso visible
- **Manejo de alertas**: JavaScript alerts automáticos
- **Limpieza automática**: Cierre de navegador y cleanup

## 🎨 Datos de Prueba Utilizados

### Usuario de Prueba:

- **Email**: juan@example.com
- **Password**: Password123
- **Tipo**: Dueño de mascota

### Mascota de Prueba:

- **Nombre**: TestPet
- **Especie**: Perro
- **Raza**: Mestizo
- **Edad**: 3 años
- **Peso**: 30 kg
- **Tipo de sangre**: DEA 1.1+
- **Última vacunación**: 01/07/2025
- **Estado de salud**: "Mascota en excelente estado de salud, sin enfermedades conocidas, vacunas al día"

## 🚨 Notas Importantes

1. **Servidor frontend**: Debe ejecutarse en `http://localhost:5173`
2. **Firefox**: Instalación requerida en el sistema
3. **GeckoDriver**: Necesario en PATH o carpeta del proyecto
4. **Ventana maximizada**: Navegador se abre en pantalla completa
5. **Timeouts**: Esperas de hasta 10 segundos para carga dinámica
6. **Datos de prueba**: No se guardan permanentemente en la base de datos
7. **Formulario**: Validación completa de todos los campos obligatorios

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

### Error: "Login failed"

- Verifica que las credenciales `juan@example.com / Password123` sean válidas
- Comprueba que el usuario esté registrado en el sistema

### Error: "Button not clickable"

- Verifica que el botón "Registrar Mascota" esté visible
- Comprueba que no haya overlays bloqueando el elemento
- El navegador debe estar maximizado

### PDF no se genera

- Verifica permisos de escritura en la carpeta `reports/`
- Comprueba que ReportLab esté instalado: `pip install reportlab`

## 📈 Métricas de Calidad

- **Cobertura**: Flujo completo end-to-end
- **Robustez**: Manejo de errores y timeouts
- **Documentación**: Reporte PDF detallado
- **Mantenibilidad**: Código modular y comentado
- **Eficiencia**: Prueba única y completa
