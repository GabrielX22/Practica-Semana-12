#Gabriel Eduardo Henriquez Gonzalez
#Salvador Mauricio Chavarria Carranza
from tkinter import Entry, Label,Button,Tk,messagebox,Text
import smtplib
ventana = Tk()
ventana.title("Gestion de Correos")
ventana.geometry('510x420')
ventana.resizable(0,0)
ventana.configure(bg="aqua")
lblenviar = Label(ventana,text="Enviar a: ",bg="aqua")
lblenviar.place(x=100,y=20,width=100,height=20)
correo = Entry(ventana,bg="white")
correo.place(x=200,y=20,width=200,height=25)
lblusuario = Label(ventana,text="Usuario: ",bg="aqua")
lblusuario.place(x=100,y=100,width=100,height=20)
usuario = Entry(ventana,bg="white")
usuario.place(x=200,y=100,width=200,height=25)
space = Text(ventana,bg="white")
space.place(x=60,y=150,width=400,height=150)
def enviocorreo():
    if(usuario.get()== "" or correo.get()== "" or space.get("1.0","end")==""):
        messagebox.showwarning("Correo","Rellene los valores necesarios")
    else:
        enviarmi = usuario.get()
        elusuario = correo.get()
        mensaje = space.get("1.0","end")
        correo_origen="Su correo"
        contra_origen="Su contraseña para aplicaciones"
        server = smtplib.SMTP('smtp.gmail.com:587') 
        server.starttls() 
        server.login(correo_origen,contra_origen) 
        server.sendmail(enviarmi, elusuario, mensaje) 
        server.quit()
        messagebox.showinfo("Correo",f"El correo fue enviado correctamente a {elusuario}")
        usuario.delete(0, 'end')
        correo.delete(0, 'end')
        space.delete("1.0","end")   
btnenviar = Button(ventana,text="Enviar",command=enviocorreo,bg="light blue")
btnenviar.place(x=230,y=320,width=70,height=30)
ventana.mainloop()
