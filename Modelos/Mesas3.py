from sesiones.sesion import db

class Mesa3(db.Model):
    __tablename__= "Tabla Mesas"

    #id = db.Column(db.Integer, primary_key = True) db.String()
    numeroMesa = db.Column(db.Integer, primary_key = True)
    cant_inscritos = db.Column(db.String())

    def __init__(self, cant_inscritos):
        #self.numeroMesa = numeroMesa
        self.cant_inscritos = cant_inscritos


    def __repr__(self):
        #return f" Numero mesa: {self.numeroMesa}, Inscritos: {self.cant_inscritos}"
        return f" Inscritos: {self.cant_inscritos}"