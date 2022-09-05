from main import db
from Modelos import Mesa2
'''
#Crear
#db.create_all()
mesa = Mesa2.Mesa2("1","1000")
mesa2 = Mesa2.Mesa2("2","800")
mesa3 = Mesa2.Mesa2("3","1500")
db.session.add_all([mesa, mesa2, mesa3])
db.session.commit()


#Leer todo
resultado = Mesa2.Mesa2.query.all()
print("Las mesas son: ")
print(resultado)


#Leer uno
resultado2 = Mesa2.Mesa2.query.get(2)
print(resultado2)


#Actualizar
actualizar = Mesa2.Mesa2.query.get(2)
actualizar.cant_inscritos = "2500"
db.session.add(actualizar)
db.session.commit()


#Eliminar
eliminar = Mesa2.Mesa2.query.get(2)
db.session.delete(eliminar)
db.session.commit()
'''