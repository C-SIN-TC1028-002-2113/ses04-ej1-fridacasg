def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    id = input("¿Tienes identificación oficial? (s/n): ")
    if edad>=0 and edad<=100 and id== "s" or id== "n":
        if edad>=18 and id=="s" :
            print("Trámite de licencia concedido")
        else:
            print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")        



if __name__ == '__main__':
    main()
