from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, Image as RLImage,
                                 BaseDocTemplate, Frame, PageTemplate, FrameBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
import os

# Colors
BLUE_DARK = colors.HexColor('#2E5F8A')
BLUE_MID = colors.HexColor('#4A7FA5')
BLUE_LIGHT = colors.HexColor('#D6E8F5')
BLUE_SIDEBAR = colors.HexColor('#5B8DB8')
BLUE_SIDEBAR_ACCENT = colors.HexColor('#7AAED0')
GRAY_DARK = colors.HexColor('#333333')
GRAY_MED = colors.HexColor('#666666')
GRAY_LIGHT = colors.HexColor('#AAAAAA')
WHITE = colors.white

PAGE_W, PAGE_H = A4  # 210 x 297 mm

LEFT_COL_W = 65 * mm
RIGHT_COL_W = PAGE_W - LEFT_COL_W - 20 * mm  # margins
MARGIN = 10 * mm

# ── Styles ────────────────────────────────────────────────────────────────────

def make_styles():
    base = getSampleStyleSheet()

    name = ParagraphStyle('Name', fontName='Helvetica-Bold', fontSize=22,
                          textColor=BLUE_DARK, alignment=TA_CENTER, leading=26)
    role = ParagraphStyle('Role', fontName='Helvetica', fontSize=10,
                          textColor=GRAY_MED, alignment=TA_CENTER, leading=14)
    section_title = ParagraphStyle('SectionTitle', fontName='Helvetica-Bold',
                                   fontSize=11, textColor=BLUE_DARK,
                                   spaceBefore=6, spaceAfter=2)
    left_section = ParagraphStyle('LeftSection', fontName='Helvetica-Bold',
                                  fontSize=10, textColor=BLUE_DARK,
                                  spaceBefore=8, spaceAfter=2)
    body = ParagraphStyle('Body', fontName='Helvetica', fontSize=8,
                          textColor=GRAY_DARK, leading=12, alignment=TA_JUSTIFY)
    body_left = ParagraphStyle('BodyLeft', fontName='Helvetica', fontSize=8,
                               textColor=GRAY_DARK, leading=12)
    skill_item = ParagraphStyle('SkillItem', fontName='Helvetica', fontSize=8,
                                textColor=GRAY_DARK, leading=11)
    contact = ParagraphStyle('Contact', fontName='Helvetica', fontSize=8,
                             textColor=GRAY_DARK, leading=14)
    job_company = ParagraphStyle('JobCompany', fontName='Helvetica-Bold',
                                 fontSize=9, textColor=GRAY_DARK, leading=12)
    job_title = ParagraphStyle('JobTitle', fontName='Helvetica-Oblique',
                               fontSize=8.5, textColor=BLUE_MID, leading=11)
    job_tech = ParagraphStyle('JobTech', fontName='Helvetica', fontSize=7.5,
                              textColor=GRAY_MED, leading=11, alignment=TA_JUSTIFY)
    bullet = ParagraphStyle('Bullet', fontName='Helvetica', fontSize=8,
                            textColor=GRAY_DARK, leading=11,
                            leftIndent=10, firstLineIndent=-6)
    edu_title = ParagraphStyle('EduTitle', fontName='Helvetica-Bold', fontSize=8.5,
                               textColor=GRAY_DARK, leading=12)
    edu_sub = ParagraphStyle('EduSub', fontName='Helvetica-Oblique', fontSize=8,
                             textColor=GRAY_MED, leading=11)
    course = ParagraphStyle('Course', fontName='Helvetica', fontSize=8,
                            textColor=GRAY_DARK, leading=13)
    return dict(name=name, role=role, section_title=section_title,
                left_section=left_section, body=body, body_left=body_left,
                skill_item=skill_item, contact=contact,
                job_company=job_company, job_title=job_title,
                job_tech=job_tech, bullet=bullet,
                edu_title=edu_title, edu_sub=edu_sub, course=course)

S = make_styles()

def hr(col=BLUE_LIGHT, w=1):
    return HRFlowable(width='100%', thickness=w, color=col, spaceAfter=4, spaceBefore=2)

