# Pruebas de Donación - PetMatch

Este módulo contiene las pruebas automatizadas para el sistema de donación de sangre de mascotas de PetMatch, verificando el flujo completo desde la búsqueda de solicitudes hasta la postulación de mascotas como donantes.

## 📋 Descripción

Las pruebas de donación verifican:

- ✅ **Flujo completo con primera solicitud**: Login, navegación, selección de primera solicitud disponible, click en botón de donación y postulación de mascota
- ✅ **Flujo completo con solicitud aleatoria**: Login, navegación, selección aleatoria entre 2da y última solicitud, postulación de mascota
- ✅ Detección inteligente de postulaciones duplicadas (HTTP 409)
- ✅ Manejo de modales de selección de mascotas
- ✅ Navegación automática entre secciones
- ✅ Validación de estados de autenticación
- ✅ Generación de reportes PDF profesionales

## 🛠️ Instalación

1. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Verificar Firefox y geckodriver:**

   - Tener Firefox instalado
   - Geckodriver debe estar en el PATH o en la carpeta del proyecto

3. **Asegurar que el servidor local esté ejecutándose:**
   - Frontend en `http://localhost:5173`
   - Backend API funcionando correctamente

## 🚀 Ejecución

### Ejecutar todas las pruebas:

```bash
python test_donations.py
```

El sistema ejecutará automáticamente:

1. **Prueba 1**: Flujo completo con primera solicitud disponible
2. **Prueba 2**: Flujo completo con solicitud aleatoria (entre 2da y última)

## 📊 Reportes PDF

Cada ejecución genera automáticamente:

### 📄 Reporte Consolidado Único

- `reporte_resumen_donaciones_YYYYMMDD_HHMMSS.pdf`

El reporte incluye:

- 🎯 Logo de la Universidad Nacional de Colombia
- 🏛️ Información académica: Ingeniería de Software 2, Proyecto Pet-Match
- 🥧 Gráfico de torta con resultados de pruebas (exitosas/fallidas)
- 📊 Gráfico de barras con tiempos de ejecución por prueba
- 📋 Resumen general con estadísticas de éxito
- 📝 Tabla detallada con descripción de cada prueba ejecutada
- 🎨 Diseño temático para donaciones (colores rosa/rojo)
- 📅 Pie de página con timestamp e información académica

## 📁 Estructura de Archivos

```
test-donations/
├── test_donations.py        # Archivo principal de pruebas
├── pdf_generator.py         # Generador de reportes PDF
├── requirements.txt         # Dependencias del proyecto
├── README.md               # Esta documentación
├── geckodriver.exe         # Driver de Firefox (si está incluido)
└── reports/                # Carpeta de reportes generados
    └── reporte_resumen_*.pdf  # Reportes consolidados
```

## 🔧 Configuración

### Datos de Prueba Predefinidos:

**Usuario Dueño de Mascota:**

- Email: `juan@example.com`
- Password: `Password123`

### URLs del Sistema:

- **Frontend**: `http://localhost:5173`
- **Página de solicitudes**: `http://localhost:5173/public`

### Comportamientos Esperados:

- **Primera solicitud**: Puede detectar postulación duplicada (comportamiento esperado del sistema)
- **Solicitud aleatoria**: Selecciona aleatoriamente entre solicitudes 2-N para mayor variabilidad
- **Detección de duplicados**: El sistema maneja correctamente HTTP 409 como éxito controlado

## 🎲 Funcionalidad Aleatoria

El sistema implementa selección inteligente:

1. **Prueba 1**: Siempre usa la primera solicitud disponible
2. **Prueba 2**: Selecciona aleatoriamente entre la 2da y última solicitud disponible

**Ejemplo**: Si hay 10 solicitudes, la Prueba 2 puede elegir cualquiera de las solicitudes 2-10.

## 📝 Características Técnicas

- **Selenium WebDriver 4.x** para automatización
- **Firefox** como navegador de pruebas
- **ReportLab** para generación de PDFs
- **Navegador persistente** entre pruebas para eficiencia
- **Detección automática de estado de login**
- **Manejo inteligente de modales y overlays**
- **Validación de respuestas HTTP 409** como comportamiento esperado
- **Selección aleatoria** para mayor cobertura de pruebas

## ⏱️ Tiempos de Ejecución

- **Prueba 1 (Primera solicitud)**: ~35 segundos
- **Prueba 2 (Solicitud aleatoria)**: ~17 segundos
- **Tiempo total estimado**: ~52 segundos
- **Generación de PDF**: ~2 segundos

## 🎯 Objetivos de las Pruebas

1. **Funcionalidad**: Verificar que el sistema de donaciones funciona end-to-end
2. **Variabilidad**: Probar diferentes solicitudes para mayor cobertura
3. **Robustez**: Manejar casos edge como postulaciones duplicadas
4. **Usabilidad**: Confirmar flujos de usuario intuitivos
5. **Documentación**: Generar evidencia formal de las pruebas ejecutadas

## 🚨 Notas Importantes

- Las pruebas requieren que el servidor frontend esté ejecutándose en `localhost:5173`
- El sistema detecta automáticamente si ya existe una sesión activa
- Las postulaciones duplicadas (HTTP 409) se consideran comportamiento esperado
- Los reportes se guardan directamente en la carpeta `reports/`

---

_Sistema de Pruebas Automatizadas - Universidad Nacional de Colombia_
