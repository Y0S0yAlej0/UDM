gastos = [
    {"id": "G001", "categoria": "comida",        "valor": 18000, "dia": 1,  "metodo": "tarjeta",       "lugar": "Cafeteria",     "nota": "almuerzo"},
    {"id": "G002", "categoria": "transporte",    "valor":  4200, "dia": 1,  "metodo": "tarjeta",       "lugar": "Metro",         "nota": "pasaje"},
    {"id": "G003", "categoria": "servicios",     "valor": 65000, "dia": 2,  "metodo": "transferencia", "lugar": "EPM",           "nota": "energia"},
    {"id": "G004", "categoria": "comida",        "valor":  9500, "dia": 2,  "metodo": "efectivo",      "lugar": "Panaderia",     "nota": "onces"},
    {"id": "G005", "categoria": "entretenimiento","valor": 28000,"dia": 3,  "metodo": "tarjeta",       "lugar": "Cine",          "nota": "entrada"},
    {"id": "G006", "categoria": "transporte",    "valor": 12000, "dia": 3,  "metodo": "efectivo",      "lugar": "Taxi",          "nota": "carrera"},
    {"id": "G007", "categoria": "educacion",     "valor": 35000, "dia": 4,  "metodo": "transferencia", "lugar": "Plataforma",    "nota": "curso"},
    {"id": "G008", "categoria": "salud",         "valor": 16000, "dia": 4,  "metodo": "tarjeta",       "lugar": "Farmacia",      "nota": "medicina"},
    {"id": "G009", "categoria": "comida",        "valor": 22000, "dia": 5,  "metodo": "tarjeta",       "lugar": "Restaurante",   "nota": "cena"},
    {"id": "G010", "categoria": "hogar",         "valor":  8700, "dia": 5,  "metodo": "efectivo",      "lugar": "Tienda",        "nota": "aseo"},
    {"id": "G011", "categoria": "servicios",     "valor": 54000, "dia": 6,  "metodo": "transferencia", "lugar": "Claro",         "nota": "internet"},
    {"id": "G012", "categoria": "transporte",    "valor":  4200, "dia": 6,  "metodo": "tarjeta",       "lugar": "Metro",         "nota": "pasaje"},
    {"id": "G013", "categoria": "entretenimiento","valor": 15000,"dia": 7,  "metodo": "efectivo",      "lugar": "Parque",        "nota": "snacks"},
    {"id": "G014", "categoria": "comida",        "valor":  7600, "dia": 7,  "metodo": "efectivo",      "lugar": "Cafeteria",     "nota": "tinto"},
    {"id": "G015", "categoria": "hogar",         "valor": 39000, "dia": 8,  "metodo": "tarjeta",       "lugar": "Supermercado",  "nota": "mercado"},
]

lista1 = [x["valor"] for x in gastos]
print(lista1)

lista2 = [x["lugar"].upper () for x in gastos]
print(lista2)

lista3 = [x["id"] for x in gastos if x["metodo"] == "tarjeta"]
print(lista3)

lista4 = [x["valor"] for x in gastos if x["categoria"] == "transporte"]
print(lista4)

lista5 = [(x["id"], x["categoria"], x["valor"], x["lugar"]) for x in gastos]
print(lista5)

lista6 = ["ALTO" if x["valor"] >= 30000 else "NORMAL" for x in gastos]
print(lista6)

lista7 = [int(x["valor"]) * 1.02 if x["metodo"] == "tarjeta" else int(x["valor"]) for x in gastos]
print(lista7)

lista8 = [x["nota"].strip().lower() for x in gastos if x["categoria"] == "comida"]
print(lista8)


dict1 = {x["id"]: x for x in gastos}
print(dict1)

dict2 = {x["id"]: x["valor"] for x in gastos}
print(dict2)

dict3 = {"Revisar" if x["valor"] > 50000 else "ok": x["valor"] for x in gastos}
print(dict3)