from vista import Vista_formulario
from modelo import Numero
from controlador import Controlador

class Principal:
    @staticmethod
    def main() -> None:
        vista = Vista_formulario()
        numero = Numero()
        controlador = Controlador(vista, numero)
        controlador.tomar_numero()

if __name__ == "__main__":
    Principal.main()
