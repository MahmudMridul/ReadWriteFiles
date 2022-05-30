from docx import Document
document = Document()

for num in range(9,54):
    docname = str(num) + '.' + 'docx'
    document.save(docname)

