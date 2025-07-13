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

class PetMatchPDFGenerator:
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
        
        project_title = Paragraph("Sistema PetMatch - Pruebas de Autenticación", styles['Heading2'])
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
    
    def create_test_steps_table(self, test_steps, elements, styles):
        """Crea tabla con los pasos de la prueba"""
        title = Paragraph("Pasos de la Prueba Ejecutada", styles['Heading2'])
        elements.append(title)
        elements.append(Spacer(1, 10))
        
        # Encabezados
        data = [['Paso', 'Descripción', 'Estado']]
        
        # Agregar pasos
        for i, step in enumerate(test_steps, 1):
            data.append([str(i), step['description'], step['status']])
        
        table = Table(data, colWidths=[0.8*inch, 4*inch, 1.2*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 20))
    
    def create_pie_chart(self, test_results):
        """Crea gráfico de torta profesional con resultados y porcentajes"""
        drawing = Drawing(450, 250)
        
        pie = Pie()
        pie.x = 175
        pie.y = 75
        pie.width = 120
        pie.height = 120
        
        successful = sum(1 for result in test_results if result)
        failed = len(test_results) - successful
        total = len(test_results)
        
        if failed > 0:
            pie.data = [successful, failed]
            pie.labels = [f'{(successful/total)*100:.0f}%', f'{(failed/total)*100:.0f}%']
            # Colores más profesionales
            pie.slices[0].fillColor = colors.Color(0.2, 0.7, 0.3)  # Verde profesional
            pie.slices[1].fillColor = colors.Color(0.8, 0.2, 0.2)  # Rojo profesional
        else:
            pie.data = [successful]
            pie.labels = ['100%']
            pie.slices[0].fillColor = colors.Color(0.2, 0.7, 0.3)  # Verde profesional
        
        # Configurar etiquetas dentro del círculo con mejor estilo
        pie.slices.strokeWidth = 2
        pie.slices.strokeColor = colors.white
        pie.slices.labelRadius = 0.7
        pie.slices.fontSize = 16
        pie.slices.fontName = 'Helvetica-Bold'
        pie.slices.fontColor = colors.white
        
        # Agregar sombra (efecto 3D)
        pie.slices.popout = 5
        
        # Título del gráfico
        title = String(225, 220, 'Resultados de Pruebas', fontSize=14, fontName='Helvetica-Bold', textAnchor='middle')
        drawing.add(title)
        
        # Leyenda mejorada
        if failed > 0:
            # Cuadro verde
            legend_green = Rect(50, 180, 15, 15, fillColor=colors.Color(0.2, 0.7, 0.3), strokeColor=colors.black)
            legend_green_text = String(75, 185, f'Exitosas ({successful})', fontSize=10, fontName='Helvetica')
            drawing.add(legend_green)
            drawing.add(legend_green_text)
            
            # Cuadro rojo
            legend_red = Rect(50, 160, 15, 15, fillColor=colors.Color(0.8, 0.2, 0.2), strokeColor=colors.black)
            legend_red_text = String(75, 165, f'Fallidas ({failed})', fontSize=10, fontName='Helvetica')
            drawing.add(legend_red)
            drawing.add(legend_red_text)
        else:
            legend_green = Rect(50, 170, 15, 15, fillColor=colors.Color(0.2, 0.7, 0.3), strokeColor=colors.black)
            legend_green_text = String(75, 175, f'Todas Exitosas ({successful})', fontSize=10, fontName='Helvetica-Bold')
            drawing.add(legend_green)
            drawing.add(legend_green_text)
        
        drawing.add(pie)
        return drawing
    
    def create_bar_chart(self, test_names, test_durations):
        """Crea gráfico de barras profesional con duración de pruebas"""
        drawing = Drawing(500, 300)
        
        chart = VerticalBarChart()
        chart.x = 50
        chart.y = 80
        chart.height = 150
        chart.width = 400
        chart.data = [test_durations]
        chart.strokeColor = colors.black
        chart.valueAxis.valueMin = 0
        chart.valueAxis.valueMax = max(test_durations) * 1.3 if test_durations else 30
        
        # Configurar etiquetas del eje Y (tiempo) con mejor formato
        chart.valueAxis.labelTextFormat = '%d seg'
        chart.valueAxis.labels.fontName = 'Helvetica'
        chart.valueAxis.labels.fontSize = 9
        chart.valueAxis.strokeWidth = 1
        chart.valueAxis.strokeColor = colors.black
        
        # Líneas de cuadrícula
        chart.valueAxis.visibleGrid = 1
        chart.valueAxis.gridStrokeColor = colors.Color(0.8, 0.8, 0.8)
        chart.valueAxis.gridStrokeWidth = 0.5
        
        # Configurar etiquetas del eje X con mejor formato
        chart.categoryAxis.labels.boxAnchor = 'ne'
        chart.categoryAxis.labels.dx = 8
        chart.categoryAxis.labels.dy = -2
        chart.categoryAxis.labels.angle = 30
        chart.categoryAxis.labels.fontName = 'Helvetica'
        chart.categoryAxis.labels.fontSize = 8
        chart.categoryAxis.strokeWidth = 1
        chart.categoryAxis.strokeColor = colors.black
        
        # Nombres más legibles
        clean_names = []
        for name in test_names:
            clean_name = name.replace('test_', '').replace('_', ' ')
            if 'login usuario' in clean_name:
                clean_names.append('Login\nUsuario')
            elif 'login veterinaria' in clean_name:
                clean_names.append('Login\nVeterinaria') 
            elif 'register and login owner' in clean_name:
                clean_names.append('Registro\nDueño')
            elif 'register and login clinic' in clean_name:
                clean_names.append('Registro\nClínica')
            else:
                clean_names.append(clean_name.title())
        
        chart.categoryAxis.categoryNames = clean_names
        
        # Colores degradados profesionales para las barras
        bar_colors = [
            colors.Color(0.2, 0.4, 0.8),  # Azul profesional
            colors.Color(0.3, 0.6, 0.9),  # Azul claro
            colors.Color(0.1, 0.5, 0.7),  # Azul marino
            colors.Color(0.4, 0.7, 1.0)   # Azul cielo
        ]
        
        # Aplicar colores a las barras
        for i, duration in enumerate(test_durations):
            if i < len(bar_colors):
                chart.bars[(0,i)].fillColor = bar_colors[i]
            chart.bars[(0,i)].strokeColor = colors.Color(0.1, 0.1, 0.1)
            chart.bars[(0,i)].strokeWidth = 1
        
        # Título del gráfico
        title = String(250, 260, 'Duración de Pruebas por Tipo', fontSize=14, fontName='Helvetica-Bold', textAnchor='middle')
        drawing.add(title)
        
        # Valores en la parte superior de cada barra
        for i, duration in enumerate(test_durations):
            x_pos = chart.x + (i + 0.5) * (chart.width / len(test_durations))
            y_pos = chart.y + chart.height + 10
            value_text = String(x_pos, y_pos, f'{duration}s', fontSize=9, fontName='Helvetica-Bold', textAnchor='middle')
            drawing.add(value_text)
        
        drawing.add(chart)
        return drawing
    
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
    
    def generate_individual_test_report(self, test_name, test_result, test_data, output_dir):
        """Genera un PDF individual para una prueba específica"""
        # Crear nombre de archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reporte_{test_name}_{timestamp}.pdf"
        filepath = os.path.join(output_dir, filename)
        
        # Crear documento con márgenes optimizados
        doc = SimpleDocTemplate(filepath, pagesize=A4, rightMargin=60, leftMargin=60,
                              topMargin=60, bottomMargin=50)
        
        # Obtener estilos y crear estilos personalizados
        styles = getSampleStyleSheet()
        
        # Estilo personalizado para títulos principales
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=20,
            spaceAfter=25,
            alignment=TA_CENTER,
            textColor=colors.Color(0.2, 0.4, 0.8),
            fontName='Helvetica-Bold'
        )
        styles.add(title_style)
        
        # Estilo para subtítulos
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=colors.Color(0.3, 0.3, 0.3),
            fontName='Helvetica-Bold'
        )
        styles.add(subtitle_style)
        
        # Lista de elementos del documento
        elements = []
        
        # Crear contenido
        self.create_header(elements, styles)
        
        # Información de la prueba
        duration = test_data.get('duration', 25)  # Duración estimada
        self.create_test_info_table(test_name, test_result, duration, elements, styles)
        
        # Pasos de la prueba
        test_steps = test_data.get('steps', [])
        if test_steps:
            self.create_test_steps_table(test_steps, elements, styles)
        
        # Gráficos
        elements.append(Paragraph("Análisis Gráfico de Resultados", styles['Heading2']))
        elements.append(Spacer(1, 10))
        
        # Gráfico de resultado
        pie_chart = self.create_pie_chart([test_result])
        elements.append(pie_chart)
        
        elements.append(Spacer(1, 20))
        
        # Información adicional
        if test_data.get('user_data'):
            elements.append(Paragraph("Datos del Usuario/Clínica Procesados", styles['Heading2']))
            elements.append(Spacer(1, 10))
            
            user_info = test_data['user_data']
            user_table_data = [['Campo', 'Valor']]
            for key, value in user_info.items():
                user_table_data.append([key, str(value)])
            
            user_table = Table(user_table_data, colWidths=[2*inch, 3*inch])
            user_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 11),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 1), (-1, -1), 9),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))
            
            elements.append(user_table)
        
        # Pie de página
        self.create_footer(elements, styles)
        
        # Generar PDF
        doc.build(elements)
        
        return filepath
    
    def generate_summary_report(self, all_test_results, output_dir):
        """Genera un reporte resumen de todas las pruebas"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reporte_resumen_autenticacion_{timestamp}.pdf"
        filepath = os.path.join(output_dir, filename)
        
        doc = SimpleDocTemplate(filepath, pagesize=A4, rightMargin=72, leftMargin=72,
                              topMargin=72, bottomMargin=18)
        
        styles = getSampleStyleSheet()
        elements = []
        
        # Header
        self.create_header(elements, styles)
        
        # Resumen general
        total_tests = len(all_test_results)
        successful_tests = sum(1 for result in all_test_results.values() if result['success'])
        
        summary_data = [
            ['Resumen General', ''],
            ['Total de Pruebas:', str(total_tests)],
            ['Pruebas Exitosas:', str(successful_tests)],
            ['Pruebas Fallidas:', str(total_tests - successful_tests)],
            ['Porcentaje de Éxito:', f'{(successful_tests/total_tests)*100:.1f}%'],
            ['Tiempo Total Estimado:', f'{sum(r["duration"] for r in all_test_results.values())}s']
        ]
        
        summary_table = Table(summary_data, colWidths=[3.5*inch, 2.5*inch])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.2, 0.4, 0.8)),  # Azul profesional
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 13),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 15),
            ('TOPPADDING', (0, 0), (-1, 0), 15),
            ('BACKGROUND', (0, 1), (-1, -1), colors.Color(0.95, 0.97, 1.0)),  # Azul muy claro
            ('GRID', (0, 0), (-1, -1), 1.5, colors.Color(0.2, 0.4, 0.8)),
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 1), (-1, -1), 11),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 10),
        ]))
        
        elements.append(summary_table)
        elements.append(Spacer(1, 30))
        
        # Gráficos
        elements.append(Spacer(1, 20))
        title_graphics = Paragraph("Análisis Gráfico Consolidado", styles['Heading2'])
        title_graphics.alignment = TA_CENTER
        elements.append(title_graphics)
        elements.append(Spacer(1, 10))
        
        # Gráfico de torta
        pie_chart = self.create_pie_chart([r['success'] for r in all_test_results.values()])
        elements.append(pie_chart)
        
        elements.append(Spacer(1, 20))
        
        # Gráfico de barras
        test_names = list(all_test_results.keys())
        test_durations = [all_test_results[name]['duration'] for name in test_names]
        bar_chart = self.create_bar_chart(test_names, test_durations)
        elements.append(bar_chart)
        
        # Detalles por prueba
        elements.append(PageBreak())
        title_detail = Paragraph("Detalle de Pruebas Ejecutadas", styles['Heading2'])
        title_detail.alignment = TA_CENTER
        elements.append(title_detail)
        elements.append(Spacer(1, 10))
        
        detail_data = [['Prueba', 'Estado', 'Duración', 'Descripción']]
        for test_name, result in all_test_results.items():
            status = '✅ EXITOSO' if result['success'] else '❌ FALLIDO'
            description = result.get('description', 'Prueba de autenticación')
            
            # Nombres más legibles
            display_name = test_name.replace('test_', '').replace('_', ' ')
            if 'login usuario' in display_name:
                display_name = 'Login Usuario'
            elif 'login veterinaria' in display_name:
                display_name = 'Login Veterinaria'
            elif 'register and login owner' in display_name:
                display_name = 'Registro Dueño'
            elif 'register and login clinic' in display_name:
                display_name = 'Registro Clínica'
            else:
                display_name = display_name.title()
            
            detail_data.append([
                display_name,
                status,
                f"{result['duration']}s",
                description
            ])
        
        detail_table = Table(detail_data, colWidths=[1.8*inch, 1.2*inch, 0.8*inch, 3.2*inch])
        detail_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.2, 0.4, 0.8)),  # Azul profesional
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 15),
            ('TOPPADDING', (0, 0), (-1, 0), 15),
            # Filas alternadas
            ('BACKGROUND', (0, 1), (-1, 1), colors.Color(0.95, 0.97, 1.0)),
            ('BACKGROUND', (0, 2), (-1, 2), colors.white),
            ('BACKGROUND', (0, 3), (-1, 3), colors.Color(0.95, 0.97, 1.0)),
            ('BACKGROUND', (0, 4), (-1, 4), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.Color(0.2, 0.4, 0.8)),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (3, 1), (3, -1), 'LEFT'),  # Descripción alineada a la izquierda
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ]))
        
        elements.append(detail_table)
        
        # Footer
        self.create_footer(elements, styles)
        
        doc.build(elements)
        return filepath
