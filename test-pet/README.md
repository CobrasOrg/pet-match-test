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

### 🐾 Test-Pet: Registro y Eliminación Completa de Mascota

**Objetivo**: Verificar el flujo end-to-end de registro y eliminación de una nueva mascota en el sistema.

#### Flujo de Prueba Detallado:

1. **🔑 Autenticación**

   - Login con credenciales: `mcastiblancoa@unal.edu.co` / `Mati112999`
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

   - **Nombre**: TestPetAuto
   - **Especie**: Perro (canine)
   - **Raza**: Mestizo (selección automática)
   - **Edad**: 3 años
   - **Peso**: 15.5 kg

5. **🏥 Información Médica**

   - **Tipo de sangre**: DEA 1.1+ (selección automática)
   - **Última vacunación**: Fecha válida (6 meses atrás)
   - **Estado de salud**: Descripción detallada de 405 caracteres

6. **✅ Envío y Confirmación**

   - Envío del formulario completo
   - Manejo de respuesta del sistema
   - Aceptación de alert de confirmación

7. **🗑️ Eliminación de Mascota**
   - Navegación a página "Mis Mascotas"
   - Búsqueda específica de la mascota "TestPetAuto"
   - Click en botón "Eliminar"
   - Confirmación en modal "¿Eliminar mascota?"
   - Eliminación exitosa de la mascota creada

#### Validaciones Incluidas:

- ✅ Todos los campos obligatorios completados
- ✅ Formatos de datos correctos (edad, peso, fechas)
- ✅ Selección válida en dropdowns
- ✅ Texto suficiente en descripción de salud
- ✅ Fecha de vacunación dentro del rango válido
- ✅ Registro exitoso de la mascota
- ✅ Eliminación específica de la mascota creada
- ✅ Confirmación en modal de eliminación

## ⏱️ Tiempos de Ejecución

- **Prueba completa**: ~35-45 segundos
- **Login y navegación**: ~8-10 segundos
- **Completar formulario**: ~12-15 segundos
- **Envío y confirmación**: ~3-5 segundos
- **Eliminación de mascota**: ~5-8 segundos
- **Generación de PDF**: ~2-3 segundos

## 🔧 Características Técnicas

- **Selenium WebDriver 4.x**: Automatización web robusta
- **Firefox**: Navegador principal para estabilidad
- **ReportLab**: Generación de PDFs profesionales
- **Esperas inteligentes**: WebDriverWait para elementos dinámicos
- **Logging detallado**: Progreso paso a paso visible
- **Manejo de alertas**: JavaScript alerts automáticos
- **Limpieza automática**: Cierre de navegador y cleanup
- **Eliminación inteligente**: Búsqueda específica por nombre de mascota
- **Tiempos optimizados**: Esperas reducidas para mayor eficiencia

## 🎨 Datos de Prueba Utilizados

### Usuario de Prueba:

- **Email**: mcastiblancoa@unal.edu.co
- **Password**: Mati112999
- **Tipo**: Dueño de mascota

### Mascota de Prueba:

- **Nombre**: TestPetAuto
- **Especie**: Perro
- **Raza**: Mestizo
- **Edad**: 3 años
- **Peso**: 15.5 kg
- **Tipo de sangre**: DEA 1.1+
- **Última vacunación**: Fecha válida (6 meses atrás)
- **Estado de salud**: "Mascota en excelente estado de salud general. Sin enfermedades conocidas..."

## 🚨 Notas Importantes

1. **Servidor frontend**: Debe ejecutarse en `http://localhost:5173`
2. **Firefox**: Instalación requerida en el sistema
3. **GeckoDriver**: Necesario en PATH o carpeta del proyecto
4. **Ventana maximizada**: Navegador se abre en pantalla completa
5. **Timeouts**: Esperas de hasta 15 segundos para carga dinámica
6. **Mascota temporal**: Se crea y elimina automáticamente "TestPetAuto"
7. **Formulario**: Validación completa de todos los campos obligatorios
8. **Modal de eliminación**: Confirmación requerida para eliminar mascota

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

- Verifica que las credenciales `mcastiblancoa@unal.edu.co / Mati112999` sean válidas
- Comprueba que el usuario esté registrado en el sistema

### Error: "Button not clickable"

- Verifica que el botón "Registrar Mascota" esté visible
- Comprueba que no haya overlays bloqueando el elemento
- El navegador debe estar maximizado

### Error: "Mascota no encontrada para eliminar"

- Verifica que la mascota "TestPetAuto" se haya registrado correctamente
- Comprueba que estés en la página `localhost:5173/my-pets`
- Asegúrate de que el modal de eliminación aparezca correctamente

### PDF no se genera

- Verifica permisos de escritura en la carpeta `reports/`
- Comprueba que ReportLab esté instalado: `pip install reportlab`

## 📈 Métricas de Calidad

- **Cobertura**: Flujo completo end-to-end con eliminación
- **Robustez**: Manejo de errores y timeouts
- **Documentación**: Reporte PDF detallado
- **Mantenibilidad**: Código modular y comentado
- **Eficiencia**: Prueba optimizada y completa
