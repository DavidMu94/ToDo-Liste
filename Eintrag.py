#Ein Objekt dieser Klasse enthält alle Informationen, die für einen Eintrag in der ToDo-Liste nötig sind,
#nämlich id, Titel, Beschreibung, Frist und Priorität.
class list_item():
    #Erzeugt ein neues Objekt mit den übergebenen Eigenschaften.
    def __init__(self,id,title,description="",date="",priority="Mittel"):
        self.update(id,title,description,date,priority)

    #Ändert die Eigenschaften des aufrufenden Objekts auf die übergebenen Werte.
    def update(self,id,title,description="",date="",priority="Mittel"):
        self.id=id
        self.title=title
        self.description=description
        self.date=date
        self.priority=priority

    #Gibt die id des Objekts zurück.
    def get_id(self):
        return int(self.id)
    
    #Gibt den Titel des Objetks zurück.
    def get_title(self):
        return self.title

    #Gibt die Beschreibung des Objekts zurück.
    def get_description(self):
        return self.description

    #Gibt die Frist des Objekts zurück. Falls keine Frist eingetragen ist, wird "Keine" zurückgegeben.
    def get_date(self):
        if self.date!="":
            return self.date
        return "Keine"

    #Gibt die Priorität des Objekts zurück.
    def get_priority(self):
        return self.priority