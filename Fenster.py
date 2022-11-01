from tkinter import *
import ListManager
import Eingabefenster
import Eintrag

#Diese Klasse beschreibt das Hauptfenster des Programms, in dem die Einträge der ToDo-Liste angezeigt werden
#und bearbeitet werden können.

class window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.manager=ListManager.list_manager()
        self.button_new=Button(self,text="Neuen Eintrag erstellen",command=self.create_new_open)
        self.button_new.pack()
        self.draw_frames()
        self.mainloop()

    #Erzeugt zu jedem gespeicherten Listeneintrag ein Tkinter-Frame und fügt diese Frames in das
    #Fenster ein.
    def draw_frames(self):
        self.items=self.manager.read_from_file()
        self.frames=[]
        for item in self.items:
            frame=self.build_frame(item)
            frame.pack(fill="x")
            self.frames.append(frame)

    #Öffnet ein zweites Fenster, um die für einen neuen Eintrag nötigen Informationen abzufragen.
    def create_new_open(self):
        Eingabefenster.input_window(self)

    #Erzeugt einen neuen Eintrag in der Liste, veranlasst, dass dieser gespeichert wird und erzeugt die
    #auf dem Bildschirm angezeigte Liste neu. Die Parameter sind die Attribute des neu zu erzeugenden
    #Eintrags.
    def create_new(self,title,description,date,priority):
        id=self.manager.find_id()
        item=Eintrag.list_item(id,title,description,date,priority)
        self.manager.add_to_file(item)
        self.redraw_frames()

    #Öffnet ein zweites Fenster, um die nötigen Informationen abzufragen, um den Listeneintrag item zu
    #aktualisieren.
    def update_open(self,item):
        Eingabefenster.input_window(self,item)

    #Veranlasst, dass der gespeicherte Eintrag item aktualisiert wird, und erzeugt die auf dem Bildschirm
    #angezeigte Liste neu.
    def update(self,item):
        self.manager.update_in_file(item)
        self.redraw_frames()

    #Veranlasst das der Eintrag item aus den gespeicherten Einträgen gelöscht wird und erzeugt die auf dem
    #Bildschirm angezeigte Liste neu.
    def delete(self,item):
        self.manager.delete_from_file(item.id)
        self.redraw_frames()

    #Erzeugt zu dem Listeneintrag item ein Tkinter-Frame mit dessen Informationen.
    def build_frame(self,item):
        frame=Frame(self,relief="sunken",bd=1,background="blue")
        label=Label(frame,text=item.get_title()+"\n"+
        "Frist: "+item.get_date()+ "\n"+
        "Priorität: "+item.get_priority()+"\n"+"\n"+
        item.get_description(),background="blue",justify="left")
        label.pack(side="left")
        subframe=Frame(frame)
        button_delete=Button(subframe,text="Löschen",command=lambda:self.delete(item))
        button_delete.pack(side="top")
        button_update=Button(subframe,text="Ändern",command=lambda:self.update_open(item))
        button_update.pack(side="bottom")
        subframe.pack(side="right")
        return frame

    #Löscht die Frames aus der gespeicherten Liste und erzeugt sie mit den derzeit gespeicherten Einträgen neu.
    def redraw_frames(self):
        for frame in self.frames:
            frame.destroy()
        self.draw_frames()
        

window()