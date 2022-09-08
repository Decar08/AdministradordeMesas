from sesiones.sesion import db

class Mesa2(db.Model):
    __tablename__= "Mesa"

    #id = db.Column(db.Integer, primary_key = True) db.String()
    numeroMesa = db.Column(db.Integer, primary_key = True)
    cant_inscritos = db.Column(db.String())

    def __init__(self, numeroMesa, cant_inscritos):
        self.numeroMesa = numeroMesa
        self.cant_inscritos = cant_inscritos

    def consulta(self):
        return {
            "Mesa #": self.numeroMesa,
            "Cantidad Inscritos": self.cant_inscritos
        }


    def __repr__(self):
        return f" Numero mesa: {self.numeroMesa}, Inscritos: {self.cant_inscritos}"
