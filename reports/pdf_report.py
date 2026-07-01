from reportlab.pdfgen import canvas

def generate_pdf(file_name):
    pdf = canvas.Canvas(file_name)
    pdf.drawString(100, 750, "AutoReport PDF Report")
    pdf.drawString(100, 730, "Generated Successfully!")
    pdf.save()
