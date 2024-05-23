# Descripción: Programa que convierte pesos a dólares
import argparse

def conversor(valor_dolar_chile, valor_dolar_argentina, valor_dolar_colombia, valor_dolar_peru):
    """
    Convierte una cantidad de moneda de diferentes países a dólares basado en las tasas de cambio.

    Args:
        valor_dolar_chile (float): La tasa de cambio de pesos chilenos a dólares.
        valor_dolar_argentina (float): La tasa de cambio de pesos argentinos a dólares.
        valor_dolar_colombia (float): La tasa de cambio de pesos colombianos a dólares.
        valor_dolar_peru (float): La tasa de cambio de soles peruanos a dólares.
    """
    try:
        pais = int(input("\nSeleccione el número del país para convertir su dinero al valor del dólar:\n"
                         "1 - Chile\n"
                         "2 - Argentina\n"
                         "3 - Colombia\n"
                         "4 - Perú\n"))

        if pais == 1:
            pesos = float(input("\nIngrese la cantidad de pesos chilenos que desea convertir a dólares: "))
            dolares = pesos / valor_dolar_chile
            print(f'\nLa cantidad de {pesos} pesos chilenos equivale a {format(dolares, ".2f")} dólares') 
            
        elif pais == 2:
            pesos = float(input("\nIngrese la cantidad de pesos argentinos que desea convertir a dólares: "))
            dolares = pesos / valor_dolar_argentina
            print(f'\nLa cantidad de {pesos} pesos argentinos equivale a {format(dolares, ".2f")} dólares')
            
        elif pais == 3:
            pesos = float(input("\nIngrese la cantidad de pesos colombianos que desea convertir a dólares: "))
            dolares = pesos / valor_dolar_colombia
            print(f'\nLa cantidad de {pesos} pesos colombianos equivale a {format(dolares, ".2f")} dólares')
            
        elif pais == 4:
            pesos = float(input("\nIngrese la cantidad de soles peruanos que desea convertir a dólares: "))
            dolares = pesos / valor_dolar_peru
            print(f'\nLa cantidad de {pesos} soles peruanos equivale a {format(dolares, ".2f")} dólares')
            
        else:
            print("\nPor favor seleccione un número válido")
            conversor(valor_dolar_chile, valor_dolar_argentina, valor_dolar_colombia, valor_dolar_peru)     
        
        while True:
            respuesta = input("\n¿Desea convertir otra cantidad de pesos a dólares? (si/no): ")
            if respuesta.lower() == "si":
                conversor(valor_dolar_chile, valor_dolar_argentina, valor_dolar_colombia, valor_dolar_peru)
                break
            elif respuesta.lower() == "no":
                print("\n¡Gracias por usar nuestro conversor de pesos a dólares!")
                break
            else:
                print("\nPor favor ingrese una respuesta válida: si o no")
                continue
    except ValueError:
        print("\n¡Por favor ingrese un valor numérico!")
        conversor(valor_dolar_chile, valor_dolar_argentina, valor_dolar_colombia, valor_dolar_peru)
            
if __name__ == "__main__":
    print("********************************************")
    print("Bienvenido al conversor de pesos a dólares")
    print("*******************************************")
    parser = argparse.ArgumentParser(description="Conversor de pesos a dólares, países de origen: Chile, Argentina, Colombia, Perú")
    parser.add_argument('--valor_dolar_chile', type=float, help='Valor del dólar en pesos chilenos', default=758.69)
    parser.add_argument('--valor_dolar_argentina', type=float, help='Valor del dólar en pesos argentinos', default=94.50)
    parser.add_argument('--valor_dolar_colombia', type=float, help='Valor del dólar en pesos colombianos', default=3875)
    parser.add_argument('--valor_dolar_peru', type=float, help='Valor del dólar en soles peruanos', default=3.75)
        
    args = parser.parse_args()
    
    conversor(args.valor_dolar_chile, args.valor_dolar_argentina, args.valor_dolar_colombia, args.valor_dolar_peru)