from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todas las mesas")
        unaMesa = {
            "id": "1",
            "inscritos": "1000"

        }
        return [unaMesa]


    def create(self,infoMesa):
        print("Crear un estudiante")
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def show(self,id):
        print("Mostrando una mesa con id ",id)
        laMesa = {
            "id": id,
            "numeroMesa": "350",
            "cant_inscritos": "1000"
        }
        return laMesa

    def update(self,id,infoMesa):
        print("Actualizando mesa con id ",id)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def delete(self,id):
        print("Elimiando mesa con id ",id)
        return {"deleted_count": 1}