from tkinter import *
from tkinter import messagebox
from reportlab.pdfgen import canvas

#ROOT#
def ROOT(p):
 if p == 'name':
  return 'Genereitor The Pdf'
  
 elif p == 'background':
  return 'bgcrr.jpg'
  
def CreatePdf():
  cnv = canvas.Canvas('Curriculo.pdf')
  cnv.drawImage(ROOT('background'),1,250, 550, 600)
  
  cnv.drawString(115,785, vname.get())
  cnv.drawString(95, 620, vschool.get())
  
  cnv.drawString(95,695, vcargo.get())
  
  cnv.drawString(95,535, vperfil.get())
  
  cnv.drawString(95,435, vport.get())
  
  cnv.drawString(95,355, vcontat.get())
  
  
  cnv.save()
  messagebox.showinfo(title='Concluido', message='PDF GERADO!')
  
#SCREEN APP#
app = Tk()
app.title(ROOT('name'))

Label(app, text='Genereitor The Pdf', font='Arial 15').place(x=150, y=0)
Label(app, text='Nome:').place(x=50, y=200)
vname = Entry(app, placeholder='Seu Nome')
vname.place(x=250, y=200)
Label(app, text='Estudos:').place(x=50, y=300)
vschool = Entry(app, placeholder='Seu Nivel De Estudos')
vschool.place(x=250, y=300)

Label(app, text='Objetivo:').place(x=50, y=400)
vcargo = Entry(app, placeholder='Seu Objetivo')

vcargo.place(x=250, y= 400)

Label(app, text='Perfil:').place(x=50, y=500)
vperfil = Entry(app, placeholder='Sua Area De Trabalho')
vperfil.place(x=250, y=500)

Label(app, text='Portfolio:', font='monospace 7').place(x=50, y=600)
vport = Entry(app, placeholder='Seu Corriculo Virtual')

vport.place(x=250, y= 600)

Label(app, text='Contato:').place(x=50, y=700)
vcontat = Entry(app, placeholder='Seu Contato')
vcontat.place(x=250, y=700)

btn = Button(app, text='Create Pdf',command=CreatePdf)
btn.place(x=350, y=800)

#RUN#
app.mainloop()