def dot_bullet(text, style):
    return Paragraph(f'• {text}', style)


# ── Left column ───────────────────────────────────────────────────────────────

def build_left():
    items = []

    # Photo
    items.append(Spacer(1, 8*mm))
    foto = RLImage(os.path.join(os.path.dirname(__file__), 'foto.png'), width=38*mm, height=38*mm)
    foto.hAlign = 'CENTER'
    items.append(foto)
    items.append(Spacer(1, 4))

    # Name & role
    items.append(Paragraph('Javier', S['name']))
    items.append(Paragraph('Polo', S['name']))
    items.append(Spacer(1, 2))
    items.append(Paragraph('Backend Developer', S['role']))
    items.append(Spacer(1, 8))

    # Contact
    items.append(hr())
    items.append(Paragraph('✆  Contacto', S['left_section']))
    items.append(hr())
    items.append(Spacer(1, 4))
    for line in [
        '📞  +34 689 850 370',
        '✉  javier.polgar@gmail.com',
        '📍  Ávila',
        '🔗  linkedin.com/in/javier-garro-045084177',
    ]:
        items.append(Paragraph(line, S['contact']))

    # Sobre mí
    items.append(Spacer(1, 8))
    items.append(hr())
    items.append(Paragraph('👤  Sobre mi', S['left_section']))
    items.append(hr())
    items.append(Spacer(1, 4))
    sobre = (
        'Desarrollador Back-End con más de 5 años de experiencia en microservicios, '
        'arquitecturas limpias y entornos de alta disponibilidad en sectores como banca '
        'y retail. Sólido conocimiento en DDD, arquitectura hexagonal y patrones avanzados '
        'de diseño. Experiencia creciente en el uso de herramientas de Inteligencia Artificial '
        'y automatización aplicadas al desarrollo de software.'
    )
    items.append(Paragraph(sobre, S['body']))

    # Skills por bloques
    items.append(Spacer(1, 8))
    items.append(hr())
    items.append(Paragraph('⚙  Skills', S['left_section']))
    items.append(hr())
    items.append(Spacer(1, 3))

    skill_block_label = ParagraphStyle('SkillBlockLabel', fontName='Helvetica-Bold',
                                       fontSize=7.5, textColor=BLUE_DARK, leading=12, spaceBefore=4)

    skill_blocks = [
        ('Backend', ['Java', 'Kotlin', 'Spring Boot', 'Microservicios', 'REST API', 'OAuth2.0']),
        ('Arquitectura', ['DDD', 'Arq. Hexagonal', 'Clean Code', 'CQS', 'Event Driven']),
        ('DevOps / Infra', ['Docker', 'CI/CD', 'AWS', 'Kafka', 'Sonar', 'Git', 'Grafana']),
        ('Testing', ['JUnit', 'Mockito', 'TestContainers', 'Karate', 'TDD / BDD']),
        ('IA / Automatización', ['MCP', 'Spec-Driven Development', 'Claude Code', 'n8n', 'SpecKit']),
        ('Herramientas', ['Postman', 'SoapUI', 'IntelliJ IDEA', 'Jira', 'Agile/Scrum']),
        ('Idiomas', ['Español (nativo)', 'Inglés (B2)']),
    ]

    for block_name, skills in skill_blocks:
        items.append(Paragraph(block_name, skill_block_label))
        skills_text = '  '.join([f'• {s}' for s in skills])
        items.append(Paragraph(skills_text, S['skill_item']))

    return items


# ── Right column ──────────────────────────────────────────────────────────────

