from variables import PERSO, MUR, DEST, BOX,PERSO_ON_ZONE, BOX_ON_ZONE, VIDE
import copy


map_test =[['#','#','#','#','#','#','#','#','#'],
           ['#',' ',' ',' ',' ',' ',' ',' ','#'],
           ['#',' ',' ','.','.',' ','$',' ','#'],
           ['#',' ','@','.',' ',' ',' ',' ','#'],
           ['#',' ',' ',' ','$',' ',' ',' ','#'],
           ['#',' ',' ',' ',' ',' ',' ',' ','#'],
           ['#','#','#','#','#','#','#','#','#'],]


def deplacement(map_1):
    
    # determine la position de @
    xPerso , yPerso = position(map_1)
            
    #print(xPerso, yPerso) # pour le debug
    
    dep=input('deplacez vous avec zqsd')
    
    # se deplace en haut
    if dep == 'z':
        direction(-1,0,map_1,xPerso,yPerso)

    
    # se deplace à gauche
    elif dep == 'q':
        direction(0,-1,map_1,xPerso,yPerso)
    
    # se deplace en bas
    elif dep == 's':
        direction(1,0,map_1,xPerso,yPerso)
    
    # se deplace à droite
    elif dep == 'd':
        direction(0,1,map_1,xPerso,yPerso)
        
        # pour recommencer le niveau
    elif dep == 'e':
        return True
    return False


def direction(x,y,map_1,xPerso,yPerso):
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
            map_1[xPerso+x][yPerso+y] = PERSO_ON_ZONE
            map_1[xPerso+2*x][yPerso+2*y] = BOX
        
        
        
        # deplacement du joueur sur une case avec une box avec la box vers la du vide
        elif map_1[xPerso+x][yPerso+y] == BOX and map_1[xPerso+2*x][yPerso+2*y] == VIDE and map_1[xPerso][yPerso] == PERSO: # verifie si la boite peux se deplacer
            map_1[xPerso][yPerso]= VIDE
            map_1[xPerso+x][yPerso+y] = PERSO
            map_1[xPerso+2*x][yPerso+2*y] = BOX_ON_ZONE
        
        elif map_1[xPerso+x][yPerso+y] == BOX and map_1[xPerso+2*x][yPerso+2*y] == VIDE and map_1[xPerso][yPerso] == PERSO_ON_ZONE: # verifie si la boite peux se deplacer
            map_1[xPerso][yPerso]= DEST
            map_1[xPerso+x][yPerso+x] = PERSO_ON_ZONE 
            map_1[xPerso+2*x][yPerso+2*y] = BOX_ON_ZONE 
         
        
         
        # deplacement du joueur sur une case avec une box avec la box vers la destination
        elif map_1[xPerso+x][yPerso+y] == BOX and map_1[xPerso+2*x][yPerso+2*y] == DEST and map_1[xPerso][yPerso] == PERSO: # verifie si la boite peux se deplacer
            map_1[xPerso][yPerso]= VIDE 
            map_1[xPerso+x][yPerso+y] = PERSO 
            map_1[xPerso+2*x][yPerso+2*y] = BOX_ON_ZONE 
        
        elif map_1[xPerso+x][yPerso+y] == BOX and map_1[xPerso+2*x][yPerso+2*y] == DEST and map_1[xPerso][yPerso] == PERSO_ON_ZONE: # verifie si la boite peux se deplacer
            map_1[xPerso][yPerso]= DEST
            map_1[xPerso+x][yPerso+y] = PERSO_ON_ZONE
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
            print('tu ne peux pas avancer')
        
    
    
def position(map_1):
    for y in range(len(map_1[0])):
        for x in range(len(map_1)):
            if map_1[x][y] == PERSO or map_1[x][y] == PERSO_ON_ZONE:
                    return( x, y )




# programme principale pas utile dans le main

isRunning=True
print(map_test)
etape1 = copy.deepcopy(map_test)
while isRunning == True:
    recommencer=deplacement(map_test)
    if recommencer == True :
        map_test = copy.deepcopy(etape1)
    print(map_test)


    
