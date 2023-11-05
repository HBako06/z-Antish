import tkinter
from tkinter import messagebox as mb
import requests
import json

ventana = tkinter.Tk()
ventana.title("Software Lion")

frm = tkinter.Frame(ventana)
frm.grid(column=0, row=0, padx=(25, 25))

#Consulta DNI
label1 = tkinter.Label(frm, text="Consulta DNI", font="-weight bold")
label1.grid(row=0, column=0, pady=10)

anchoText = 35

#Txt Buscar DNI
txtDNIBuscar = tkinter.Entry(frm, width=anchoText)
txtDNIBuscar.grid(row=1, column=0)

#BTN BUSCAR
btnBuscar = tkinter.Button(frm, text="Buscar", width=29, bg="blue", fg="white", command= lambda: buscar())
btnBuscar.grid(row=2, column=0)

##RESPONSE
fila = 3

#DNI - CUI
label2 = tkinter.Label(frm, text="DNI - CUI: ")
label2.grid(row=fila, column=0, sticky="w")
fila = fila + 1

txtDniCui = tkinter.Entry(frm, width=anchoText)
txtDniCui.grid(row=fila, column=0, sticky="w")
fila = fila + 1

#PATERNO
label2 = tkinter.Label(frm, text="A. Paterno: ")
label2.grid(row=fila, column=0, sticky="w")
fila = fila + 1

txtPaterno = tkinter.Entry(frm, width=anchoText)
txtPaterno.grid(row=fila, column=0, sticky="w")
fila = fila + 1

#MATERNO
label2 = tkinter.Label(frm, text="A. Materno: ")
label2.grid(row=fila, column=0, sticky="w")
fila = fila + 1

txtMaterno = tkinter.Entry(frm, width=anchoText)
txtMaterno.grid(row=fila, column=0, sticky="w")
fila = fila + 1

#NOMBRES
label2 = tkinter.Label(frm, text="Nombres: ")
label2.grid(row=fila, column=0, sticky="w")
fila = fila + 1

txtNombres = tkinter.Entry(frm, width=anchoText)
txtNombres.grid(row=fila, column=0, sticky="w")
fila = fila + 1

#SEXO
label2 = tkinter.Label(frm, text="Sexo: ")
label2.grid(row=fila, column=0, sticky="w")
fila = fila + 1

txtSexo = tkinter.Entry(frm, width=anchoText)
txtSexo.grid(row=fila, column=0, sticky="w", pady=(0, 10))
fila = fila + 1
##END RESPONSE

def buscar():
    dni = txtDNIBuscar.get()

    txtPaterno.delete(0, tkinter.END)
    txtMaterno.delete(0, tkinter.END)
    txtNombres.delete(0, tkinter.END)
    txtDniCui.delete(0, tkinter.END)
    txtSexo.delete(0, tkinter.END)

    url = "https://www.softwarelion.xyz/api/reniec/reniec-dni"
    _json = { "dni": dni }
    token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyNDIxLCJjb3JyZW8iOiJtb2NvOTEyeGRAZ21haWwuY29tIiwiaWF0IjoxNjYyMDkwMTU2fQ.B4p41hmxEvTNb3jCunu1LcS2gDe18FKGw9JbAEA3wdo"
    _headers = { 'Content-Type': 'application/json', 'Authorization': token }

    response = requests.post(url, data=json.dumps(_json), headers=_headers)

    dataJson = response.json()

    if(dataJson['success'] == False):
        mb.showwarning("Jesús", dataJson['message'])
        return

    persona = dataJson['result']

    txtPaterno.insert(0, persona['paterno'])
    txtMaterno.insert(0, persona['materno'])
    txtNombres.insert(0, persona['nombres'])
    txtDniCui.insert(0, dni +"-"+ persona['codigoVerificacion'])
    txtSexo.insert(0, persona['sexo'])


ventana.mainloop()
