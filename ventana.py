from tkinter import *
from tkinter import ttk
from clases import *
from tkinter import messagebox


class Ventana(Frame):
    
    laboratorios = Lab()
    provedores = Supp()
    items = Item()

    def __init__(self, master=None):
        super().__init__(master, bg="lightblue", width=1200, height=600)  # Nuevas dimensiones
        self.master = master
        self.pack()
        self.create_menu_buttons()
        self.create_widgets_labs()
        self.llenaDatosLab()
        self.habilitarCajasLabs("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id = -1
        self.current_section = "labs"
                   
    def habilitarCajasLabs(self, estado):
        self.txtname.configure(state=estado)
        self.txtaddress.configure(state=estado)
        self.txtphone.configure(state=estado)
        self.txtemail.configure(state=estado)
        self.txtstatus.configure(state=estado)
        
    def habilitarCajasSupp(self, estado):
        self.txtnamesupp.configure(state=estado)
        self.txtaddresssupp.configure(state=estado)
        self.txtphonesupp.configure(state=estado)
        self.txtemailsupp.configure(state=estado)
        self.txtstatussupp.configure(state=estado)

    def habilitarCajasItems(self, estado):
        self.txtnameitem.configure(state=estado)
        self.cmblabs.configure(state=estado)
        self.cmbsuppliers.configure(state=estado)
        self.txtprice.configure(state=estado)
        self.txtcategory.configure(state=estado)
        self.txtexpiration.configure(state=estado)
        self.txtdescription.configure(state=estado if estado == "normal" else "disabled")
        self.txtstatusitem.configure(state=estado)

    def habilitarBtnOper(self, estado):
        self.btnNuevo.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        
    def habilitarBtnGuardar(self, estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado)
        
    def limpiarCajasLabs(self):
        self.txtname.delete(0, END)
        self.txtaddress.delete(0, END)
        self.txtphone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtstatus.delete(0, END)

    def limpiarCajasSup(self):
        self.txtnamesupp.delete(0, END)
        self.txtaddresssupp.delete(0, END)
        self.txtphonesupp.delete(0, END)
        self.txtemailsupp.delete(0, END)
        self.txtstatussupp.delete(0, END)

    def limpiarCajasItems(self):
        self.txtnameitem.delete(0, END)
        self.cmblabs.set("")
        self.cmbsuppliers.set("")
        self.txtprice.delete(0, END)
        self.txtcategory.delete(0, END)
        self.txtexpiration.delete(0, END)
        self.txtdescription.delete("1.0", END)
        self.txtstatusitem.delete(0, END)

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
                
    def llenaDatosLab(self):
        datos = self.laboratorios.consulta_laboratorios()        
        for row in datos:            
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])
    
    def llenaDatosSupp(self):
        datos = self.provedores.consulta_proveedores()        
        for row in datos:            
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def llenaDatosItems(self):
        datos = self.items.consulta_items()        
        for row in datos:            
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def create_menu_buttons(self):
        self.btnItems = Button(text="Articulos", command=self.fItems, bg="#FFDAB9", fg="Black")
        self.btnItems.place(x=10, y=15, width=100, height=40)        
        self.btnSuppl = Button(text="Proveedores", command=self.fSuppl, bg="#FFDAB9", fg="Black")
        self.btnSuppl.place(x=120, y=15, width=100, height=40)        
        self.btnLabo = Button(text="Laboratorios", command=self.fLabo, bg="#FFDAB9", fg="Black")
        self.btnLabo.place(x=230, y=15, width=100, height=40)

    def create_widgets_labs(self):
        self.current_section = "labs"
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=80, width=150, height=520)  
        self.btnNuevo = Button(frame1, text="Nuevo", command=self.fNuevoLa, bg="blue", fg="white")
        self.btnNuevo.place(x=10, y=50, width=100, height=40)        
        self.btnModificar = Button(frame1, text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=10, y=100, width=100, height=40)                
        self.btnEliminar = Button(frame1, text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=10, y=150, width=100, height=40)        
        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=150, y=80, width=290, height=520) 
        lbl1 = Label(frame2, text="Nombre del laboratorio: ")
        lbl1.place(x=10, y=10)        
        self.txtname = Entry(frame2)
        self.txtname.place(x=10, y=30, width=200, height=25)  # Aumentado
        lbl2 = Label(frame2, text="Direccion del Laboratorio: ")
        lbl2.place(x=10, y=60)        
        self.txtaddress = Entry(frame2)
        self.txtaddress.place(x=10, y=80, width=200, height=25)  # Aumentado
        lbl3 = Label(frame2, text="Numero del Laboratorio: ")
        lbl3.place(x=10, y=110)        
        self.txtphone = Entry(frame2)
        self.txtphone.place(x=10, y=130, width=200, height=25)  # Aumentado
        lbl4 = Label(frame2, text="Correo electronico del Laboratorio: ")
        lbl4.place(x=10, y=160)        
        self.txtemail = Entry(frame2)
        self.txtemail.place(x=10, y=180, width=200, height=25)  # Aumentado
        lbl5 = Label(frame2, text="Status Laboratorio: ")
        lbl5.place(x=10, y=210)        
        self.txtstatus = Entry(frame2)
        self.txtstatus.place(x=10, y=230, width=80, height=25)  # Aumentado
        self.btnGuardar = Button(frame2, text="Guardar", command=self.fGuardarL, bg="green", fg="white")
        self.btnGuardar.place(x=10, y=280, width=80, height=40)
        self.btnCancelar = Button(frame2, text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=100, y=280, width=80, height=40)         
        frame3 = Frame(self, bg="white")
        frame3.place(x=450, y=80, width=720, height=510) 
        self.grid = ttk.Treeview(frame3, columns=("col1", "col2", "col3", "col4", "col5"))        
        self.grid.column("#0", width=50)
        self.grid.column("col1", width=120, anchor=CENTER)
        self.grid.column("col2", width=170, anchor=CENTER)
        self.grid.column("col3", width=120, anchor=CENTER)
        self.grid.column("col4", width=190, anchor=CENTER)        
        self.grid.column("col5", width=50, anchor=CENTER)        
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="name", anchor=CENTER)
        self.grid.heading("col2", text="address", anchor=CENTER)
        self.grid.heading("col3", text="phone", anchor=CENTER)
        self.grid.heading("col4", text="email", anchor=CENTER)                
        self.grid.heading("col5", text="status", anchor=CENTER)                
        self.grid.pack(side=LEFT, fill=Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode'] = 'browse'

    def create_widgets_supp(self):
        self.current_section = "suppliers"
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=80, width=150, height=520)  
        self.btnNuevo = Button(frame1, text="Nuevo", command=self.fNuevoSu, bg="blue", fg="white")
        self.btnNuevo.place(x=10, y=50, width=100, height=40)        
        self.btnModificar = Button(frame1, text="Modificar", command=self.fModificarSu, bg="blue", fg="white")
        self.btnModificar.place(x=10, y=100, width=100, height=40)                
        self.btnEliminar = Button(frame1, text="Eliminar", command=self.fEliminarSu, bg="blue", fg="white")
        self.btnEliminar.place(x=10, y=150, width=100, height=40)        
        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=150, y=80, width=290, height=520)  
        lbl1 = Label(frame2, text="Nombre del Proveedor: ")
        lbl1.place(x=10, y=10)        
        self.txtnamesupp = Entry(frame2)
        self.txtnamesupp.place(x=10, y=30, width=200, height=25)  # Aumentado
        lbl2 = Label(frame2, text="Direccion del Proveedor: ")
        lbl2.place(x=10, y=60)        
        self.txtaddresssupp = Entry(frame2)
        self.txtaddresssupp.place(x=10, y=80, width=200, height=25)  # Aumentado
        lbl3 = Label(frame2, text="Numero del Proveedor: ")
        lbl3.place(x=10, y=110)        
        self.txtphonesupp = Entry(frame2)
        self.txtphonesupp.place(x=10, y=130, width=200, height=25)  # Aumentado
        lbl4 = Label(frame2, text="Correo electronico del Proveedor: ")
        lbl4.place(x=10, y=160)        
        self.txtemailsupp = Entry(frame2)
        self.txtemailsupp.place(x=10, y=180, width=200, height=25)  # Aumentado
        lbl5 = Label(frame2, text="Status Proveedor: ")
        lbl5.place(x=10, y=210)        
        self.txtstatussupp = Entry(frame2)
        self.txtstatussupp.place(x=10, y=230, width=80, height=25)  # Aumentado
        self.btnGuardar = Button(frame2, text="Guardar", command=self.fGuardarS, bg="green", fg="white")
        self.btnGuardar.place(x=10, y=280, width=80, height=40)
        self.btnCancelar = Button(frame2, text="Cancelar", command=self.fCancelarSup, bg="red", fg="white")
        self.btnCancelar.place(x=100, y=280, width=80, height=40)         
        frame3 = Frame(self, bg="white")
        frame3.place(x=450, y=80, width=720, height=510)  
        self.grid = ttk.Treeview(frame3, columns=("col1", "col2", "col3", "col4", "col5"))        
        self.grid.column("#0", width=50)
        self.grid.column("col1", width=120, anchor=CENTER)
        self.grid.column("col2", width=170, anchor=CENTER)
        self.grid.column("col3", width=120, anchor=CENTER)
        self.grid.column("col4", width=190, anchor=CENTER)        
        self.grid.column("col5", width=50, anchor=CENTER)        
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="name", anchor=CENTER)
        self.grid.heading("col2", text="address", anchor=CENTER)
        self.grid.heading("col3", text="phone", anchor=CENTER)
        self.grid.heading("col4", text="email", anchor=CENTER)                
        self.grid.heading("col5", text="status", anchor=CENTER)                
        self.grid.pack(side=LEFT, fill=Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode'] = 'browse'

    def create_widgets_items(self):
        self.current_section = "items"
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=80, width=150, height=520)
        self.btnNuevo = Button(frame1, text="Nuevo", command=self.fNuevoIt, bg="blue", fg="white")
        self.btnNuevo.place(x=10, y=50, width=100, height=40)        
        self.btnModificar = Button(frame1, text="Modificar", command=self.fModificarIt, bg="blue", fg="white")
        self.btnModificar.place(x=10, y=100, width=100, height=40)                
        self.btnEliminar = Button(frame1, text="Eliminar", command=self.fEliminarIt, bg="blue", fg="white")
        self.btnEliminar.place(x=10, y=150, width=100, height=40)        
        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=150, y=80, width=290, height=520)  
        lbl1 = Label(frame2, text="Nombre del Articulo: ")
        lbl1.place(x=10, y=10)        
        self.txtnameitem = Entry(frame2)
        self.txtnameitem.place(x=10, y=30, width=200, height=25)  
        lbl2 = Label(frame2, text="Laboratorio: ")
        lbl2.place(x=10, y=60)        
        self.cmblabs = ttk.Combobox(frame2, values=self.get_labs_list(), state="readonly")
        self.cmblabs.place(x=10, y=80, width=200, height=25)  
        lbl3 = Label(frame2, text="Proveedor: ")
        lbl3.place(x=10, y=110)        
        self.cmbsuppliers = ttk.Combobox(frame2, values=self.get_suppliers_list(), state="readonly")
        self.cmbsuppliers.place(x=10, y=130, width=200, height=25)  
        lbl4 = Label(frame2, text="Precio: ")
        lbl4.place(x=10, y=160)        
        self.txtprice = Entry(frame2)
        self.txtprice.place(x=10, y=180, width=120, height=25)  
        lbl5 = Label(frame2, text="Categoria: ")
        lbl5.place(x=10, y=210)        
        self.txtcategory = Entry(frame2)
        self.txtcategory.place(x=10, y=230, width=200, height=25)  
        lbl6 = Label(frame2, text="Fecha Expiracion (dd/mm/yyyy): ")
        lbl6.place(x=10, y=260)        
        self.txtexpiration = Entry(frame2)
        self.txtexpiration.place(x=10, y=280, width=120, height=25)  
        lbl7 = Label(frame2, text="Descripcion: ")
        lbl7.place(x=10, y=310)        
        self.txtdescription = Text(frame2, height=4, width=25)
        self.txtdescription.place(x=10, y=330, width=200, height=80)  
        lbl8 = Label(frame2, text="Status: ")
        lbl8.place(x=10, y=415)        
        self.txtstatusitem = Entry(frame2)
        self.txtstatusitem.place(x=10, y=435, width=80, height=25)  
        self.btnGuardar = Button(frame2, text="Guardar", command=self.fGuardarIt, bg="green", fg="white")
        self.btnGuardar.place(x=10, y=470, width=80, height=40)
        self.btnCancelar = Button(frame2, text="Cancelar", command=self.fCancelarIt, bg="red", fg="white")
        self.btnCancelar.place(x=100, y=470, width=80, height=40)         
        frame3 = Frame(self, bg="white")
        frame3.place(x=450, y=80, width=720, height=510) 
        self.grid = ttk.Treeview(frame3, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))        
        self.grid.column("#0", width=40)
        self.grid.column("col1", width=100, anchor=CENTER)
        self.grid.column("col2", width=50, anchor=CENTER)
        self.grid.column("col3", width=50, anchor=CENTER)
        self.grid.column("col4", width=80, anchor=CENTER)
        self.grid.column("col5", width=100, anchor=CENTER)
        self.grid.column("col6", width=100, anchor=CENTER)
        self.grid.column("col7", width=120, anchor=CENTER)
        self.grid.column("col8", width=60, anchor=CENTER)
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Name", anchor=CENTER)
        self.grid.heading("col2", text="Lab ID", anchor=CENTER)
        self.grid.heading("col3", text="Supp ID", anchor=CENTER)
        self.grid.heading("col4", text="Price", anchor=CENTER)
        self.grid.heading("col5", text="Category", anchor=CENTER)
        self.grid.heading("col6", text="Expiration", anchor=CENTER)
        self.grid.heading("col7", text="Description", anchor=CENTER)
        self.grid.heading("col8", text="Status", anchor=CENTER)
        self.grid.pack(side=LEFT, fill=Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode'] = 'browse'

    def get_labs_list(self):
        labs = self.laboratorios.consulta_laboratorios()
        return [f"{lab[0]} - {lab[1]}" for lab in labs]

    def get_suppliers_list(self):
        suppliers = self.provedores.consulta_proveedores()
        return [f"{supp[0]} - {supp[1]}" for supp in suppliers]

    def validate_item_fields(self):
        try:
            name = self.txtnameitem.get()
            labs_id = int(self.cmblabs.get().split(" - ")[0]) if self.cmblabs.get() else 0
            suppliers_id = int(self.cmbsuppliers.get().split(" - ")[0]) if self.cmbsuppliers.get() else 0
            price = float(self.txtprice.get())
            category = self.txtcategory.get()
            expiration = self.txtexpiration.get()
            description = self.txtdescription.get("1.0", END).strip()
            status = int(self.txtstatusitem.get())
            if not name or labs_id == 0 or suppliers_id == 0 or price <= 0 or not category or not expiration or status not in [1, 2]:
                return False
            return True
        except ValueError:
            return False

    def fNuevoLa(self):         
        self.habilitarCajasLabs("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajasLabs()        
        self.txtname.focus()

    def fNuevoSu(self):         
        self.habilitarCajasSupp("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajasSup()        
        self.txtnamesupp.focus()

    def fNuevoIt(self):         
        self.habilitarCajasItems("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajasItems()        
        self.txtnameitem.focus()

    def fLabo(self):
        self.create_widgets_labs()
        self.llenaDatosLab()
        self.habilitarCajasLabs("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id = -1 
        
    def fSuppl(self):
        self.create_widgets_supp()
        self.llenaDatosSupp()
        self.habilitarCajasSupp("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id = -1 

    def fItems(self):
        self.create_widgets_items()
        self.llenaDatosItems()
        self.habilitarCajasItems("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id = -1 

    def fGuardarL(self): 
        if self.id == -1:       
            self.laboratorios.inserta_laboratorio(self.txtname.get(), self.txtaddress.get(), self.txtphone.get(), self.txtemail.get(), self.txtstatus.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.laboratorios.modifica_laboratorio(self.id, self.txtname.get(), self.txtaddress.get(), self.txtphone.get(), self.txtemail.get(), self.txtstatus.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatosLab() 
        self.limpiarCajasLabs() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajasLabs("disabled")

    def fGuardarS(self): 
        if self.id == -1:       
            self.provedores.inserta_proveedores(self.txtnamesupp.get(), self.txtaddresssupp.get(), self.txtphonesupp.get(), self.txtemailsupp.get(), self.txtstatussupp.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.provedores.modifica_proveedores(self.id, self.txtnamesupp.get(), self.txtaddresssupp.get(), self.txtphonesupp.get(), self.txtemailsupp.get(), self.txtstatussupp.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatosSupp() 
        self.limpiarCajasSup() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajasSupp("disabled")

    def fGuardarIt(self): 
        if not self.validate_item_fields():
            messagebox.showwarning("Guardar", "Por favor, complete todos los campos correctamente.")
            return
        labs_id = int(self.cmblabs.get().split(" - ")[0])
        suppliers_id = int(self.cmbsuppliers.get().split(" - ")[0])
        if self.id == -1:       
            self.items.inserta_item(
                self.txtnameitem.get(), labs_id, suppliers_id, float(self.txtprice.get()),
                self.txtcategory.get(), self.txtexpiration.get(), self.txtdescription.get("1.0", END).strip(),
                self.txtstatusitem.get()
            )            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.items.modifica_item(
                self.id, self.txtnameitem.get(), labs_id, suppliers_id, float(self.txtprice.get()),
                self.txtcategory.get(), self.txtexpiration.get(), self.txtdescription.get("1.0", END).strip(),
                self.txtstatusitem.get()
            )
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatosItems() 
        self.limpiarCajasItems() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajasItems("disabled")

    def fModificar(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected, 'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id = clave  
            self.habilitarCajasLabs("normal")                         
            valores = self.grid.item(selected, 'values')
            self.limpiarCajasLabs()            
            self.txtname.insert(0, valores[0])
            self.txtaddress.insert(0, valores[1])
            self.txtphone.insert(0, valores[2])
            self.txtemail.insert(0, valores[3])            
            self.txtstatus.insert(0, valores[4])            
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtname.focus()

    def fModificarSu(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected, 'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id = clave  
            self.habilitarCajasSupp("normal")                         
            valores = self.grid.item(selected, 'values')
            self.limpiarCajasSup()            
            self.txtnamesupp.insert(0, valores[0])
            self.txtaddresssupp.insert(0, valores[1])
            self.txtphonesupp.insert(0, valores[2])
            self.txtemailsupp.insert(0, valores[3])            
            self.txtstatussupp.insert(0, valores[4])            
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtnamesupp.focus()

    def fModificarIt(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected, 'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id = clave  
            self.habilitarCajasItems("normal")                         
            valores = self.grid.item(selected, 'values')
            self.limpiarCajasItems()            
            self.txtnameitem.insert(0, valores[0])
            self.cmblabs.set([lab for lab in self.get_labs_list() if lab.startswith(f"{valores[1]} - ")][0])
            self.cmbsuppliers.set([supp for supp in self.get_suppliers_list() if supp.startswith(f"{valores[2]} - ")][0])
            self.txtprice.insert(0, valores[3])
            self.txtcategory.insert(0, valores[4])
            self.txtexpiration.insert(0, valores[5])
            self.txtdescription.insert("1.0", valores[6])
            self.txtstatusitem.insert(0, valores[7])
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtnameitem.focus()

    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected, 'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected, 'values')
            data = str(clave) + ", " + valores[0]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.laboratorios.elimina_laboratorio(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatosLab()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')

    def fEliminarSu(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected, 'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected, 'values')
            data = str(clave) + ", " + valores[0]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.provedores.elimina_proveedores(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatosSupp()
                else:
                   ("/", "Eliminar", 'No fue posible eliminar el elemento.')

    def fEliminarIt(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected, 'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected, 'values')
            data = str(clave) + ", " + valores[0]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.items.elimina_item(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatosItems()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')

    def fCancelar(self):
        r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajasLabs() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajasLabs("disabled")

    def fCancelarSup(self):
        r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajasSup() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajasSupp("disabled")

    def fCancelarIt(self):
        r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajasItems() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajasItems("disabled")