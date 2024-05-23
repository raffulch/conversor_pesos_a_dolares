# Conversor de Pesos a Dólares

Este programa es una herramienta simple para convertir monedas de diferentes países a dólares estadounidenses (USD). Actualmente, admite conversiones para las siguientes monedas:

- Pesos chilenos (CLP)
- Pesos argentinos (ARS)
- Pesos colombianos (COP)
- Soles peruanos (PEN)

## Descripción

El script solicita al usuario que seleccione un país y luego ingrese la cantidad de dinero que desea convertir a dólares. Utiliza las tasas de cambio proporcionadas como argumentos y realiza la conversión, mostrando el resultado en la consola.

## Requisitos

- Python 3.10.3 o superior

## Instalación

1. Clona este repositorio o descarga el archivo `conversor_pesos_a_dolares.py` en tu máquina local.
2. Asegúrate de tener Python instalado. Puedes verificar esto ejecutando `python --version` en tu terminal.

## Uso

Para ejecutar el script, usa el siguiente comando en tu terminal:

```sh
python conversor_pesos_a_dolares.py [--valor_dolar_chile VALOR] [--valor_dolar_argentina VALOR] [--valor_dolar_colombia VALOR] [--valor_dolar_peru VALOR]
```

### Argumentos

- `--valor_dolar_chile`: Tasa de cambio de pesos chilenos a dólares (por defecto: 758.69)
- `--valor_dolar_argentina`: Tasa de cambio de pesos argentinos a dólares (por defecto: 94.50)
- `--valor_dolar_colombia`: Tasa de cambio de pesos colombianos a dólares (por defecto: 3875)
- `--valor_dolar_peru`: Tasa de cambio de soles peruanos a dólares (por defecto: 3.75)

### Ejemplo

```sh
python conversor_pesos_a_dolares.py --valor_dolar_chile 800 --valor_dolar_argentina 95 --valor_dolar_colombia 4000 --valor_dolar_peru 4
```

## Funcionamiento

1. El script muestra un menú para que el usuario seleccione su país.
2. Solicita la cantidad de dinero que desea convertir.
3. Realiza la conversión utilizando la tasa de cambio correspondiente.
4. Muestra el resultado en la consola.
5. Pregunta al usuario si desea realizar otra conversión.

## Notas

- Asegúrate de ingresar valores numéricos válidos cuando se te solicite.
- Si ingresas un valor inválido, el programa te pedirá que ingreses un valor numérico válido.
- Puedes actualizar las tasas de cambio utilizando los argumentos al ejecutar el script.

## Contacto

Si tienes alguna pregunta o sugerencia, por favor contáctame.

---

# Currency Converter: Pesos to US Dollars

This program is a simple tool to convert various currencies to United States Dollars (USD). Currently, it supports conversions for the following currencies:

- Chilean Pesos (CLP)
- Argentine Pesos (ARS)
- Colombian Pesos (COP)
- Peruvian Soles (PEN)

## Description

The script asks the user to select a country and then enter the amount of money they want to convert to dollars. It uses the provided exchange rates as arguments and performs the conversion, displaying the result in the console.

## Requirements

- Python 3.10.3 or higher

## Installation

1. Clone this repository or download the `conversor_pesos_a_dolares.py` file to your local machine.
2. Ensure you have Python installed. You can verify this by running `python --version` in your terminal.

## Usage

To run the script, use the following command in your terminal:

```sh
python conversor_pesos_a_dolares.py [--valor_dolar_chile VALUE] [--valor_dolar_argentina VALUE] [--valor_dolar_colombia VALUE] [--valor_dolar_peru VALUE]
```

### Arguments

- `--valor_dolar_chile`: Exchange rate from Chilean Pesos to US Dollars (default: 758.69)
- `--valor_dolar_argentina`: Exchange rate from Argentine Pesos to US Dollars (default: 94.50)
- `--valor_dolar_colombia`: Exchange rate from Colombian Pesos to US Dollars (default: 3875)
- `--valor_dolar_peru`: Exchange rate from Peruvian Soles to US Dollars (default: 3.75)

### Example

```sh
python conversor_pesos_a_dolares.py --valor_dolar_chile 800 --valor_dolar_argentina 95 --valor_dolar_colombia 4000 --valor_dolar_peru 4
```

## How it Works

1. The script displays a menu for the user to select their country.
2. It asks for the amount of money to be converted.
3. It performs the conversion using the appropriate exchange rate.
4. It displays the result in the console.
5. It asks the user if they want to perform another conversion.

## Notes

- Ensure you enter valid numeric values when prompted.
- If you enter an invalid value, the program will ask you to enter a valid numeric value.
- You can update the exchange rates using the arguments when running the script.

## Contact

If you have any questions or suggestions, please contact me.
