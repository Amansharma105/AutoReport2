from jinja2 import Template

def generate_html_report(data):
    with open("templates/report.html", "r") as file:
        template = Template(file.read())

    return template.render(data=data)
