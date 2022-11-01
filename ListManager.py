import Eintrag

#Diese Klasse stellt Methoden bereit, um die csv-Datei, in der die Daten für die ToDo-Liste gespeichert
#werden, zu verwalten.
class list_manager():
    def __init__(self):
        self.file_name="Liste.csv"

    #Fügt einen neuen Eintrag mit den Informationen von item zur Datei hinzu.
    def add_to_file(self,item):
        with open(self.file_name,"a") as d:
            d.write(str(item.get_id())+";"+item.get_title()+";"+item.get_description()+";"+item.get_date()+";"+
            item.get_priority()+"\n")

    #Löscht den Eintrag mit der übergebenen id aus der Datei.
    def delete_from_file(self,id):
        test=str(id)+";"
        with open(self.file_name,"r+") as d:
            entries=d.readlines()
            d.seek(0)
            for item in entries:
                if not item.startswith(test):
                    d.write(item)
            d.truncate()

    #Ändert den Eintrag, der dieselbe id wie item hat und passt dessen Informationen an item an.
    def update_in_file(self,item):
        id=item.get_id()
        test=str(id)+";"
        with open(self.file_name,"r+") as d:
            entries=d.readlines()
            d.seek(0)
            for entry in entries:
                if entry.startswith(test):
                    d.write(str(item.get_id())+";"+item.get_title()+";"+item.get_description()+";"+
                    item.get_date()+";"+item.get_priority()+"\n")
                else:
                    d.write(entry)
            d.truncate()

    #Liest alle Einträge aus der Datei aus und gibt eine Liste der entsprechenden list_item-Objekte zurück.
    def read_from_file(self):
        try:
            d=open(self.file_name)
            entries=[a.replace("\n","") for a in d.readlines()]
            result=[]
            for a in entries:
                if a=="\n":
                    continue
                a=a.split(";")
                result.append(Eintrag.list_item(int(a[0]),a[1],a[2],a[3],a[4]))
            d.close()
            return result
        except FileNotFoundError:
            return []

    #Findet die kleinste id, die derzeit von keinem gespeicherten Eintrag verwendet wird.
    def find_id(self):
        id=0
        used_ids=[item.get_id() for item in self.read_from_file()]
        while(True):
            if id not in used_ids:
                return id
            id+=1
