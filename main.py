from cliente import Cliente
from vendedor import Vendedor
from menu import menu_principal

vendedor1 = Vendedor("", "", "", "", "", "", [])
cliente1 = Cliente("", "", "", "", "", "", "", "", "", vendedor1)
menu_principal(cliente1, vendedor1)