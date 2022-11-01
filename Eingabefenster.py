from tkinter import *

#Ein Fenster, in dem die Informationen für einen neuen oder zu ändernden Eintrag eingegeben werden können.
class input_window(Tk):
    #Root ist das Hauptfenster, item der Eintrag, der geändert werden soll, item=None für das Fenster
    #für einen neu zu erstellenden Eintrag .
    def __init__(self,root,item=None):
        Tk.__init__(self)
        self.root=root
        self.item=item
        self.create_widgets()
        self.mainloop()
    
    #Hilfsfunktion, um die Elemente des Fensters zu erstellen.
    def create_widgets(self):
        self.label_title=Label(self,text="Titel: (erforderlich)")
        self.entry_title=Entry(self)
        self.label_description=Label(self,text="Beschreibung:")
        self.entry_description=Text(self,height=5,width=30)
        self.label_date=Label(self,text="Zu erledigen bis:")
        self.entry_date=Entry(self)
        self.priority=StringVar(self)
        self.priority.set("Mittel")
        self.label_priority=Label(self,text="Priorität:")
        self.entry_priority=OptionMenu(self,self.priority,"Hoch","Mittel","Niedrig")
        self.label_message=Label(self,text="")
        if not self.item==None:
            self.entry_title.insert(END,self.item.get_title())
            self.entry_description.insert(1.0,self.item.get_description())
            self.entry_date.insert(END,self.item.get_date())
            self.priority.set(self.item.get_priority())
        self.label_title.pack()
        self.entry_title.pack()
        self.label_description.pack()
        self.entry_description.pack()
        self.label_date.pack()
        self.entry_date.pack()
        self.label_priority.pack()
        self.entry_priority.pack()
        self.label_message.pack()
        if self.item==None:
            self.button_create=Button(self,text="Eintrag erstellen",command=self.create)
            self.button_create.pack()
        else:
            self.button_update=Button(self,text="Eintrag ändern",command=self.update)
            self.button_update.pack()

    #Gibt die Informationen für einen neu zu erstellenden Eintrag an das Hauptfenster zurück und schließt
    #dieses Fenster.
    def create(self):
        if self.entry_title.get()=="":
            self.label_message["text"]="Bitte geben Sie einen Titel ein."
        else:
            self.root.create_new(self.entry_title.get(),self.entry_description.get("1.0",'end-1c'),
            self.entry_date.get(),self.priority.get())
            self.destroy()

    #Gibt die Informationen für einen zu ändernden Eintrag an das Hauptfenster zurückk und schließt dieses
    #Fenster.
    def update(self):
        if self.entry_title.get()=="":
            self.label_message["text"]="Bitte geben Sie einen Titel ein."
        else:
            self.item.update(self.item.get_id(),self.entry_title.get(),
            self.entry_description.get("1.0",'end-1c'),self.entry_date.get(),self.priority.get())
            self.root.update(self.item)
            self.destroy()