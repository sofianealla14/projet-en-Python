'''
import pygame
from niveau import Niveau
from page_accueil_niveaux import screen
from variables import PERSO , MUR , DEST , BOX , BOX_ON_ZONE , PERSO_ON_ZONE , VIDE # * pour tous les elements
'''

class Affichage(Niveau):
    
    def __init__(self):
        self.largeur = 0
        self.hauteur = 0
        self.case = 20
        
    def association(self):
        for ligne in Niveau.grille:
            self.hauteur += self.case
            self.largeur = 0
            for element in ligne:
                self.largeur += self.case
                image = self.image(element)
                screen.blit(image, (self.largeur, self.hauteur))
    
    def image(self, element):
        # if 
        theme = "ressources/kenney/theme1/"
        # elif
        #   theme2 = "ressources/kenney/thème2/"
        # ...
        if element == PERSO or PERSO_ON_ZONE:
            image = pygame.image.load(theme + 'PERSO.png')
        elif element == MUR:
            image = pygame.image.load(theme + 'mur.png')
        elif element == DEST:
            image = pygame.image.load(theme + 'chemin.png')
        elif element == BOX:
            image = pygame.image.load(theme + 'BOX.png')
        elif element == BOX_ON_ZONE:
            image = pygame.image.load(theme + 'BOX_ON_ZONE.png')
        elif element == VIDE:
            image = pygame.image.load(theme + 'VIDE.png')
        image = pygame.transform.scale(image , (20,20))
        return(image)