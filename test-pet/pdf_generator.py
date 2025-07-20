from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from datetime import datetime
import os

class PetMatchPDFGenerator:
    def __init__(self):
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
        
        subtitle = Paragraph("Facultad de Ingeniería - Ingeniería de Sistemas y Computación ", styles['Heading2'])
        subtitle.alignment = TA_CENTER
        elements.append(subtitle)
        
        elements.append(Spacer(1, 15))
        
        # Información académica
        academic_info = Paragraph("""
        <para align="center">
        <b>Materia:</b> Ingeniería de Software 2<br/>
        <b>Grupo:</b> Cobras<br/>
        <b>Proyecto:</b> Pet-Match
        </para>
        """, styles['Normal'])
        elements.append(academic_info)
        
        elements.append(Spacer(1, 20))
        
        # Título del reporte
        report_title = Paragraph("REPORTE DE PRUEBAS AUTOMATIZADAS", styles['Heading1'])
        report_title.alignment = TA_CENTER
        elements.append(report_title)
        
        project_title = Paragraph("Sistema PetMatch - Pruebas de Mascotas", styles['Heading2'])
        project_title.alignment = TA_CENTER
        elements.append(project_title)
        
        elements.append(Spacer(1, 30))

    def create_test_info_table(self, test_name, test_result, test_duration, elements, styles):
        """Crea tabla con información general de la prueba"""
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        data = [
            ['Información General de la Prueba', ''],
            ['Nombre de la Prueba:', test_name],
            ['Resultado:', '✅ EXITOSO' if test_result else '❌ FALLIDO'],
            ['Duración Estimada:', f'{test_duration}s'],
            ['Fecha y Hora:', current_time],
            ['Sistema Bajo Prueba:', 'PetMatch Frontend (React)'],
            ['URL Base:', 'http://localhost:5173'],
            ['Navegador:', 'Firefox con Selenium WebDriver'],
            ['Responsable:', 'Sistema de Pruebas Automatizadas']
        ]
        
        table = Table(data, colWidths=[3*inch, 3*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 20))

    def generate_summary_report(self, all_test_results, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reporte_resumen_mascotas_{timestamp}.pdf"
        filepath = os.path.join(output_dir, filename)
        doc = SimpleDocTemplate(filepath, pagesize=A4, rightMargin=72, leftMargin=72,
                              topMargin=72, bottomMargin=18)
        styles = getSampleStyleSheet()
        elements = []
        self.create_header(elements, styles)
        
        # Agregar descripción del flujo de prueba
        self.add_test_flow_description(elements, styles)
        
        for test_name, result in all_test_results.items():
            self.create_test_info_table(test_name, result['success'], result['duration'], elements, styles)
            elements.append(Paragraph(result['description'], styles['Normal']))
            elements.append(PageBreak())
        doc.build(elements)
        return filepath

    def add_test_flow_description(self, elements, styles):
        """Agrega descripción paso a paso del flujo de prueba"""
        title = Paragraph("Descripción del Flujo de Prueba", styles['Heading2'])
        title.alignment = TA_CENTER
        elements.append(title)
        elements.append(Spacer(1, 10))
        
        flow_description = """
        <para align="justify">
        <b>Prueba de Registro de Mascota - Flujo Completo End-to-End</b><br/><br/>
        
        La prueba automatizada ejecuta los siguientes pasos secuenciales:<br/><br/>
        
        <b>1. Autenticación:</b> Login en el sistema usando credenciales de usuario dueño de mascota (mcastiblancoa@unal.edu.co).<br/><br/>
        
        <b>2. Navegación:</b> Apertura del menú de perfil y navegación a la sección "Mis Mascotas".<br/><br/>
        
        <b>3. Acceso al Formulario:</b> Click en el botón "Registrar Mascota" para abrir el formulario de registro.<br/><br/>
        
        <b>4. Completar Información Básica:</b><br/>
        • Nombre de la mascota: "TestPet"<br/>
        • Especie: Perro (canine)<br/>
        • Raza: Mestizo<br/>
        • Edad: 3 años<br/>
        • Peso: 30 kg<br/><br/>
        
        <b>5. Completar Información Médica:</b><br/>
        • Tipo de sangre: DEA 1.1+<br/>
        • Fecha de última vacunación: 01/07/2025<br/>
        • Estado de salud: Descripción detallada del estado actual<br/><br/>
        
        <b>6. Envío y Confirmación:</b> Envío del formulario y manejo de la respuesta del sistema.<br/><br/>
        
        <b>Validación:</b> La prueba verifica que todos los campos obligatorios sean completados correctamente y que el sistema procese la información sin errores.
        </para>
        """
        
        flow_paragraph = Paragraph(flow_description, styles['Normal'])
        elements.append(flow_paragraph)
        elements.append(Spacer(1, 20))
    
    def create_footer(self, elements, styles):
        """Crea el pie de página con información académica"""
        elements.append(Spacer(1, 30))
        
        footer_text = """
        <para align="center">
        <b>Universidad Nacional de Colombia</b><br/>
        Facultad de Ingeniería - Departamento de Sistemas<br/>
        <b>Materia:</b> Ingeniería de Software 2 | <b>Grupo:</b> Cobras | <b>Proyecto:</b> Pet-Match<br/>
        Sistema de Pruebas Automatizadas<br/>
        Generado automáticamente el """ + datetime.now().strftime("%d de %B de %Y a las %H:%M") + """
        </para>
        """
        
        footer = Paragraph(footer_text, styles['Normal'])
        elements.append(footer)
