from typing import Union, BinaryIO, Dict

from PyPDFForm import PdfWrapper, FormWrapper


class PdfForm(FormWrapper):
    def __init__(self, template: Union[bytes, str, BinaryIO] = b"",):
        super().__init__(template)
        self.pdf = PdfWrapper(template)
        self.pdf_form = self

    def get_fields(self):
        return self.pdf.schema

    def get_field_values(self):
        return self.pdf.sample_data

    def get_field_value(self, field_name):
        field_values = self.get_field_values()
        return field_values.get(field_name)

    def fill_pdf(self, data: Dict[str, Union[str, bool, int]], **kwargs):
        self.pdf_form.fill(data, **kwargs)
        return self.pdf_form

    def save(self, output_path):
        with open(output_path, "wb+") as output:
            output.write(self.pdf_form.read())