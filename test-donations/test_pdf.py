#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para probar la generación de PDFs de donación
Genera un reporte de ejemplo con datos simulados
"""

import os
from datetime import datetime
from pdf_generator import PetMatchDonationPDFGenerator

def test_pdf_generation():
    """Prueba la generación de PDFs con datos de ejemplo"""
    
    print("🧪 PROBANDO GENERACIÓN DE PDF DE DONACIONES")
    print("=" * 50)
    
    # Crear instancia del generador
    pdf_generator = PetMatchDonationPDFGenerator()
    
    # Datos de prueba simulados para donaciones
    test_results = {
        'test_find_donation_request': {
            'success': True,
            'duration': 28,
            'description': 'Búsqueda y localización de solicitudes de donación activas en la plataforma',
            'donation_data': {
                'Mascota Receptora': 'Luna',
                'Veterinaria': 'Clínica Veterinaria San Patricio',
                'Urgencia': 'URGENCIA ALTA',
                'Solicitud': '#1',
                'Estado': 'Encontrada',
                'Fecha': datetime.now().strftime("%d/%m/%Y %H:%M")
            }
        },
        'test_apply_donation_with_pet': {
            'success': True,
            'duration': 35,
            'description': 'Postulación exitosa de mascota como donante de sangre',
            'donation_data': {
                'Mascota Receptora': 'Max',
                'Veterinaria': 'Veterinaria Los Andes',
                'Urgencia': 'URGENCIA MEDIA',
                'Solicitud': '#2',
                'Estado': 'Postulación Enviada',
                'Fecha': datetime.now().strftime("%d/%m/%Y %H:%M")
            }
        },
        'test_complete_donation_flow': {
            'success': True,
            'duration': 42,
            'description': 'Flujo completo desde búsqueda hasta confirmación de donación',
            'donation_data': {
                'Mascota Receptora': 'Bella',
                'Veterinaria': 'Hospital Veterinario Central',
                'Urgencia': 'URGENCIA ALTA',
                'Solicitud': '#3',
                'Estado': 'Flujo Completo',
                'Fecha': datetime.now().strftime("%d/%m/%Y %H:%M")
            }
        },
        'test_donation_validation': {
            'success': True,
            'duration': 25,
            'description': 'Validación de datos y requisitos para proceso de donación',
            'donation_data': {
                'Mascota Receptora': 'Rocky',
                'Veterinaria': 'Clínica Veterinaria Norte',
                'Urgencia': 'URGENCIA MEDIA',
                'Solicitud': '#4',
                'Estado': 'Validado',
                'Validaciones': '4/4 exitosas',
                'Fecha': datetime.now().strftime("%d/%m/%Y %H:%M")
            }
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
        print("   • Resumen general de pruebas de donación")
        print("   • Gráfico de torta con resultados (colores temáticos)")
        print("   • Gráfico de barras con duración por tipo de prueba")
        print("   • Detalle de cada prueba ejecutada")
        print("   • Datos de donaciones procesadas")
        print("   • Pie de página académico")
        print()
        print("🎨 Características visuales:")
        print("   • Esquema de colores rosa/rojo (temática donaciones)")
        print("   • Gráficos 3D con efectos profesionales")
        print("   • Tablas con filas alternadas")
        print("   • Tipografía institucional")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generando PDF de prueba: {e}")
        return False

if __name__ == "__main__":
    test_pdf_generation()
