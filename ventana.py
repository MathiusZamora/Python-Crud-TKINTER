from tkinter import *
from tkinter import ttk
from clases import *
from tkinter import messagebox


class Ventana(Frame):
    
    

    laboratorios = Lab()
    provedores = Supp()
        

    def __init__(self, master=None):
        super().__init__(master,bg="lightblue",width=890, height=470)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatosLab()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1      
                   
    def habilitarCajas(self,estado):
        self.txtname.configure(state=estado)
        self.txtaddress.configure(state=estado)
        self.txtphone.configure(state=estado)
        self.txtemail.configure(state=estado)
        self.txtstatus.configure(state=estado)
         
        
    def habilitarBtnOper(self,estado):
        self.btnNuevo.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        
    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado)                
        
    def limpiarCajas(self):
        self.txtname.delete(0,END)
        self.txtaddress.delete(0,END)
        self.txtphone.delete(0,END)
        self.txtemail.delete(0,END)
        self.txtstatus.delete(0,END)

        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
                
    def llenaDatosLab(self):
        datos = self.laboratorios.consulta_laboratorios()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5]))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )
    
            
    def fNuevoLa(self):         
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()        
        self.txtname.focus()
    

    def fLabo(self):
        self.create_widgets()
        self.llenaDatosLab()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1 
        
    
    def fItems(self):
        pass    
    
    def fSuppl(self):
        self.create_widgets2()
        self.llenaDatosSupp()
        self.habilitarCajasSupp("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1 
      
    
    def fGuardarL(self): 
        if self.id ==-1:       
            self.laboratorios.inserta_laboratorio(self.txtname.get(),self.txtaddress.get(),self.txtphone.get(),self.txtemail.get(),self.txtstatus.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.laboratorios.modifica_laboratorio(self.id,self.txtname.get(),self.txtaddress.get(),self.txtphone.get(),self.txtemail.get(),self.txtstatus.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatosLab() 
        self.limpiarCajas() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")
    
    
                    
    def fModificar(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave  
            self.habilitarCajas("normal")                         
            valores = self.grid.item(selected,'values')
            self.limpiarCajas()            
            self.txtname.insert(0,valores[0])
            self.txtaddress.insert(0,valores[1])
            self.txtphone.insert(0,valores[2])
            self.txtemail.insert(0,valores[3])            
            self.txtstatus.insert(0,valores[4])            
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtname.focus()
                                        
    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.laboratorios.elimina_laboratorio(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatosLab()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def fCancelar(self):
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=112,width=100, height=359)        
        self.btnItems=Button(text="Articulos", command=self.fItems, bg="#FFDAB9", fg="Black")
        self.btnItems.place(x=2,y=50,width=80, height=40 )        
        self.btnSuppl=Button(text="Proveedores", command=self.fSuppl, bg="#FFDAB9", fg="Black")
        self.btnSuppl.place(x=92,y=50,width=80, height=40 )        
        self.btnLabo=Button(text="Laboratorios", command=self.fLabo, bg="#FFDAB9", fg="Black")
        self.btnLabo.place(x=182,y=50,width=80, height=40 )        
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevoLa, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=112,width=250, height=359)                        
        lbl1 = Label(frame2,text="Nombre del laboratorio: ")
        lbl1.place(x=3,y=5)        
        #self.txtname=Entry(frame2,textvariable = self.ISO3)
        self.txtname=Entry(frame2)
        self.txtname.place(x=3,y=25,width=150, height=20)                
        lbl2 = Label(frame2,text="Direccion del Laboratorio: ")
        lbl2.place(x=3,y=55)        
        self.txtaddress=Entry(frame2)
        self.txtaddress.place(x=3,y=75,width=150, height=20)        
        lbl3 = Label(frame2,text="Numero del Laboratorio: ")
        lbl3.place(x=3,y=105)        
        self.txtphone=Entry(frame2)
        self.txtphone.place(x=3,y=125,width=150, height=20)        
        lbl4 = Label(frame2,text="Correo electronico del Laboratorio: ")
        lbl4.place(x=3,y=155)        
        self.txtemail=Entry(frame2)
        self.txtemail.place(x=3,y=175,width=150, height=20)        
        lbl5 = Label(frame2,text="Status Laboratorio: ")
        lbl5.place(x=3,y=205)        
        self.txtstatus=Entry(frame2)
        self.txtstatus.place(x=3,y=225,width=50, height=20)        
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardarL, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=270,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=270,width=60, height=30)         
        frame3 = Frame(self,bg="white" )
        frame3.place(x=350,y=112,width=570, height=350)                      
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4","col5"))        
        self.grid.column("#0",width=60)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=155, anchor=CENTER)        
        self.grid.column("col5",width=70, anchor=CENTER)        
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="name", anchor=CENTER)
        self.grid.heading("col2", text="address", anchor=CENTER)
        self.grid.heading("col3", text="phone", anchor=CENTER)
        self.grid.heading("col4", text="email", anchor=CENTER)                
        self.grid.heading("col5", text="status", anchor=CENTER)                
        self.grid.pack(side=LEFT,fill = Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'
    











    def habilitarCajasSupp(self,estado):
        self.txtnamesupp.configure(state=estado)
        self.txtaddresssupp.configure(state=estado)
        self.txtphonesupp.configure(state=estado)
        self.txtemailsupp.configure(state=estado)
        self.txtstatussupp.configure(state=estado)

    def limpiarCajasSup(self):
        self.txtnamesupp.delete(0,END)
        self.txtaddresssupp.delete(0,END)
        self.txtphonesupp.delete(0,END)
        self.txtemailsupp.delete(0,END)
        self.txtstatussupp.delete(0,END)

    def llenaDatosSupp(self):
        datos = self.provedores.consulta_proveedores()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5]))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )   

    def fNuevoSu(self):         
        self.habilitarCajasSupp("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajasSup()        
        self.txtnamesupp.focus()

    def fGuardarS(self): 
        if self.id ==-1:       
            self.provedores.inserta_proveedores(self.txtnamesupp.get(),self.txtaddresssupp.get(),self.txtphonesupp.get(),self.txtemailsupp.get(),self.txtstatussupp.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.provedores.modifica_proveedores(self.id,self.txtnamesupp.get(),self.txtaddresssupp.get(),self.txtphonesupp.get(),self.txtemailsupp.get(),self.txtstatussupp.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatosSupp() 
        self.limpiarCajasSup() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajasSupp("disabled")


    def fModificarSu(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave  
            self.habilitarCajasSupp("normal")                         
            valores = self.grid.item(selected,'values')
            self.limpiarCajasSup()            
            self.txtnamesupp.insert(0,valores[0])
            self.txtaddresssupp.insert(0,valores[1])
            self.txtphonesupp.insert(0,valores[2])
            self.txtemailsupp.insert(0,valores[3])            
            self.txtstatussupp.insert(0,valores[4])            
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtnamesupp.focus()

    def fEliminarSu(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.provedores.elimina_proveedores(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatosSupp()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def fCancelarSup(self):
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajasSup() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajasSupp("disabled")        


    def create_widgets2(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=112,width=100, height=359)        
        self.btnItems=Button(text="Articulos", command=self.fItems, bg="#FFDAB9", fg="Black")
        self.btnItems.place(x=2,y=50,width=80, height=40 )        
        self.btnSuppl=Button(text="Proveedores", command=self.fSuppl, bg="#FFDAB9", fg="Black")
        self.btnSuppl.place(x=92,y=50,width=80, height=40 )        
        self.btnLabo=Button(text="Laboratorios", command=self.fLabo, bg="#FFDAB9", fg="Black")
        self.btnLabo.place(x=182,y=50,width=80, height=40 )        
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevoSu, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificarSu, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminarSu, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=112,width=250, height=359)                        
        lbl1 = Label(frame2,text="Nombre del Proveedor: ")
        lbl1.place(x=3,y=5)        
        #self.txtname=Entry(frame2,textvariable = self.ISO3)
        self.txtnamesupp=Entry(frame2)
        self.txtnamesupp.place(x=3,y=25,width=150, height=20)                
        lbl2 = Label(frame2,text="Direccion del Proveedor: ")
        lbl2.place(x=3,y=55)        
        self.txtaddresssupp=Entry(frame2)
        self.txtaddresssupp.place(x=3,y=75,width=150, height=20)        
        lbl3 = Label(frame2,text="Numero del Proveedor: ")
        lbl3.place(x=3,y=105)        
        self.txtphonesupp=Entry(frame2)
        self.txtphonesupp.place(x=3,y=125,width=150, height=20)        
        lbl4 = Label(frame2,text="Correo electronico del Proveedor: ")
        lbl4.place(x=3,y=155)        
        self.txtemailsupp=Entry(frame2)
        self.txtemailsupp.place(x=3,y=175,width=150, height=20)        
        lbl5 = Label(frame2,text="Status Proveedor: ")
        lbl5.place(x=3,y=205)        
        self.txtstatussupp=Entry(frame2)
        self.txtstatussupp.place(x=3,y=225,width=50, height=20)        
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardarS, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=270,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelarSup, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=270,width=60, height=30)         
        frame3 = Frame(self,bg="white" )
        frame3.place(x=350,y=112,width=570, height=350)                      
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4","col5"))        
        self.grid.column("#0",width=60)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=155, anchor=CENTER)        
        self.grid.column("col5",width=70, anchor=CENTER)        
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="name", anchor=CENTER)
        self.grid.heading("col2", text="address", anchor=CENTER)
        self.grid.heading("col3", text="phone", anchor=CENTER)
        self.grid.heading("col4", text="email", anchor=CENTER)                
        self.grid.heading("col5", text="status", anchor=CENTER)                
        self.grid.pack(side=LEFT,fill = Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'