
import django


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DocumentBot.settings')
django.setup()

from pdf_form_filler import PdfForm
from models import User_doc
pdf_form = PdfForm("i-765.pdf")

data = {
    'form1[0].Page1[0].Line1a_FamilyName[0]': 'AAAAAAA',
    'form1[0].Page1[0].Line1b_GivenName[0]': 'BBBBB',
    'form1[0].Page1[0].Line1c_MiddleName[0]': 'CCCCCCCCasfCCCCC',
    'form1[0].Page1[0].Part1_Checkbox[0]': 1,
    'form1[0].Page1[0].Line2a_FamilyName[0]': 'AAAWWWWW',
    'form1[0].Page1[0].USCISELISAcctNumber[0]': "145656789",
    'form1[0].Page1[0].CheckBox1[0]': 1
}

pdf_form.fill_pdf(data)


model_object = User_doc.objects.get(id=0)
model_object.PDF.save("output.pdf", pdf_form.read())

# для теста сохранения файла в файловую систему
pdf_form.save("output.pdf") # Для теста