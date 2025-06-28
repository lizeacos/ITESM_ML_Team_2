from src.calculadora.Operaciones import sumar
def main():
  """Función principal que llama a otras funciones."""
  print("Dentro de main()")
  num1= 7
  num2= 1 
  suma = sumar.sumar(num1,num2)
  print(suma)

if __name__ == "__main__":
  main()