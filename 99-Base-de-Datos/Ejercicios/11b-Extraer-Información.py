from pymongo import MongoClient
from functools import reduce
from datetime import datetime, date

# Conexión con MongoDB
connect = MongoClient("mongodb://localhost:27017/")
db = connect.Northwind

productos = connect.Northwind.products
pedidos = connect.Northwind.orders
pedidos_detalle = connect.Northwind.order_details

# Coste o Valor de nuestro Stock utilizand map() y sum()
TotalStock = sum(list(map(lambda x: float(x['UnitPrice']) * int(x['UnitsInStock']), productos.find())))
print(f"\nValor del Stock: {TotalStock:1.2f}")
print("")

# Coste o Valor de nuestro Stock utilizand map() y reduce()
TotalStock = reduce(lambda x,y: x + y, map(lambda x: float(x['UnitPrice']) * int(x['UnitsInStock']), productos.find()))
print(f"\nValor del Stock: {TotalStock:1.2f}")
print("")

# Facturación entre fechas
def FilterForDate(x) -> bool:
    dt = datetime.strptime(x['OrderDate'][0:10], "%Y-%m-%d").date()
    if(dt >= date1 and dt <= date2):
        return True
    else:
        return False

def FilterForOrderID(x) -> bool:
    if(x['OrderID'] in pedidos):
        return True
    else:
        return False

date1 = datetime.strptime("01-08-1996", "%d-%m-%Y").date()
date2 = datetime.strptime("31-08-1996", "%d-%m-%Y").date()
pedidos = list(map(lambda x: x['OrderID'], filter(FilterForDate, pedidos.find())))

result = sum(map(lambda x: float(x['UnitPrice']) * int(x['Quantity']), filter(FilterForOrderID, pedidos_detalle.find())))
print("Facturación: {s:1.2f}".format(s=result))





# Ventas por Vendedor
