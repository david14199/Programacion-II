from conectar import cur
from conectar import miconexion
import pymysql
hola=True
print("ingrese registrar si quiere ingresar un nuevo producto")
print("ingrese muestrame si quiere ver los productos disponibles")
print("ingrese eliminar si quiere eliminar algun producto")
print("ingrese comprar si quiere comprar algun producto")
while hola:
    opcion=input("ingrese su opcion ").lower()

    if opcion=="muestrame":
        cur.execute("select id,producto,precios,inventario from productos")
        for id,producto,precios,inventario in cur.fetchall():
            print("el id es",id,"el nombre del producto es;",producto,"su precio es:",precios,"Su inventario es:",inventario)

    if opcion=="registrar":
        id=input("ingrese el id del producto ")
        nombre=input("ingrese el nombre del producto ")
        valor=int(input("ingrese el precio del producto "))
        inven=int(input("ingrese el inventario del producto "))
        sql='''INSERT INTO productos (id,producto, precios, inventario) 
    VALUES( '{}', '{}','{}', '{}')'''.format(id,nombre,valor ,inven)
        cur.execute(sql)
        n=cur.rowcount
        print(n)
        miconexion.commit()
        
    if opcion=="eliminar":
        nombre2=input("ingrese el nombr del producto ")
        elimina='''DELETE FROM productos WHERE producto = {}'''.format(nombre2)
        cur.execute(elimina)
        n=cur.rowcount
        print(n)
        miconexion.commit()
        cur.close()
    if opcion=="comprar":
        compra=True
        while compra:
            comprare=input("ingrese la ide de su producto a comprar")
            cur.execute("select*from productos Where producto={}".format(comprare))
            for id,producto,precios,inventario in cur.fetchall():
                print("el id es",id,"el nombre del producto es;",producto,"su precio es:",precios,"Su inventario es:",inventario)

            if comprare=="fin":
                compra=False

    if opcion=="1":
        hola=False
        print("tenga buen dia")
