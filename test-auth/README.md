# Pruebas de Autenticación - PetMatch

Este módulo contiene las pruebas automatizadas para el sistema de autenticación de PetMatch, incluyendo login y registro de usuarios y clínicas veterinarias.

## 📋 Descripción

Las pruebas de autenticación verifican:

- ✅ Login de usuarios dueños de mascotas
- ✅ Login de clínicas veterinarias
- ✅ Registro de nuevos usuarios
- ✅ Registro de nuevas clínicas veterinarias
- ✅ Validación de formatos (teléfonos colombianos, emails)
- ✅ Navegación post-autenticación
- ✅ Extracción de datos de perfil
- ✅ Cierre de sesión

## 🛠️ Instalación

1. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Verificar Firefox y geckodriver:**
   - Tener Firefox instalado
   - Geckodriver debe estar en el PATH o en la carpeta del proyecto

## 🚀 Ejecución

### Ejecutar todas las pruebas:

```bash
python test_auth.py
```

### Ejecutar prueba específica:

```bash
python test_auth.py test_login_usuario
python test_auth.py test_login_veterinaria
python test_auth.py test_register_and_login_owner
python test_auth.py test_register_and_login_clinic
```

## 📊 Reportes PDF

Cada ejecución genera automáticamente:

### � Reporte Consolidado Único

- `reporte_resumen_autenticacion_YYYYMMDD_HHMMSS.pdf`

El reporte incluye:

- 🎯 Logo de la Universidad Nacional de Colombia (tamaño optimizado)
- 🏛️ Información académica: Ingeniería de Software 2, Grupo Cobras, Proyecto Pet-Match
- 🥧 Gráfico de torta profesional con porcentajes, colores y leyenda mejorada
- 📊 Gráfico de barras con degradados de color, cuadrícula y valores en barras
- 📋 Resumen general con tabla profesional y colores institucionales
- � Tabla de detalles con filas alternadas y mejor legibilidad
- 🎨 Títulos centrados con colores institucionales azules
- 📏 Márgenes optimizados y espaciado profesional
- 📅 Pie de página con información académica completa y timestamp

## 📁 Estructura de Archivos

```
test-auth/
├── test_auth.py           # Archivo principal de pruebas
├── pdf_generator.py       # Generador de reportes PDF
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Esta documentación
├── reports/              # Carpeta de reportes generados
    └── reporte_resumen_*.pdf  # Reporte consolidado únicamente
```

## 🔧 Configuración

### Datos de Prueba Predefinidos:

**Usuario Existente:**

- Email: `juan@example.com`
- Password: `Password123`

**Clínica Existente:**

- Email: `veterinaria@sanpatricio.com`
- Password: `Clinic123`

**Nuevos Registros:**

- Formato teléfono: 10 dígitos colombianos (ej: 3118622827)
- Localidades válidas: Engativá, Suba, Usaquén, Chapinero, Kennedy

## 📝 Características Técnicas

- **Selenium WebDriver 4.15.2** para automatización
- **Firefox** como navegador de pruebas
- **ReportLab 4.0.4** para generación de PDFs
- **Esperas explícitas** para estabilidad
- **Manejo de errores** robusto
- **Extracción de datos** inteligente
- **Validación de resultados** automática

## 🎯 Objetivos de las Pruebas

1. **Funcionalidad:** Verificar que el sistema de autenticación funciona correctamente
2. **Usabilidad:** Confirmar flujos de navegación intuitivos
3. **Validación:** Asegurar que las validaciones de formulario funcionan
4. **Integración:** Verificar la correcta integración frontend-backend
5. **Documentación:** Generar evidencia formal de las pruebas ejecutadas
