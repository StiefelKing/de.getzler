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
        try:
            self.filepath = filepath
            self.filename = os.path.basename(filepath)
            x = self.filename.split("-")
            self.year4 = x[0]
            self.year2 = self.year4[:2]
            self.notary = x[1]
            self.number = x[2].split(".")[0]
        except:
            pass

    @staticmethod
    def get_file(folder, document):
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.startswith(document):
                    return root + str(file)

    def get_document(self):
        if self.notary == "C":
            folder = "U:\\Caspary\\{}{}\\".format(self.notary, self.year4)
        elif self.notary == "M":
            folder = "U:\\Metzger\\{}{}\\".format(self.notary, self.year4)
        elif self.notary == "B":
            folder = "U:\\Berringer\\{}{}\\".format(self.notary, self.year4)
        elif self.notary == "V":
            folder = "U:\\Verwalter\\{}{}\\".format(self.notary, self.year4)
        else:
            print("Fehler, Notar nicht bekannt oder Dateiname entspricht nicht der Konvention.")
            return
        document = "{}{}_{}".format(self.notary, self.number, self.year2)
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.startswith(document):
                    return root + str(file), file


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


print("Wie viele Dateien sollen verbunden werden?")
j = 0
while j < 1:
    try:
        j = int(input())
    except ValueError:
        pass
i = 0
for root, dirs, files in os.walk("G:\\Notarstelle_Sonthofen\\Urkundenanlagen\\"):
    for file in files:
        try:
            if Attachment(file).get_document() is not None and i < j:
                print(Attachment(file).get_document()[0])
                paths = [Attachment(file).get_document()[0], "G:\\Notarstelle_Sonthofen\\Urkundenanlagen\\" + file]
                if not os.path.exists("C:\\" + os.getenv("HOMEPATH") + "\\Desktop\\Zusammengefügt\\"):
                    os.makedirs("C:\\" + os.getenv("HOMEPATH") + "\\Desktop\\Zusammengefügt\\")
                merge_pdfs(paths, output="C:\\" + os.getenv("HOMEPATH") + "\\Desktop\\Zusammengefügt\\" +
                                         Attachment(file).get_document()[1])
                os.rename("G:\\Notarstelle_Sonthofen\\Urkundenanlagen\\" + file,
                          "G:\\Notarstelle_Sonthofen\\Urkundenanlagen\\in Arbeit\\" + file)
                i += 1
        except FileNotFoundError:
            pass
