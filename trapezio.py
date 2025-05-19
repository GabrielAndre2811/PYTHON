entradas = [float(input("Informe a base maior do trapézio: ")),
            float(input("Informe a base menor do trapézio: ")),
            float(input("Informe a altura do trapézio: "))]

base_maior = entradas[0]
base_menor = entradas[1]
altura = entradas[2]

base_triangulo = (base_maior - base_menor) / 2
area_triangulo = (base_triangulo * altura) / 3
area_total_triangulos = area_triangulo * 2
area_retangulo = base_menor * altura
area_total = area_total_triangulos + area_retangulo

areas = [area_total_triangulos, area_retangulo, area_total]


print(f"A área do triângulo é {areas[0]:.2f}")
print(f"A área do retângulo é {areas[1]:.2f}")
print(f"A área total é {areas[2]:.2f}")