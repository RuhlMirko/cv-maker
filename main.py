import fpdf
import functions

pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
content = functions.get_list()
pdf.set_auto_page_break(auto=False, margin=0)

pdf.set_font('Helvetica', '', 12)
pdf.add_page()
for item in content:
    pdf.cell(h=10, text=item, new_x="LMARGIN", new_y="NEXT")

paragraph = """Hi, my name is Mirko and I'm a python developer that loves to create things. I really like graphic 
design, I have developed a lot of web and desktop apps using modern day graphics and themes, with technologies such as bootstrap 5, css, tailwind, ttkbootstrap, tkinter and pysimple."""

pdf.multi_cell(0, 6, text=paragraph)

pdf.output('cv.pdf')
