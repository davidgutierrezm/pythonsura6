#los diccionarios son variables especiales que me permiten almacenar
#multiples datos de diferente TIPO EN UNA SOLA VARIABLE

empleado = {
    'nombre': "Juan",
    'cedula': 1128407766,
    'cargo': "Analista de datos",
    'salario':8000000,
    'horasTrabajadas': 40,
    'aplicaSubsidioTransporte': False,
    'deuda': [1500000,800000]
}
print(empleado)
print(empleado['deuda'][1])

# Recorriendo un diccionario:
for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)
    
    
