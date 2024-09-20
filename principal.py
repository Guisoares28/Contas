from View.Menu import MenuAPP
from Controller.controller import ControllerConta as controller

if __name__ == '__main__':
    MenuAPP.mostrarMenu()
    escolha = MenuAPP.escolha()
    if escolha == 1:
        print(controller.cadastrarConta())



