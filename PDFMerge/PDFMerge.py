from PyPDF4 import PdfFileReader, PdfFileWriter
import os


class Attachment:
    filepath = ""
    filename = ""
    notary = ""
    number = 0
    year4 = 0
    year2 = 0

    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        x = self.filename.split("-")
        self.year4 = x[0]
        self.year2 = self.year4[:2]
        self.notary = x[1]
        self.number = x[2].split(".")[0]

    def getdocument(self):
        print("stub")
        if self.notary == "C":
            folder = "U:\\Caspary\\{}{}\\".format(self.notary, self.year4)
            file = "{}{}_{}".format(self.notary, self.number, self.year2)
            print(folder)
            print(file)
        # todo returns filepath of deed for attachment


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    paths = ['U:\\Caspary\\C2020\\C0487_20Pl.tlw.verkl.pdf',
             'G:\\Notarstelle_Sonthofen\\Urkundenanlagen\\2020-C-0487.pdf']
    Attachment(paths[1]).getdocument()
    # merge_pdfs(paths, output='merged.pdf')

# todo sorting through Filesystem get Year, Notary and Number from Anlage and Search in Ablage --> Ununified Filenames
# todo Output
# todo move Anlagen to in Arbeit
# todo input how many Files
