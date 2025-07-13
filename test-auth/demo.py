#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo de las Pruebas de Autenticación de PetMatch
Universidad Nacional de Colombia

Este script ejecuta una demostración completa del sistema de pruebas.
"""

import os
import sys
from test_auth import PetMatchAuthTester

def main():
    print("=" * 60)
    print("🏛️  UNIVERSIDAD NACIONAL DE COLOMBIA")
    print("   Facultad de Ingeniería - Departamento de Sistemas")
    print("=" * 60)
    print("")
    print("📋 DEMO: Sistema de Pruebas Automatizadas PetMatch")
    print("🔐 Módulo: Autenticación y Registro")
    print("")
    print("Este demo ejecutará:")
    print("  ✅ 4 pruebas de autenticación completas")
    print("  📄 Generación de reportes PDF individuales")
    print("  📊 Reporte consolidado con gráficos")
    print("  🎯 Logo universitario y formato profesional")
    print("")
    
    # Verificar frontend
    print("🔍 Verificando configuración...")
    print("   • Frontend debe estar en: http://localhost:5173")
    print("   • Firefox debe estar instalado")
    print("   • Se generarán reportes en: ./reports/")
    print("")
    
    response = input("¿Desea continuar con la ejecución? [S/n]: ")
    if response.lower() in ['n', 'no']:
        print("Demo cancelado.")
        return
    
    print("\n🚀 Iniciando demo...")
    print("=" * 60)
    
    # Ejecutar las pruebas
    tester = PetMatchAuthTester()
    tester.run_all_tests()
    
    print("=" * 60)
    print("✅ Demo completado exitosamente!")
    print("")
    print("📁 Revisa la carpeta 'reports/' para ver los PDFs generados:")
    
    # Listar archivos generados
    reports_dir = os.path.join(os.path.dirname(__file__), "reports")
    if os.path.exists(reports_dir):
        files = os.listdir(reports_dir)
        pdf_files = [f for f in files if f.endswith('.pdf')]
        for pdf_file in sorted(pdf_files):
            print(f"   📄 {pdf_file}")
    
    print("")
    print("🎓 Universidad Nacional de Colombia")
    print("   Sistema de Pruebas Automatizadas")

if __name__ == "__main__":
    main()
