# Test de Solicitudes - PetMatch

Este módulo contiene las pruebas automatizadas para el sistema de gestión de solicitudes de donación de sangre para mascotas en la plataforma PetMatch.

## 📋 Descripción

Las pruebas automatizadas validan el flujo completo de gestión de solicitudes desde la perspectiva de una veterinaria:

1. **Autenticación**: Login como veterinaria con credenciales de prueba
2. **Navegación**: Acceso al módulo de solicitudes
3. **Filtrado**: Selección de solicitudes activas
4. **Gestión**: Acceso a la gestión detallada de solicitudes
5. **Postulaciones**: Visualización y conteo de mascotas postuladas
6. **Aprobación**: Proceso de aprobación de postulaciones

## 🚀 Configuración Inicial

### Requisitos

- Python 3.7+
- Firefox instalado
- GeckoDriver (se incluye o descarga automáticamente)

### Instalación

```bash
# Ejecutar el script de configuración
setup.bat

# O manualmente:
pip install -r requirements.txt
```

## 🧪 Ejecución de Pruebas

### Pruebas Completas

```bash
python test_requests.py
```

### Solo Prueba de PDF

```bash
python test_pdf.py
```

## 📄 Reportes

Los reportes se generan automáticamente en formato PDF en la carpeta `reports/`:

- Resumen detallado de todas las pruebas ejecutadas
- Análisis específico de postulaciones encontradas
- Estadísticas de éxito y fallos
- Recomendaciones y conclusiones

## 🔧 Configuración de Pruebas

### Credenciales de Prueba

- **Email**: veterinaria@sanpatricio.com
- **Contraseña**: Clinic123

### URL Base

- **Frontend**: http://localhost:5173

## 📊 Flujo de Pruebas

```
1. Login Veterinaria
   ↓
2. Navegar a /requests
   ↓
3. Click en "Activas"
   ↓
4. Click en "Gestionar"
   ↓
5. Click en "Ver mascotas postuladas"
   ↓
6. Contar postulaciones
   ↓
7. Aprobar primera postulación (si existe)
```

## 🎯 Casos de Prueba

### ✅ Casos Exitosos

- Login con credenciales válidas
- Navegación correcta entre páginas
- Detección de solicitudes activas
- Acceso a gestión de solicitudes
- Visualización de postulaciones
- Conteo correcto de postulaciones
- Aprobación de postulaciones

### ⚠️ Casos Edge

- Solicitudes sin postulaciones (válido)
- Postulaciones ya aprobadas
- Errores de conectividad temporal

## 📁 Estructura de Archivos

```
test-requests/
├── test_requests.py      # Pruebas principales
├── pdf_generator.py      # Generador de reportes PDF
├── test_pdf.py          # Prueba de generación de PDF
├── requirements.txt     # Dependencias Python
├── setup.bat           # Script de configuración
├── README.md           # Esta documentación
└── reports/            # Reportes generados
    └── *.pdf
```

## 🔍 Detalles Técnicos

### Tecnologías

- **Selenium WebDriver**: Automatización del navegador
- **Firefox**: Navegador de pruebas
- **ReportLab**: Generación de reportes PDF
- **Python**: Lenguaje de implementación

### Estrategias de Localización

- XPath para elementos con texto específico
- Múltiples selectores de respaldo
- Scroll automático para elementos fuera del viewport
- Manejo robusto de timeouts

## 📈 Métricas y Estadísticas

Las pruebas generan métricas detalladas incluyendo:

- Tasa de éxito por prueba individual
- Tiempo de ejecución
- Número de postulaciones encontradas
- Estadísticas de aprobación

## 🐛 Solución de Problemas

### Error: GeckoDriver no encontrado

```bash
# Descargar desde: https://github.com/mozilla/geckodriver/releases
# Colocar en la carpeta del proyecto o en PATH
```

### Error: Firefox no encontrado

```bash
# Instalar Firefox desde: https://www.mozilla.org/firefox/
```

### Error: Servidor no responde

```bash
# Verificar que el frontend esté ejecutándose en localhost:5173
# Verificar que el backend esté ejecutándose en localhost:8000 y 8001
```
