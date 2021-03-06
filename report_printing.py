from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

#['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

def print_report(fname,arr,res):
    res=round(res[0][0][0]*100,2)
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("template.html")
    template_vars = {"name" : fname,
                    "age": arr[7],
                    "preg":arr[0],
                    "glucose":arr[1],
                    "bp":arr[2],
                    "sk_thick":arr[3],
                    "insu":arr[4],
                    "bmi":arr[5],
                    "dpi":arr[6],
                    "result":res
                 }
    html_out = template.render(template_vars)
    fname="reports/"+fname+"_report.pdf"
    HTML(string=html_out).write_pdf(fname)
