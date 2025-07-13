#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de prueba rápida para verificar la generación de PDF mejorado
"""

import os
from pdf_generator import PetMatchPDFGenerator

def test_pdf_generation():
    """Genera un PDF de prueba con datos simulados"""
    print("🔍 Generando PDF de prueba...")
    
    # Crear generador
    pdf_gen = PetMatchPDFGenerator()
    
    # Datos de prueba simulados
    test_results = {
        'test_login_usuario': {
            'success': True,
            'duration': 15,
            'description': 'Autenticación de usuario dueño de mascota existente'
        },
        'test_login_veterinaria': {
            'success': True, 
            'duration': 18,
            'description': 'Autenticación de clínica veterinaria existente'
        },
        'test_register_and_login_owner': {
            'success': True,
            'duration': 25,
            'description': 'Registro y autenticación de nuevo dueño de mascota'
        },
        'test_register_and_login_clinic': {
            'success': True,
            'duration': 28,
            'description': 'Registro y autenticación de nueva clínica veterinaria'
        }
    }
    
    # Directorio de reportes
    reports_dir = os.path.join(os.path.dirname(__file__), "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    try:
        # Generar PDF
        pdf_path = pdf_gen.generate_summary_report(test_results, reports_dir)
        print(f"✅ PDF de prueba generado exitosamente:")
        print(f"📄 {os.path.basename(pdf_path)}")
        print(f"📁 Ubicación: {pdf_path}")
        
        # Mostrar características mejoradas
        print("\n🎨 Características estéticas mejoradas:")
        print("  ✅ Logo universitario más grande (2.5x1.8 pulgadas)")
        print("  ✅ Información académica: Ingeniería de Software 2, Grupo Cobras")
        print("  ✅ Gráfico de torta profesional con colores y leyenda")
        print("  ✅ Gráfico de barras con degradados y cuadrícula")
        print("  ✅ Tablas con colores profesionales y filas alternadas")
        print("  ✅ Títulos centrados con colores institucionales")
        print("  ✅ Márgenes optimizados y espaciado mejorado")
        print("  ✅ Pie de página con información académica completa")
        
    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_pdf_generation()
