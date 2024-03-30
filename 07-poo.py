class Personaje():
    vida = 1
    estadoVivo = True

    def estadPV(self, vida, estado):
        self.estadoVivo = estado
        self.vida = vida

        if estado == False: 
            vida = vida - 1

    def estadoActual(self, vida, estado):
        self.estadoVivo = estado
        if estado == True: 
            estado == "Vivo"
            print(f"el estado actual del personaje vidas: {vida}, estado actual: {estado} ") 

        else:
            estado = "muerto"
        print(f"el estado actual del personaje vidas: {vida}, estado actual: {estado} ") 

william = Personaje()
william.estadoActual(False, 1)