import math
class ESG:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

   #CalculoECS
    def calculoECS(self, a, b, c):
        discriminante = math.pow(b, 2) - 4 * a * c
        if discriminante >= 0:
            raizdiscriminante = math.sqrt(discriminante)
            x1 = (-b + raizdiscriminante) / ( 2 * a)
            x2 = (-b - raizdiscriminante) / ( 2 * a)
            return x1, x2
        else :
            return None, None
    def definirParametros(self, a, b, c):
        self.a = self.parametroAFloat ( a )
        self.b = self.parametroAFloat ( b )
        self.c = self.parametroAFloat ( c )

    def parametroAFloat (self, parametro) :
        if not type ( parametro ) is float :
            try:
                parametro = float ( parametro )
            except ValueError :
                # raise ValueError("El parámetro no se puede convertir a float")
                print(f"El parámetro: \"{parametro}\" no se puede convertir a float")
                #exit(0)
                raise
        return parametro

    def solucionESG(self):
        self.x1=0
        self.x2=0

        d = math.pow(self.b, 2) - 4 * self.a * self.c
        if d >= 0 :
            r1 = (-self.b + math.sqrt ( d )) / (2 * self.a)
            r2 = (-self.b - math.sqrt ( d )) / (2 * self.a)
            self.x1 = "{0:.2f}".format(r1)
            self.x2 = "{0:.2f}".format(r2)
        else:
            parteReal = -self.b / (2 * self.a)
            parteImaginaria = math.sqrt(math.fabs(d))  / (2 * self.a)
            self.x1 = "{0:.2f}+{1:.2f}i".format(parteReal, parteImaginaria)
            self.x2 = "{0:.2f}-{1:.2f}i".format(parteReal, parteImaginaria)

        return self.x1, self.x2

    def imprimirSolución(self):
        print("\nEcuación de segundo grado")
        print ( "{0:.2f}X^2 + {1:.2f}x + {2:.2f}".format(self.a,self.b,self.c) )
        print ( "\nSolución:" )
        x1,x2=self.solucionESG ( )
        print ( f"X1 = {x1}" )
        print ( f"X2 = {x2}" )