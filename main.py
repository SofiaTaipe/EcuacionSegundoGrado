from src.logica.ESG import ESG

def solucionarEcuacion (a,b,c) :
    solucion.definirParametros(a, b, c)
    solucion.solucionESG()
    solucion.imprimirSolución()

if __name__ == '__main__':
    solucion = ESG()
    try:
        solucionarEcuacion(1, 2 ,1)
        solucionarEcuacion(1, 2 ,3)
        solucionarEcuacion("1", "2" ,"1")
        solucionarEcuacion("a", "b" ,"c")
    except ValueError:
          print("Uno de los parámetros no es un número")

