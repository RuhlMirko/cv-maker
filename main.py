import fpdf
import functions

pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
content = functions.get_list()
pdf.set_auto_page_break(auto=False, margin=0)

pdf.set_font('Helvetica', '', 12)
pdf.add_page()
for item in content:
    pdf.cell(h=10, text=item, new_x="LMARGIN", new_y="NEXT")

pdf.output('cv.pdf')
