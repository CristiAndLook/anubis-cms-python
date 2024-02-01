import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING

class centerWindowMixin:
    def center(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

class MainWindow(Tk, centerWindowMixin):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Clientes")
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame, columns=("DNI", "Name", "Last Name"))
        treeview.heading("#0", text="ID")
        treeview.heading("DNI", text="DNI")
        treeview.heading("Name", text="Name")
        treeview.heading("Last Name", text="Last Name")
        treeview.column("#0", width=0, stretch=NO)

        scrollbar = Scrollbar(frame, orient="vertical", command=treeview.yview)
        scrollbar.pack(side="right", fill="y")
        treeview.configure(yscrollcommand=scrollbar.set)

        clients = db.Clients.list_clients
        for client in clients:
            treeview.insert(parent="", index="end",iid=client.dni, values=(client.dni, client.name, client.last_name))

        treeview.pack()

        buttons_frame = Frame(self)

        Button(buttons_frame, text="Add", command=None).grid(row=0, column=0)
        Button(buttons_frame, text="Modify", command=None).grid(row=0, column=1)
        Button(buttons_frame, text="Delete", command=self.delete).grid(row=0, column=2)

        buttons_frame.pack(pady=20)

        self.treeview = treeview

    def delete(self):
        client = self.treeview.focus()
        if client: 
            camps = self.treeview.item(client, "values")
            comfirm = askokcancel(
                title="Are you sure you want to delete this client?",
                message=f'¿Are you sure you want to delete the client with DNI {camps[0]}, {camps[1], camps[2]}?',
                icon=WARNING
            )
            if comfirm:
                self.treeview.delete(client)



    
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()