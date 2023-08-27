import PySimpleGUI as sg
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_pdf_report(data):
    filename = "software_receipt.pdf"
    doc = SimpleDocTemplate(filename, pagesize=landscape(letter))

    elements = []
    
    title = "Software Development Service Receipt"
    elements.append(Table([[title]], colWidths=600, style=[('ALIGN', (0, 0), (-1, -1), 'CENTER')]))

    table_data = [[key.replace('_', ' ').capitalize(), str(value)] for key, value in data.items()]
    table_data.append(["Total Price", f"${data['Total Price']}"])

    t = Table(table_data, colWidths=[250, 250], rowHeights=30)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.black),
        ('ALIGN', (0, -1), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, -1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 12),
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),
    ]))
    elements.append(t)

    doc.build(elements)

layout = [
    [sg.Text("Software Development Pricing Calculator")],
    [sg.Text("Hourly Rate ($ lkr):"), sg.InputText(key='hourly_rate')],
    [sg.Text("Hours Worked on Meetings:"), sg.InputText(key='hours_meetings')],
    [sg.Text("Hours Worked on Research:"), sg.InputText(key='hours_research')],
    [sg.Text("Hours Worked on Development:"), sg.InputText(key='hours_development')],
    [sg.Text("Hours Worked on Testing:"), sg.InputText(key='hours_testing')],
    [sg.Text("Hours Worked on Post-Deployment Fixes:"), sg.InputText(key='hours_post_deployment')],
    [sg.Text("Hours Worked on Maintenance Post-Launch:"), sg.InputText(key='hours_maintenance')],
    [sg.Button("Calculate"), sg.Button("Exit")]
]

window = sg.Window("Software Pricing Calculator", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Calculate':
        hourly_rate = float(values['hourly_rate'])

        hours_meetings = float(values['hours_meetings'])
        hours_research = float(values['hours_research'])
        hours_development = float(values['hours_development'])
        hours_testing = float(values['hours_testing'])
        hours_post_deployment = float(values['hours_post_deployment'])
        hours_maintenance = float(values['hours_maintenance'])

        total_hours_worked = hours_meetings + hours_research + hours_development + hours_testing + \
                             hours_post_deployment + hours_maintenance
        
        total_price = total_hours_worked * hourly_rate

        pricing_data = {
            'Hourly Rate': f"${hourly_rate:.2f}",
            'Hours Meetings': hours_meetings,
            'Hours Research': hours_research,
            'Hours Development': hours_development,
            'Hours Testing': hours_testing,
            'Hours Post-Deployment Fixes': hours_post_deployment,
            'Hours Maintenance Post-Launch': hours_maintenance,
            'Total Hours Worked': total_hours_worked,
            'Total Price': f"${total_price:.2f}"
        }

        generate_pdf_report(pricing_data)
        sg.popup("Calculation complete! Receipt saved as 'software_receipt.pdf'")

window.close()
