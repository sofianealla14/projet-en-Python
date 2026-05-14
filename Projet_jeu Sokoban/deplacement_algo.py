#import keyboard
from variables import PERSO , MUR , DEST , BOX , BOX_ON_ZONE , PERSO_ON_ZONE , VIDE

            # 0   1   2   3   4   5
map_1 = [['#','#','#','#','#','#'], #0
         ['#',' ',' ',' ',' ',' '], #1
         ['#',' ',' ',' ',' ',' '], #2
         ['#','@',' ','$','.',' '], #3
         ['#',' ',' ',' ',' ','.'], #4
         ['#',' ',' ',' ',' ',' ']] #5

liste_test =[(0,1),(0,1)]

def position(map_1):
    for y in range(len(map_1[0])):
        for x in range(len(map_1)):
            if map_1[x][y] == PERSO or map_1[x][y] == PERSO_ON_ZONE:
                return( x, y )
                    
def direction(x,y, map_1): # reste probleme dans de conflict pas regle ( niveau 3 )
        xPerso , yPerso = position(map_1)
        
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
        
        
        return map_1

def deplacement_algo(liste,dep_algo=True):
    n=0
    while n < len(liste):
        if dep_algo :
            
            x,y = liste[n]
            direction(x,y)
            print(map_1)
            n += 1
                
#deplacement_algo(liste_test)