print("Emilio Chaparro 189304")

# Crear una funcion que calcule el area de un triangulo y evaluar los 
# valores, 3, 4, 25

def area_triangulo(base, altura):
    return (base * altura) / 2

base = 3
altura = 25
print(f"base: {base}, altura: {altura}, area: {area_triangulo(base, altura)}")
base = 4
print(f"base: {base}, altura: {altura}, area: {area_triangulo(base, altura)}")


#Utilizando los operadores de concatenacion y repeticion factorizar 
# para recrear las siguientes secuencias:
# '%%%%%./././<-><->%%%%%./././<-><->'
# (@)(@)(@)======(@)(@)(@)======

print("%" * 5 + "./" * 3 + "<->" * 2 + "%" * 5 + "./" * 3 + "<->" * 2)
print("(@)" * 3 + "======" + "(@)" * 3 + "======")
