import pygame
from niveau import Niveau
import copy

from etoiles import Etoile
from textniveau import TextNiveau
from deplacement_algo import deplacement_algo

# from variables import PERSO , MUR , DEST , BOX , BOX_ON_ZONE , PERSO_ON_ZONE , VIDE # * pour tous les elements
pygame.init()
pygame.font.init()

# generer la fenêtre de notre jeu
pygame.display.set_caption("sokoban-progressif")

# creer l'ecran d'accueil
screen = pygame.display.set_mode([1080,720]) # [0,0], pygame.FULLSCREEN
    
# importer l'arriere plan de notre jeu
background = pygame.image.load('ressources/fonds/fond_accueil.png')
    
# importer l'image du perso du jeu
joueur = pygame.image.load('ressources/fonds/PERSO(vierge).png')
    
# importer et dimensionner l'image d'entrer pour commencer
entrer = pygame.image.load('ressources/enter_to_begin.jpg')
entrer = pygame.transform.scale(entrer , (600,300))

running = True
is_playing = False
is_etoile = True # le bouleen determinant si il y a un etoile a faire
var_n = Niveau() # pour appeler la class niveau
text = TextNiveau(var_n) # pour le numero du niveau
num_actuel = 1 # init la variable

# tant que cette boucle est vraie la page est affichee ( la fermer si exit )
while running:
    
    pygame.draw.rect(screen,(255,255,255),[0,0,5000,5000])
    
    # la page d'accueil est affichee tant que la touche entrer n'a pas ete pressee
    if not is_playing :
        # appliquer l'arrière plan de notre jeu
        background = pygame.transform.scale(background , (1080,720))
        screen.blit(background, (0, 0))
        
        # appliquer l'image des niveaux
        screen.blit(entrer, (240, 100))
        
        # appliquer l'image du joueur  
        screen.blit(joueur, (475, 400))
        

    # on commence le jeu si la touche entrer est pressee
    else:    
        # appliquer l'arrière plan de notre jeu
        background = pygame.transform.scale(background , (1080,720))
        screen.blit(background, (0, 0))
        
        # pour changer de level quand le  niveau est finie
        var_n.next_level()
        #var_n.next_level_IA()
        
        # mettre le numero du niveau à jour ( juste apres la fin du precedent niveau )
        text.update()
        # mettre le numero du niveau
        screen.blit(text.image, (350, 550))
        
    
        # création du niveau en appliquant le images et les déplacements pour l'humain
        vertical = 0
        for y in range(len(var_n.grille)):
            horizontale = 0
            vertical += 25
            for x in range(len(var_n.grille[y])):
                horizontale += 25
                image = var_n.image(var_n.grille[y][x]) # images
                image = screen.blit(image,(horizontale,vertical)) # deplacements
             
        ''' l'algo etoile se fait ici '''     
        if var_n.num_niveau == num_actuel:

            num_actuel=var_n.num_niveau+1
            grille_a_teste=copy.deepcopy(var_n.recommencer) # la grille qui est a tester
            var_etoile=Etoile(grille_a_teste)
            lst_coup=var_etoile.lst_coup() # la liste des coups a utiliser pour la resolution de l'ordi resoudre
        
        # création du niveau en appliquant le images et les déplacements pour l'IA
        vertical = 0
        for y in range(len(var_n.grille_IA)):
            horizontale = 540
            vertical += 25
            for x in range(len(var_n.grille_IA[y])):
                horizontale += 25
                image = var_n.image(var_n.grille_IA[y][x])
                image = screen.blit(image,(horizontale,vertical)) # deplacements


                
    # mettre a jour notre ecran
    pygame.display.flip()

    # si le joueur ferme une fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN :
            
            # si la touche entrer est pressee alors le jeu demarre
            if event.key == pygame.K_RETURN :
                is_playing = True
            # appeler les comandes de deplacement
            elif event.key == pygame.K_z :
                var_n.deplacement('z')
                var_n.grille_IA = var_etoile.deplacement_IA()

            elif event.key == pygame.K_s :
                var_n.deplacement('s')
                var_n.grille_IA = var_etoile.deplacement_IA()

            elif event.key == pygame.K_q :
                var_n.deplacement('q')
                var_n.grille_IA = var_etoile.deplacement_IA()

            elif event.key == pygame.K_d :
                var_n.deplacement('d')
                var_n.grille_IA = var_etoile.deplacement_IA()

            elif event.key == pygame.K_e :
                var_n.deplacement('e')
                ''' pour remmettre a 0 la map de l'IA ( ici probleme avec les caisses)
                var_etoile.num_coup = 0
                var_n.grille_IA = copy.deepcopy(var_n.recommencer_IA)
                '''