def build_right():
    items = []
    items.append(Spacer(1, 0))

    # ── Educación ──────────────────────────────────────────────────
    items.append(Paragraph('🎓  Educación', S['section_title']))
    items.append(hr(BLUE_LIGHT, 0.8))

    edu = [
        ('Desarrollo de aplicaciones multiplataforma',
         'I.E.S. Alonso de Madrigal (Ávila)', '2019 - 2021'),
        ('Conservatorio Superior de Música',
         'C.M.S. Rafael Orozco (Córdoba)', '2014 - 2018'),
    ]
    for title, sub, dates in edu:
        row = Table([[
            Paragraph(f'● {title}', S['edu_title']),
            Paragraph(dates, ParagraphStyle('DateR', fontName='Helvetica',
                                            fontSize=8, textColor=GRAY_MED,
                                            alignment=TA_RIGHT))
        ]], colWidths=[RIGHT_COL_W*0.72, RIGHT_COL_W*0.28])
        row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                 ('LEFTPADDING',(0,0),(-1,-1),0),
                                 ('RIGHTPADDING',(0,0),(-1,-1),0),
                                 ('TOPPADDING',(0,0),(-1,-1),2),
                                 ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
        items.append(row)
        items.append(Paragraph(f'     {sub}', S['edu_sub']))
        items.append(Spacer(1, 3))

    # ── Experiencia ────────────────────────────────────────────────
    items.append(Spacer(1, 6))
    items.append(Paragraph('💼  Experiencia', S['section_title']))
    items.append(hr(BLUE_LIGHT, 0.8))

    jobs = [
        {
            'company': 'SNGULAR (Inditex)',
            'title': 'Back-end Developer',
            'dates': 'feb. 2025 - jun. 2026',
            'tech': 'Spring Boot 3.4, Java 21, OpenAPI, REST, API Gateway, Kafka, Avro, Schema Registry, Postgres, Redis, Github Actions CI/CD, JUnit, Mockito, TestContainers, Karate, Sonar, Grafana, MCP, SpecKit, Scrum.',
            'bullets': [
                'Microservicios con Domain Driven Design, Arquitectura Hexagonal y Event Driven Design.',
                'Implementación de patrones CQS (Command Query Separation) en servicios de alta disponibilidad.',
                'Testing avanzado con TDD, BDD, TestContainers y Karate para pruebas de integración.',
                'Generación y validación de especificaciones técnicas mediante SpecKit integrado con Claude Code, agilizando el ciclo de diseño de contratos API.',
                'Monitorización y observabilidad con Grafana en entorno remoto.',
            ]
        },
        {
            'company': 'Kepps/Worldline (Sabadell)',
            'title': 'Mid Backend Developer',
            'dates': 'dic. 2022 - feb. 2025',
            'tech': 'Java 8, 11 y 21, Spring Boot, Microservicios, PostgreSQL, Docker, JUnit, Mockito, Sonar, CI/CD, metodologías ágiles, Rest API, AWS.',
            'bullets': [
                'Desarrollo y mantenimiento de microservicio nuevo desde 0.',
                'Despliegue y monitorización de aplicaciones en entornos de producción, asegurando rendimiento óptimo.',
                'Optimización del código según los estándares de Clean Code y cobertura del 100% en pruebas unitarias.',
            ]
        },
        {
            'company': 'NTTData (Iberia)',
            'title': 'Jr Backend Developer',
            'dates': 'feb. 2022 - dic. 2022',
            'tech': 'Java 11 y 13, Spring Boot, Microservicios, Rest API, Oracle, Docker, JUnit, Mockito, Sonar, CI/CD, metodologías ágiles, arquitectura hexagonal.',
            'bullets': [
                'Gestión de incidencias y desarrollo de evolutivos en la plataforma asegurando su correcto funcionamiento.',
                'Mantenimiento y optimización de microservicios basados en arquitectura hexagonal, facilitando un diseño limpio y escalable.',
                'Creación de pruebas unitarias e integrales utilizando JUnit y Mockito.',
            ]
        },
        {
            'company': 'NTTData (SEPE)',
            'title': 'Jr Backend Developer',
            'dates': 'oct. 2021 - feb. 2022',
            'tech': 'Java 6, Struts, Oracle, Jenkins, Sonar',
            'bullets': [
                'Desarrollo de nuevas funcionalidades en la aplicación del SEPE, mejorando la gestión de prestaciones y trámites de los ciudadanos.'
            ]
        },
        {
            'company': 'Proexe (Netflix) Varsovia',
            'title': 'Jr Backend Developer (Prácticas, Erasmus)',
            'dates': 'feb. 2021 - oct. 2021',
            'tech': 'Kotlin, Java, Spring Boot, Microservicios, Rest API, MySQL, JUnit, Mockito.',
            'bullets': []
        },
    ]

    for job in jobs:
        row = Table([[
            Paragraph(f'● {job["company"]}', S['job_company']),
            Paragraph(job['dates'], ParagraphStyle('DateR2', fontName='Helvetica',
                                                   fontSize=8, textColor=GRAY_MED,
                                                   alignment=TA_RIGHT))
        ]], colWidths=[RIGHT_COL_W*0.65, RIGHT_COL_W*0.35])
        row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                 ('LEFTPADDING',(0,0),(-1,-1),0),
                                 ('RIGHTPADDING',(0,0),(-1,-1),0),
                                 ('TOPPADDING',(0,0),(-1,-1),2),
                                 ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
        items.append(row)
        items.append(Paragraph(f'     {job["title"]}', S['job_title']))
        items.append(Spacer(1, 2))
        items.append(Paragraph(job['tech'], S['job_tech']))
        for b in job['bullets']:
            items.append(dot_bullet(b, S['bullet']))
        items.append(Spacer(1, 5))

    # ── Formación en IA ────────────────────────────────────────────
    items.append(Spacer(1, 4))
    items.append(Paragraph('🤖  Formación en IA', S['section_title']))
    items.append(hr(BLUE_LIGHT, 0.8))

    cursos_ia = [
        '<b>AWS Certified AI Practitioner (abr. 2026)</b>',
        'Curso Completo MCP – Aprende Model Context Protocol en 1 Día (Udemy, mar. 2026)',
        'Curso n8n – Agentes de IA Avanzados: MCP, WhatsApp, Voz (Udemy, mar. 2026)'
    ]
    for c in cursos_ia:
        items.append(Paragraph(c, S['course']))

    # ── Otros Cursos ───────────────────────────────────────────────
    items.append(Spacer(1, 6))
    items.append(Paragraph('📚  Otros Cursos', S['section_title']))
    items.append(hr(BLUE_LIGHT, 0.8))

    cursos = [
        'Microservices: Clean Architecture, DDD, SAGA, Outbox & Kafka (Udemy, abr. 2026)',
        'Ansible desde cero (Udemy, jun. 2026)',
        'Curso de desarrollo de una API REST con Spring Boot',
        'Crea una app interactiva en Kotlin',
        'Aprendiendo Swift 5.5',
        'iOS Y Swift 5.7 Curso Completo Desde 0 a Profesional',
        'Introducción a Docker',
    ]
    for c in cursos:
        items.append(Paragraph(c, S['course']))

    return items


