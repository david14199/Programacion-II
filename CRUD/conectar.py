import pymysql
try:
    miconexion=pymysql.connect(host='localhost',user='root',db='compras')
    cur=miconexion.cursor()
except:
    print("no se ha podido conectar a la base de")



    

  
  