def contarLineas(nombre_archivo):
    archivo = open(nombre_archivo, 'r') 
    contador = 0
    for linea in archivo:
        contador += 1
    archivo.close()
    return contador

#print(contarLineas('hola.txt'))

def existePalabra(palabra, nombre_archivo):
    res = False
    archivo = open(nombre_archivo, 'r')
    lineas_archivo = archivo.readlines() 
    for linea in lineas_archivo:
        if palabra in linea:
            res = True
            return res
    archivo.close()
    return res 

#print(existePalabra('chau', 'hola.txt'))

def cantidadApariciones(palabra, nombre_archivo):
    res = False
    archivo = open(nombre_archivo, 'r')
    lineas_archivo = archivo.readlines() 
    for linea in lineas_archivo:
        if palabra in linea:
            res = True
            return res
    archivo.close()
    return res 

def clonarSinComentarios(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    nuevo_archivo = open('nuevo_archivo.txt','w')
    #some logic
    lineas_archivo = archivo.readlines()
    for linea in lineas_archivo:
        #for caracter in linea:
        if linea[0][0] != "#":
            print(linea[0][0])
            nuevo_archivo.write(linea)                 
    #end some logic
    archivo.close()
    nuevo_archivo.close()
    return nuevo_archivo

""" clonarSinComentarios('hola.txt')
a = open('nuevo_archivo.txt','r')
texto = a.readlines()
print(texto)
a.close()
 """

def invertirLineas(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    nuevo_archivo = open('invertirLineas.txt','w')
    lineas_archivo = archivo.readlines()
    c = len(lineas_archivo)
    for linea in range(len(lineas_archivo)):
        if c > 0:
            nuevo_archivo.writelines(lineas_archivo[c-1])
            c -= 1
        else:
            nuevo_archivo.writelines(lineas_archivo[0])
            return
    archivo.close()
    nuevo_archivo.close()
    return nuevo_archivo

#invertirLineas('hola.txt')
#invertirLineas('p8.txt')
#invertirLineas('nuevo_archivo.txt')
invertirLineas('test_falla.txt')