from Modelos.Mesa import Mesa
from Modelos.Mesa2 import Mesa2
from sesiones.sesion import db

class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todas las mesas")

        consulta = Mesa2.query.all()
        lista = []
        for i in consulta:
            lista.append(i.consulta())

        return lista
        #consulta = db.session.query(Mesa2).all()
        #return consulta



    def create(self,infoMesa):
        print("Crear una mesa")
        numeroMesa = infoMesa.get('numeroMesa')
        cant_inscritos = infoMesa.get('cant_inscritos')
        mesa = Mesa2(numeroMesa = numeroMesa, cant_inscritos = cant_inscritos)
        db.session.add(mesa)
        db.session.commit()
        #laMesa = Mesa(infoMesa)
        #return laMesa.__dict__
        return {
            "Mesa #" : numeroMesa,
            "Cantidad de inscritos": cant_inscritos
        }

    def show(self,id):
        print("Mostrando una mesa con id ",id)

        consultaMesa = Mesa2.query.get(id)
        resultado = db.session.query(consultaMesa)
        #resultado = db.session.commit()
        return resultado


    def update(self,id,infoMesa):
        print("Actualizando mesa con id ",id)

        actualizar = Mesa2.query.get(id)
        actualizar.cant_inscritos = infoMesa.get('cant_inscritos')
        db.session.add(actualizar)
        db.session.commit()
        return {'Mesagge': "Mesa actualizada"}

        #laMesa = Mesa(infoMesa)
        #return laMesa.__dict__

    def delete(self,id):
        print("Elimiando mesa con id ",id)
        eliminarId = Mesa2.query.get(id)
        db.session.delete(eliminarId)
        delete = db.session.commit()

        return {"Se eliminó mesa # ": id}