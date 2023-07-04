from io import BytesIO

from file_converter.types.document import Document


class DOCX(Document):
    can_converts_to = [
        'pdf',
        'odt',
        'html',
        'txt',
        'rtf'
    ]
    format = 'docx'

    def convert_to_pdf() -> BytesIO: ...
    