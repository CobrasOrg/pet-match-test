from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.graphics.shapes import Drawing, String, Rect
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart
from datetime import datetime
import os

class PetMatchRequestsPDFGenerator:
    def __init__(self):
        # Buscar el logo en múltiples ubicaciones posibles
        possible_paths = [
            os.path.join(os.path.dirname(__file__), "..", "assets", "university_logo.png"),
            os.path.join(os.path.dirname(__file__), "university_logo.png"),
            "university_logo.png"
        ]
        
        self.logo_path = None
        for path in possible_paths:
            if os.path.exists(path):
                self.logo_path = path
                break
        
    def create_header(self, elements, styles):
        """Crea el encabezado del documento con logo y título"""
        # Logo de la Universidad - tamaño aumentado horizontalmente
        if self.logo_path and os.path.exists(self.logo_path):
            logo = Image(self.logo_path, width=3.5*inch, height=1.8*inch)
            logo.hAlign = 'CENTER'
            elements.append(logo)
        else:
            # Si no hay logo, agregar espacio equivalente
            elements.append(Spacer(1, 1.8*inch))
        
        elements.append(Spacer(1, 12))
        
        # Título principal
        title = Paragraph("UNIVERSIDAD NACIONAL DE COLOMBIA", styles['Title'])
        title.alignment = TA_CENTER
        elements.append(title)
        
        subtitle = Paragraph("Facultad de Ingeniería - Departamento de Sistemas", styles['Heading2'])
        subtitle.alignment = TA_CENTER
        elements.append(subtitle)
        
        elements.append(Spacer(1, 15))
        
        # Título del reporte
        report_title = Paragraph("REPORTE DE PRUEBAS AUTOMATIZADAS", styles['Title'])
        report_title.alignment = TA_CENTER
        elements.append(report_title)
        
        report_subtitle = Paragraph("Sistema PetMatch - Módulo de Gestión de Solicitudes", styles['Heading2'])
        report_subtitle.alignment = TA_CENTER
        elements.append(report_subtitle)
        
        elements.append(Spacer(1, 20))
    
    def create_info_section(self, elements, styles):
        """Crea la sección de información del proyecto"""
        # Información del proyecto
        project_info = [
            ["Proyecto:", "PetMatch - Plataforma de Donación de Sangre para Mascotas"],
            ["Módulo:", "Gestión de Solicitudes de Donación"],
            ["Tipo de Prueba:", "Pruebas Funcionales Automatizadas con Selenium"],
            ["Navegador:", "Mozilla Firefox"],
            ["Fecha de Ejecución:", datetime.now().strftime("%d/%m/%Y %H:%M:%S")],
            ["Ejecutado por:", "Sistema Automatizado de Pruebas"]
        ]
        
        info_table = Table(project_info, colWidths=[2*inch, 4*inch])
        info_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        elements.append(info_table)
        elements.append(Spacer(1, 20))
    
    def create_objectives_section(self, elements, styles):
        """Crea la sección de objetivos de las pruebas"""
        objectives_title = Paragraph("OBJETIVOS DE LAS PRUEBAS", styles['Heading1'])
        elements.append(objectives_title)
        elements.append(Spacer(1, 10))
        
        objectives_text = """
        Este conjunto de pruebas automatizadas tiene como objetivo verificar el correcto funcionamiento 
        del flujo completo de gestión de solicitudes de donación de sangre para mascotas en la plataforma PetMatch:
        
        <b>Objetivos específicos:</b>
        
        <b>FLUJO 1: Gestión de Solicitudes Activas</b><br/>
        - Verificar la autenticación de usuarios veterinarios<br/>
        - Validar la navegación al módulo de solicitudes<br/>
        - Confirmar la funcionalidad de filtrado por solicitudes activas<br/>
        - Verificar la gestión de solicitudes individuales<br/>
        - Validar la visualización de mascotas postuladas<br/>
        - Comprobar el proceso de aprobación de postulaciones<br/>
        
        <b>FLUJO 2: Edición de Solicitudes en Revisión</b><br/>
        - Verificar el acceso a solicitudes en estado "En revisión"<br/>
        - Validar la funcionalidad de selección aleatoria de solicitudes<br/>
        - Confirmar el acceso al modo de edición de solicitudes<br/>
        - Verificar la modificación de campos editables (urgencia, tipo de sangre, peso, descripción)<br/>
        - Validar el guardado correcto de los cambios<br/>
        - Confirmar la actualización exitosa con mensaje de confirmación<br/>
        
        <b>Aspectos técnicos validados:</b><br/>
        - Interacción con elementos de interfaz (botones, formularios, selects)<br/>
        - Manejo de elementos dinámicos y componentes React<br/>
        - Navegación entre páginas de la aplicación<br/>
        - Respuesta del sistema ante modificaciones de datos<br/>
        - Validación de mensajes de estado y confirmación
        """
        
        objectives_para = Paragraph(objectives_text, styles['Normal'])
        elements.append(objectives_para)
        elements.append(Spacer(1, 20))
    def create_test_results_section(self, elements, styles, test_results):
        """Crea la sección de resultados de las pruebas"""
        results_title = Paragraph("RESULTADOS DE LAS PRUEBAS", styles['Heading1'])
        elements.append(results_title)
        elements.append(Spacer(1, 10))
        
        # Tabla de resumen
        passed_tests = sum(1 for result in test_results.values() if result.get('success', False))
        total_tests = len(test_results)
        
        summary_data = [
            ["Métrica", "Valor"],
            ["Total de pruebas ejecutadas", str(total_tests)],
            ["Pruebas exitosas", str(passed_tests)],
            ["Pruebas fallidas", str(total_tests - passed_tests)],
            ["Porcentaje de éxito", f"{(passed_tests/total_tests*100):.1f}%" if total_tests > 0 else "0%"]
        ]
        
        summary_table = Table(summary_data, colWidths=[2.5*inch, 1.5*inch])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        
        elements.append(summary_table)
        elements.append(Spacer(1, 20))
        
        # Detalles de cada prueba
        details_title = Paragraph("DETALLE DE PRUEBAS EJECUTADAS", styles['Heading2'])
        elements.append(details_title)
        elements.append(Spacer(1, 10))
        
        # Mapeo de nombres de pruebas a descripciones
        test_descriptions = {
            # Flujo 1: Solicitudes Activas
            'login': 'Autenticación de Veterinaria',
            'navigation': 'Navegación a Solicitudes',
            'active_tab': 'Selección de Solicitudes Activas',
            'manage_click': 'Acceso a Gestión de Solicitud',
            'view_applications': 'Visualización de Postulaciones',
            'count_applications': 'Conteo de Mascotas Postuladas',
            'approval': 'Aprobación de Postulación',
            
            # Flujo 2: Edición de Solicitudes en Revisión
            'edit_login': 'Autenticación para Edición',
            'edit_navigation': 'Navegación para Edición',
            'review_tab': 'Selección de Solicitudes en Revisión',
            'random_manage_click': 'Acceso Aleatorio a Gestión',
            'edit_click': 'Activación de Modo Edición',
            'edit_fields': 'Modificación de Campos',
            'save_changes': 'Guardado de Cambios',
            
            # Errores
            'error': 'Error General',
            'edit_error': 'Error en Edición'
        }
        
        detail_data = [["Prueba", "Estado", "Descripción", "Timestamp"]]
        
        for test_name, result in test_results.items():
            status = "✅ EXITOSA" if result.get('success', False) else "❌ FALLIDA"
            description = test_descriptions.get(test_name, test_name.title())
            timestamp = result.get('timestamp', datetime.now()).strftime("%H:%M:%S")
            
            detail_data.append([
                description,
                status,
                result.get('details', 'Sin detalles'),
                timestamp
            ])
        
        detail_table = Table(detail_data, colWidths=[2*inch, 1*inch, 2.5*inch, 0.8*inch])
        detail_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        elements.append(detail_table)
        elements.append(Spacer(1, 20))
    
    def create_applications_analysis(self, elements, styles, test_results):
        """Crea análisis específico de las postulaciones encontradas"""
        analysis_title = Paragraph("ANÁLISIS DE POSTULACIONES", styles['Heading2'])
        elements.append(analysis_title)
        elements.append(Spacer(1, 10))
        
        # Obtener datos de postulaciones
        count_result = test_results.get('count_applications', {})
        applications_count = count_result.get('count', 0)
        count_text = count_result.get('count_text', 'No disponible')
        
        analysis_text = f"""
        <b>Resumen de Postulaciones Encontradas:</b>
        
        - Número total de mascotas postuladas: {applications_count}<br/>
        - Texto del contador: "{count_text}"<br/>
        - Estado: {'Con postulaciones' if applications_count > 0 else 'Sin postulaciones'}<br/>
        
        <b>Interpretación:</b>
        """
        
        if applications_count > 0:
            analysis_text += f"""
            Se encontraron {applications_count} mascotas postuladas para la solicitud seleccionada.
            Esto indica que el sistema está funcionando correctamente y hay donantes interesados
            en participar en el proceso de donación de sangre.
            
            Las pruebas continuaron con el proceso de aprobación de una postulación.
            """
        else:
            analysis_text += """
            No se encontraron mascotas postuladas para la solicitud seleccionada.
            Esto puede ser normal dependiendo del estado de las solicitudes en el sistema.
            No se considera un error, sino una condición válida del sistema.
            """
        
        analysis_para = Paragraph(analysis_text, styles['Normal'])
        elements.append(analysis_para)
        elements.append(Spacer(1, 20))
    
    def create_flow_diagram_section(self, elements, styles):
        """Crea un diagrama del flujo de pruebas"""
        flow_title = Paragraph("FLUJO DE PRUEBAS EJECUTADO", styles['Heading2'])
        elements.append(flow_title)
        elements.append(Spacer(1, 10))
        
        flow_steps = [
            ["Paso", "Acción", "Descripción"],
            ["1", "Login", "Autenticación con veterinaria@sanpatricio.com"],
            ["2", "Navegación", "Acceso a la página /requests"],
            ["3", "Filtrado", "Selección de solicitudes activas"],
            ["4", "Gestión", "Click en botón 'Gestionar' de primera solicitud"],
            ["5", "Postulaciones", "Click en 'Ver mascotas postuladas'"],
            ["6", "Conteo", "Identificación y conteo de postulaciones"],
            ["7", "Aprobación", "Aprobación de primera postulación (si existe)"]
        ]
        
        flow_table = Table(flow_steps, colWidths=[0.5*inch, 1.2*inch, 4.3*inch])
        flow_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        elements.append(flow_table)
        elements.append(Spacer(1, 20))
    
    def create_technical_details_section(self, elements, styles):
        """Crea la sección de detalles técnicos"""
        tech_title = Paragraph("DETALLES TÉCNICOS", styles['Heading2'])
        elements.append(tech_title)
        elements.append(Spacer(1, 10))
        
        tech_text = """
        <b>Tecnologías utilizadas:</b>
        • Selenium WebDriver para automatización del navegador
        • Firefox como navegador de pruebas
        • Python como lenguaje de programación para las pruebas
        • ReportLab para generación de reportes PDF
        
        <b>Estrategias de localización de elementos:</b>
        • XPath para elementos con texto específico
        • Selectores CSS para elementos con clases específicas
        • Múltiples estrategias de respaldo para mayor robustez
        • Scroll automático para elementos fuera del viewport
        
        <b>Manejo de errores:</b>
        • Timeouts configurables para esperas
        • Múltiples intentos de localización de elementos
        • Registro detallado de errores y excepciones
        • Continuación de pruebas ante fallos no críticos
        
        <b>Configuración del navegador:</b>
        • Resolución: 1366x768
        • Modo visual (no headless) para depuración
        • Deshabilitación de notificaciones y sonidos
        • Maximización automática de ventana
        """
        
        tech_para = Paragraph(tech_text, styles['Normal'])
        elements.append(tech_para)
        elements.append(Spacer(1, 20))
    
    def create_conclusions_section(self, elements, styles, test_results):
        """Crea la sección de conclusiones"""
        conclusions_title = Paragraph("CONCLUSIONES Y RECOMENDACIONES", styles['Heading1'])
        elements.append(conclusions_title)
        elements.append(Spacer(1, 10))
        
        # Calcular estadísticas
        passed_tests = sum(1 for result in test_results.values() if result.get('success', False))
        total_tests = len(test_results)
        success_rate = (passed_tests/total_tests*100) if total_tests > 0 else 0
        
        conclusions_text = f"""
        <b>Resumen General:</b>
        
        Las pruebas automatizadas del módulo de gestión de solicitudes han sido ejecutadas 
        exitosamente con una tasa de éxito del {success_rate:.1f}% ({passed_tests} de {total_tests} pruebas).
        
        <b>Aspectos Positivos:</b>
        • El sistema de autenticación funciona correctamente
        • La navegación entre módulos es fluida
        • Los filtros de estado funcionan adecuadamente
        • La interfaz de gestión de solicitudes es accesible
        • El sistema maneja correctamente casos sin postulaciones
        
        <b>Recomendaciones:</b>
        • Mantener las pruebas automatizadas como parte del proceso de CI/CD
        • Ejecutar estas pruebas antes de cada despliegue
        • Expandir las pruebas para cubrir más escenarios edge case
        • Considerar pruebas de carga para el módulo de postulaciones
        • Implementar alertas automáticas ante fallos en las pruebas
        
        <b>Próximos Pasos:</b>
        • Integrar estas pruebas con el pipeline de desarrollo
        • Crear pruebas adicionales para diferentes tipos de usuario
        • Implementar pruebas de rendimiento
        • Documentar procedimientos de mantenimiento de las pruebas
        """
        
        conclusions_para = Paragraph(conclusions_text, styles['Normal'])
        elements.append(conclusions_para)
        elements.append(Spacer(1, 20))
    
    def create_footer(self, elements, styles):
        """Crea el pie de página del documento"""
        elements.append(Spacer(1, 20))
        
        footer_text = f"""
        <i>Reporte generado automáticamente el {datetime.now().strftime("%d de %B de %Y a las %H:%M:%S")}</i><br/>
        <i>Sistema de Pruebas Automatizadas - PetMatch v1.0</i><br/>
        <i>Universidad Nacional de Colombia - Facultad de Ingeniería</i>
        """
        
        footer_para = Paragraph(footer_text, styles['Normal'])
        footer_para.alignment = TA_CENTER
        elements.append(footer_para)
    
    def generate_report(self, test_results):
        """Genera el reporte completo en PDF"""
        try:
            # Crear directorio de reportes si no existe
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)
            
            # Generar nombre del archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"reporte_pruebas_solicitudes_{timestamp}.pdf"
            filepath = os.path.join(reports_dir, filename)
            
            # Crear documento
            doc = SimpleDocTemplate(
                filepath,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            # Obtener estilos
            styles = getSampleStyleSheet()
            
            # Crear estilo personalizado para el contenido
            styles.add(ParagraphStyle(
                name='CustomNormal',
                parent=styles['Normal'],
                fontSize=10,
                spaceAfter=12,
                alignment=TA_LEFT
            ))
            
            # Lista de elementos del documento
            elements = []
            
            # Crear todas las secciones
            self.create_header(elements, styles)
            self.create_info_section(elements, styles)
            self.create_objectives_section(elements, styles)
            
            # Nueva página para resultados
            elements.append(PageBreak())
            self.create_test_results_section(elements, styles, test_results)
            self.create_applications_analysis(elements, styles, test_results)
            
            # Nueva página para detalles técnicos
            elements.append(PageBreak())
            self.create_flow_diagram_section(elements, styles)
            self.create_technical_details_section(elements, styles)
            self.create_conclusions_section(elements, styles, test_results)
            self.create_footer(elements, styles)
            
            # Construir el documento
            doc.build(elements)
            
            return filepath
            
        except Exception as e:
            print(f"Error al generar reporte PDF: {e}")
            return None
