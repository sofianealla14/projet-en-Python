#import pygame
#from variables import * # permet impoter tout
#import copy
from niveau import Niveau


if __name__ == "__main__":
    is_running = True
    var_n = Niveau()
    while is_running == True :
        var_n.afficher() # seulement pour le terminal pas utile en soit dans le jeu
        dep = var_n.touche()
        var_n.deplacement(dep)
        var_n.next_level()