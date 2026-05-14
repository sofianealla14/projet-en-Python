import pygame
from variables import PERSO , MUR , DEST , BOX , BOX_ON_ZONE , PERSO_ON_ZONE , VIDE # * pour tous les elements
import copy
import os
# from etoiles import Etoile

class Niveau():
    """
    # renvoie la liste du niveau demande
    def __init__(self):
        self.__init__( self.lecture_fichier(self.num_niveau))
        ''' les variables globales '''
        self.num_niveau = 1 # determine le niveau
        self.grille = self.lecture_fichier(self.num_niveau)
        self.recommencer = copy.deepcopy(self.grille) # permet recommencer niveau
        self.last = copy.deepcopy(self.grille) # retour arriere
        
        '''les variables pour la resolution de l'ordi '''
        
        self.premiere = None
        self.grille_IA = None # le terrain de l'ordi a l instant T
        """
        
    def __init__(self, grille=""):
        
        ''' les variables globales '''
        self.num_niveau = 1 # determine le niveau de l'humain
        self.num_niveau_IA = 1 # determine le niveau de l'IA
        self.grille =  self.lecture_fichier(self.num_niveau) # self.lecture_fichier(self.num_niveau)
        self.grille_IA = self.lecture_fichier(self.num_niveau_IA) # le terrain de l'ordi a l instant T
        
        self.recommencer = copy.deepcopy(self.grille) # permet recommencer niveau
        self.recommencer_IA = copy.deepcopy(self.grille_IA)
        self.last = copy.deepcopy(self.grille) # retour arriere
        
        
    
    # lit le fichier texte et le renvoie en liste qui est le niveau
    def lecture_fichier(self, num_niveau):
        # lecture des caracteres a partir du fichier niveau.xsb et les mettre dans liste_mots
        with open('ressources/levels/niveau'+str(num_niveau)+".xsb", encoding = 'utf-8') as f: # lecture ligne par ligne
            liste_mots = [mot[:-1]for mot in f.readlines()] # f.readlines() renvoie une ligne et mot[:-1] le passage a la ligne

        # print ( liste_mots )
        niveau = []
        ligne = []
        for l in liste_mots :
            ligne = []
            for c in l :
                ligne.append(c)
            niveau.append(ligne)
        return(niveau)
    
    # affiche en chaine de caractère la liste niveau 
    def afficher(self, grille):
        grille = self.grille
        sret = ""
        for ligne in grille :
            for element in ligne :
                sret += element
            sret += "\n"
        print(sret)
    
    # savoir si le niveau est fini
    def is_finish(self, grille):
        if grille != []:
            for ligne in grille :
                for c in ligne :
                    if c == DEST or c == PERSO_ON_ZONE :
                        return False
            return True
    
    # niveau suivant si is_finish est vrai        
    def next_level(self):
        nb_fichier=len(os.listdir('ressources/levels'))-1
        if self.num_niveau <= nb_fichier :
            if self.is_finish(self.grille) :
                self.num_niveau += 1 # incremente avant de lire le fichier
                self.grille=self.lecture_fichier(self.num_niveau)
                self.recommencer = copy.deepcopy(self.grille)
            
                print( "Niveau" , self.num_niveau , "pour l'humain" )
                return True
            return False
        else: 
            pygame.quit()
    
            

    def direction(self,x,y,map_1): # reste probleme dans de conflict pas regle ( niveau 3 )
        
        # determine la position du perso
        
        xPerso , yPerso = self.position()
        
        '''self.last = copy.deepcopy(self.grille)'''
        
        
        # deplacement du joueur sur une case vide
        if map_1[xPerso+x][yPerso+y] == VIDE and map_1[xPerso][yPerso] == PERSO: # si la case ou on va est vide
            map_1[xPerso][yPerso]= VIDE # change la case du joueur en vide
            map_1[xPerso+x][yPerso+y] = PERSO # change la case ou on va en case joueur
            
        elif map_1[xPerso+x][yPerso+y] == VIDE and map_1[xPerso][yPerso] == PERSO_ON_ZONE: # si la case ou on va est vide ET perso sur interupteur
            map_1[xPerso][yPerso]= DEST # change la case du joueur en destination
            map_1[xPerso+x][yPerso+y] = PERSO # change la case ou on va en case joueur
        
        
        
        # deplacement du joueur sur une case destination
        elif map_1[xPerso+x][yPerso+y] == DEST and map_1[xPerso][yPerso] == PERSO:
            map_1[xPerso][yPerso]= VIDE
            map_1[xPerso+x][yPerso+y] = PERSO_ON_ZONE
        
        elif map_1[xPerso+x][yPerso+y] == DEST and map_1[xPerso][yPerso] == PERSO_ON_ZONE:
            map_1[xPerso][yPerso]= DEST
            map_1[xPerso+x][yPerso+y] = PERSO_ON_ZONE
        
        
        
        # deplacement du joueur sur une case avec une box avec la box vers du vide
        elif map_1[xPerso+x][yPerso+y] == BOX and map_1[xPerso+2*x][yPerso+2*y] == VIDE and map_1[xPerso][yPerso] == PERSO: # verifie si la boite peux se deplacer
            map_1[xPerso][yPerso]= VIDE
            map_1[xPerso+x][yPerso+y] = PERSO
            map_1[xPerso+2*x][yPerso+2*y] = BOX
        
        elif map_1[xPerso+x][yPerso+y] == BOX and map_1[xPerso+2*x][yPerso+2*y] == VIDE and map_1[xPerso][yPerso] == PERSO_ON_ZONE: # verifie si la boite peux se deplacer
            map_1[xPerso][yPerso]= DEST
            map_1[xPerso+x][yPerso+y] = PERSO
            map_1[xPerso+2*x][yPerso+2*y] = BOX
        
        
         
        
         
        # deplacement du joueur sur une case avec une box avec la box vers la destination
        elif map_1[xPerso+x][yPerso+y] == BOX and map_1[xPerso+2*x][yPerso+2*y] == DEST and map_1[xPerso][yPerso] == PERSO: # verifie si la boite peux se deplacer
            map_1[xPerso][yPerso]= VIDE 
            map_1[xPerso+x][yPerso+y] = PERSO 
            map_1[xPerso+2*x][yPerso+2*y] = BOX_ON_ZONE 
        
        elif map_1[xPerso+x][yPerso+y] == BOX and map_1[xPerso+2*x][yPerso+2*y] == DEST and map_1[xPerso][yPerso] == PERSO_ON_ZONE: # verifie si la boite peux se deplacer
            map_1[xPerso][yPerso]= DEST
            map_1[xPerso+x][yPerso+y] = PERSO
            map_1[xPerso+2*x][yPerso+2*y] = BOX_ON_ZONE
        
        
        
        elif map_1[xPerso+x][yPerso+y] == BOX_ON_ZONE and map_1[xPerso+2*x][yPerso+2*y] == VIDE and map_1[xPerso][yPerso] == PERSO:
            map_1[xPerso][yPerso]= VIDE
            map_1[xPerso+x][yPerso+y] = PERSO_ON_ZONE
            map_1[xPerso+2*x][yPerso+2*y] = BOX
        
        elif map_1[xPerso+x][yPerso+y] == BOX_ON_ZONE and map_1[xPerso+2*x][yPerso+2*y] == VIDE and map_1[xPerso][yPerso] == PERSO_ON_ZONE:
            map_1[xPerso][yPerso]= DEST
            map_1[xPerso+x][yPerso+y] = PERSO_ON_ZONE
            map_1[xPerso+2*x][yPerso+2*y] = BOX
        
        
        
        elif map_1[xPerso+x][yPerso+y] == BOX_ON_ZONE and map_1[xPerso+2*x][yPerso+2*y] == DEST and map_1[xPerso][yPerso] == PERSO:
            map_1[xPerso][yPerso]= VIDE
            map_1[xPerso+x][yPerso+y] = PERSO_ON_ZONE
            map_1[xPerso+2*x][yPerso+2*y] = BOX_ON_ZONE
        
        elif map_1[xPerso+x][yPerso+y] == BOX_ON_ZONE and map_1[xPerso+2*x][yPerso+2*y] == DEST and map_1[xPerso][yPerso] == PERSO_ON_ZONE:
            map_1[xPerso][yPerso]= DEST
            map_1[xPerso+x][yPerso+y] = PERSO_ON_ZONE
            map_1[xPerso+2*x][yPerso+2*y] = BOX_ON_ZONE
        
        
        else:
            print('Tu ne peux pas avancer')
            self.direction_possible=False

    def position( self ):
        for y in range(len(self.grille[0])):
            for x in range(len(self.grille)):
                if self.grille[x][y] == PERSO or self.grille[x][y] == PERSO_ON_ZONE:
                        return( x, y )
    
    
    def touche (self):
        dep = ' '
        while dep != 'z' and dep != 'q' and dep != 's' and dep != 'd' and dep != 'e':
            dep = input('Deplacez vous avec zqsd et e pour recommencer le niveau')  
        return dep
    
    
    def deplacement(self ,dep):

        # se deplace en haut
        if dep == 'z':
            self.direction( -1 , 0 , self.grille)

        # se deplace a gauche
        elif dep == 'q':
            self.direction( 0 , -1 , self.grille)

        # se deplace en bas
        elif dep == 's':
            self.direction( 1 , 0 , self.grille)

        # se deplace a droite
        elif dep == 'd':
            self.direction( 0 , 1 , self.grille)
        
        # pour recommencer le niveau
        elif dep == 'e':
            self.grille = copy.deepcopy(self.recommencer)
        
        ''' 
        retour arriere
        elif dep == 'a':
            self.grille = copy.deepcopy(self.last)
        '''
    
    def image(self, element):
        theme = "ressources/kenney/theme1/"
        '''  
        # test pour changer de theme avec les touches 1 , 2 ,... mais il  y a des erreurs
        for event in pygame.event.get():
            # que l'évènement est fermeture de fenetre
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Fermeture du jeu")
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_1: 
                    theme = "ressources/kenney/theme1/"
                elif event.key == pygame.K_2 :
                    theme = "ressources/kenney/thème2/"
                # pygame.display.update() pour mise à jour
        '''     
        if element == PERSO :
            image = pygame.image.load(theme + 'PERSO.png')
        elif element == PERSO_ON_ZONE:
            image = pygame.image.load(theme + 'PERSO_ON_ZONE.png')
        elif element == MUR:
            image = pygame.image.load(theme + 'mur.png')
        elif element == DEST:
            image = pygame.image.load(theme + 'DEST.png')
        elif element == BOX:
            image = pygame.image.load(theme + 'BOX.png')
        elif element == BOX_ON_ZONE:
            image = pygame.image.load(theme + 'BOX_ON_ZONE.png')
        elif element == VIDE:
            image = pygame.image.load(theme + 'VIDE.png')
        image = pygame.transform.scale(image , (25,25))
        return(image)