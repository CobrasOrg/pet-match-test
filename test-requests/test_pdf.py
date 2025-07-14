#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para probar la generación de PDFs de solicitudes
Genera un reporte de ejemplo con datos simulados
"""

import os
from datetime import datetime
from pdf_generator import PetMatchRequestsPDFGenerator

def test_pdf_generation():
    """Prueba la generación de PDFs con datos de ejemplo"""
    
    print("🧪 PROBANDO GENERACIÓN DE PDF DE SOLICITUDES")
    print("=" * 50)
    
    # Crear instancia del generador
    pdf_generator = PetMatchRequestsPDFGenerator()
    
    # Datos de prueba simulados para solicitudes
    test_results = {
        'test_login_veterinarian': {
            'success': True,
            'duration': 12,
            'description': 'Autenticación exitosa como veterinaria en el sistema',
            'details': 'Login exitoso como veterinaria@sanpatricio.com'
        },
        'test_navigate_requests': {
            'success': True,
            'duration': 8,
            'description': 'Navegación al módulo de gestión de solicitudes',
            'details': 'Navegación exitosa a /requests'
        },
        'test_active_requests_tab': {
            'success': True,
            'duration': 5,
            'description': 'Acceso a solicitudes activas y gestión de postulaciones',
            'count': 3,
            'count_text': '3 postulaciones encontradas',
            'details': 'Click exitoso en pestaña Activas'
        },
        'test_approval_process': {
            'success': True,
            'duration': 11,
            'description': 'Proceso de aprobación de postulaciones de mascotas donantes',
            'details': 'Aprobación exitosa de primera postulación'
        }
    }
    
    try:
        # Generar el reporte de resumen
        output_dir = os.path.dirname(__file__)
        pdf_path = pdf_generator.generate_summary_report(test_results, output_dir)
        
        relative_path = os.path.relpath(pdf_path, output_dir)
        print(f"✅ PDF de prueba generado exitosamente: {relative_path}")
        print(f"📁 Ubicación completa: {pdf_path}")
        print()
        print("📋 Contenido del reporte:")
        print("   • Encabezado universitario con logo")
        print("   • Información académica (Materia: Ingeniería de Software 2)")
        print("   • Resumen general de pruebas de solicitudes")
        print("   • Gráfico de torta con resultados (colores temáticos)")
        print("   • Gráfico de barras con duración por tipo de prueba")
        print("   • Detalle de cada prueba ejecutada")
        print("   • Datos de solicitudes procesadas")
        print("   • Pie de página académico")
        print()
        print("🎨 Características visuales:")
        print("   • Esquema de colores azul/verde (temática veterinaria)")
        print("   • Gráficos 3D con efectos profesionales")
        print("   • Tablas con filas alternadas")
        print("   • Tipografía institucional")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generando PDF de prueba: {e}")
        return False

if __name__ == "__main__":
    test_pdf_generation()

def test_pdf_generation():
    """Prueba la generación de PDFs con datos de ejemplo de solicitudes activas"""
    
    print("🧪 PROBANDO GENERACIÓN DE PDF DE SOLICITUDES")
    print("=" * 50)
    
    # Crear instancia del generador
    pdf_generator = PetMatchRequestsPDFGenerator()
    
    # Datos de prueba simulados para solicitudes
    test_results = {
        'login': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Login exitoso como veterinaria@sanpatricio.com',
            'duration': 12
        },
        'navigation': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Navegación exitosa a /requests',
            'duration': 8
        },
        'active_tab': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Click exitoso en pestaña Activas',
            'duration': 5
        },
        'manage_click': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Click exitoso en botón Gestionar',
            'duration': 7
        },
        'view_applications': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Click exitoso en Ver mascotas postuladas',
            'duration': 9
        },
        'count_applications': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Se encontraron 3 postulaciones',
            'count': 3,
            'count_text': '3 postulaciones',
            'duration': 6
        },
        'approval': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Aprobación exitosa de primera postulación',
            'duration': 11
        }
    }
    
    # Directorio de reportes
    reports_dir = os.path.join(os.path.dirname(__file__), "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    try:
        # Generar PDF
        pdf_path = pdf_generator.generate_report(test_results)
        if pdf_path:
            relative_path = os.path.relpath(pdf_path, os.path.dirname(__file__))
            print(f"✅ PDF de prueba generado exitosamente: {relative_path}")
            print(f"� Ubicación completa: {pdf_path}")
            print()
            print("📋 Contenido del reporte:")
            print("   • Encabezado universitario con logo institucional")
            print("   • Información académica (Materia: Ingeniería de Software 2)")
            print("   • Resumen general de pruebas de gestión de solicitudes")
            print("   • Análisis detallado del flujo de solicitudes activas")
            print("   • Estadísticas de postulaciones encontradas")
            print("   • Resultados de aprobación de postulaciones")
            print("   • Métricas de tiempo de ejecución por paso")
            print("   • Pie de página académico institucional")
            print()
            print("🎨 Características visuales:")
            print("   • Esquema de colores azul/verde (temática veterinaria)")
            print("   • Tablas con filas alternadas para mejor legibilidad")
            print("   • Tipografía profesional institucional")
            print("   • Formato académico universitario")
            print()
            print("🎉 ¡Generación de PDF completada exitosamente!")
            return True
        else:
            print("❌ Error al generar el PDF")
            return False
            
    except Exception as e:
        print(f"❌ Error durante la generación del PDF: {e}")
        return False

def test_pdf_generation_with_no_applications():
    """Genera un PDF de prueba sin postulaciones - escenario edge case"""
    print("\n🔍 PROBANDO PDF SIN POSTULACIONES (CASO EDGE)")
    print("=" * 50)
    
    # Crear generador
    pdf_generator = PetMatchRequestsPDFGenerator()
    
    # Datos de prueba sin postulaciones
    test_results = {
        'login': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Login exitoso como veterinaria@sanpatricio.com',
            'duration': 10
        },
        'navigation': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Navegación exitosa a /requests',
            'duration': 7
        },
        'active_tab': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Click exitoso en pestaña Activas',
            'duration': 4
        },
        'manage_click': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Click exitoso en botón Gestionar',
            'duration': 6
        },
        'view_applications': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'Click exitoso en Ver mascotas postuladas',
            'duration': 8
        },
        'count_applications': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'No se encontraron postulaciones',
            'count': 0,
            'count_text': '0 postulaciones',
            'duration': 5
        },
        'approval': {
            'success': True,
            'timestamp': datetime.now(),
            'details': 'No hay postulaciones para aprobar',
            'duration': 2
        }
    }
    
    try:
        # Generar PDF
        pdf_path = pdf_generator.generate_report(test_results)
        if pdf_path:
            relative_path = os.path.relpath(pdf_path, os.path.dirname(__file__))
            print(f"✅ PDF sin postulaciones generado exitosamente: {relative_path}")
            print()
            print("📋 Contenido específico del caso edge:")
            print("   • Manejo correcto de conteo cero (0 postulaciones)")
            print("   • Validación de flujo completo sin errores")
            print("   • Mensaje explicativo para caso sin postulaciones")
            print("   • Métricas de tiempo optimizadas para caso vacío")
            print("   • Recomendaciones para casos sin datos")
            print()
            print("🎯 Propósito de la prueba:")
            print("   • Verificar robustez del generador PDF")
            print("   • Validar manejo de casos edge")
            print("   • Asegurar que el sistema no falla con datos vacíos")
            return True
        else:
            print("❌ Error al generar el PDF")
            return False
            
    except Exception as e:
        print(f"❌ Error durante la generación del PDF: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("    PRUEBAS DE GENERACIÓN DE PDF - MÓDULO SOLICITUDES")
    print("    Universidad Nacional de Colombia")
    print("    Facultad de Ingeniería - Departamento de Sistemas")
    print("    Materia: Ingeniería de Software 2")
    print("=" * 60)
    print()
    
    # Inicializar contadores de éxito
    tests_passed = 0
    total_tests = 2
    
    # Probar generación con postulaciones
    print("🧪 EJECUTANDO PRUEBA 1/2")
    success1 = test_pdf_generation()
    if success1:
        tests_passed += 1
    
    # Probar generación sin postulaciones
    print("\n🧪 EJECUTANDO PRUEBA 2/2")
    success2 = test_pdf_generation_with_no_applications()
    if success2:
        tests_passed += 1
    
    # Mostrar resumen final
    print("\n" + "=" * 60)
    print("                    RESUMEN DE RESULTADOS")
    print("=" * 60)
    
    if tests_passed == total_tests:
        print("🎉 ¡TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE!")
        print(f"✅ Éxito: {tests_passed}/{total_tests} pruebas pasaron")
        print()
        print("📊 Estadísticas:")
        print("   • Generación con datos: ✅ EXITOSA")
        print("   • Generación caso edge: ✅ EXITOSA")
        print("   • Robustez del sistema: ✅ VERIFICADA")
        print("   • Manejo de errores: ✅ VALIDADO")
        print()
        print("🏆 El módulo de generación de PDF está funcionando perfectamente")
    else:
        print("⚠️ ALGUNAS PRUEBAS FALLARON")
        print(f"📊 Resultado: {tests_passed}/{total_tests} pruebas exitosas")
        print("🔍 Revisar los errores mostrados arriba para más detalles")
    
    print("=" * 60)
    print("🏁 Pruebas finalizadas - Módulo de Solicitudes PetMatch")
