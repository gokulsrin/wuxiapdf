# this is the folder that will play with pdf generation
from reportlab.pdfgen import canvas 

class pdfGenerator:
    def __init__(self, bookTitle, nametextdic, namenumdic):
        self.bookTitle = bookTitle+".pdf"
        self.pdf = canvas.Canvas(self.bookTitle)

        #set the title 
        self.pdf.setTitle(self.bookTitle)
        self.pdf.setFont("Courier", 20)
        self.pdf.drawCentredString(300, 770,bookTitle)
        self.pdf.showPage()

        #we should also take a dictionary of type {chapter name: chapter text} && {chapter name: chapter number}
        self.nametext = nametextdic
        self.namenum = namenumdic

    def createBook(self):
        #create the book using the two maps we have
        for chaptername in self.nametext:
            self.createChapter(self.namenum[chaptername], chaptername, self.nametext[chaptername])

    def createChapter(self, chapterNumber, chapterName, chapterText):
        #draw the chapter number and name
        self.pdf.setFont("Courier", 14)
        self.pdf.drawCentredString(300, 770,"Chapter " + str(chapterNumber) + ": "+ chapterName)

        #draw text 
        lines = chapterText.split('\n')
        
        text = self.pdf.beginText(40, 700)
        text.setFont("Courier", 12)
        for line in lines:
            text.textLine(line)
        self.pdf.drawText(text)

        #save page 
        self.pdf.showPage()

    def save(self):
        self.pdf.save()

        

#TESTING createChapter()
nametextdic = {"cool":"One.\nThis is a long piece of text.\nIt should contain line breaks.\nOne more for good measure.", "hot":"Two.\nThis is a long piece of text.\nIt should contain line breaks.\nOne more for good measure."}
namenumdic = {"cool": 1, "hot": 2}
p = pdfGenerator("Test", nametextdic, namenumdic)
# s = "this is a long piece of text.\nIt should contain line breaks.\nOne more for good measure."
# p.createChapter(2, "Cool Chapter",s)

#TESTING createBook()
p.createBook()
p.save()

