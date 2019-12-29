import cx_Oracle as oracle

db = oracle.connect("demo_01/demo1007@192.168.1.102:1522/testDB0113")

cursor = db.cursor()

cursor.execute("select * from employee")

data = cursor.fetchall()


for index, item in enumerate(data):

  print(index+1, item)

cursor.close()

db.close()