# ── Page background ───────────────────────────────────────────────────────────

def draw_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BLUE_SIDEBAR)
    canvas.rect(0, 0, LEFT_COL_W + 5*mm, PAGE_H, fill=1, stroke=0)
    canvas.restoreState()


# ── Build PDF ─────────────────────────────────────────────────────────────────

OUT = os.path.join(os.path.dirname(__file__), 'cv_javier_polo_updated.pdf')

doc = BaseDocTemplate(
    OUT, pagesize=A4,
    leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0,
)

left_frame = Frame(
    MARGIN * 0.6, MARGIN,
    LEFT_COL_W - MARGIN * 0.6, PAGE_H - 2 * MARGIN,
    leftPadding=4, rightPadding=4, topPadding=0, bottomPadding=4, id='left'
)
right_frame = Frame(
    LEFT_COL_W + 10*mm, MARGIN,
    PAGE_W - LEFT_COL_W - 16*mm, PAGE_H - 2 * MARGIN,
    leftPadding=2, rightPadding=4, topPadding=0, bottomPadding=4, id='right'
)

template = PageTemplate(id='TwoCol', frames=[left_frame, right_frame],
                        onPage=draw_background)
doc.addPageTemplates([template])

story = build_left() + [FrameBreak()] + build_right()
doc.build(story)
print(f'✅  CV generado en {OUT}')
