from variables import PERSO , MUR , DEST , BOX , BOX_ON_ZONE , PERSO_ON_ZONE , VIDE # * pour tous les elements
import copy
from niveau import Niveau

class Noeud ( Niveau):
    def __init__(self, parent):
        self.current_field=[] # version de la map 
        self.cout = 0
        self.parent = parent # parent direct
        
        if parent != None :
            self.cout=self.parent.cout+1  # le cout deja depense
            self.current_field=self.parent.current_field # juste pour test 
        
        self.map_alternative=copy.deepcopy(self.current_field) # permet verif des trucs sans modifier current_field
        self.cout_theorique=self.valeur_proba_win() # ligne droite nobre de cout theorique pour finir
        self.cout_total = self.cout+self.cout_theorique
        self.direction_dep = None # la direction dans laquel on s est deplace
        
        self.str_grille=""
    
        
    
    ''' creer un str à partir de la grille afin que la comparais on se fasse plus facilement/rapidement '''
    
    def grille_str(self, grille):
        str_grille=""
        for ligne in grille :
            for casse in ligne :
                str_grille+=str(casse)
        return str_grille
                
                
        
        
    '''determine les positions des elements importants'''
    
    def position_perso(self):
        
        if self.current_field != None :
            if len(self.current_field) != 0 :
                if len(self.current_field[0]) != 0 :
                    for y in range(len(self.current_field[0])):
                        for x in range(len(self.current_field)):
                            if self.current_field[x][y] == PERSO or self.current_field[x][y] == PERSO_ON_ZONE:
                                        return( x, y )
    
    def position_box(self, map_1):
        pos_box=[]
        if len(map_1) != 0 :
            for y in range(len(map_1[0])):
                for x in range(len(map_1)):
                    if map_1[x][y] == BOX or map_1[x][y] == BOX_ON_ZONE:
                        pos_box.append((x,y))
        return ( pos_box )
    
    def position_dest(self, map_1): # renvoie une liste des positions des destinations
        pos_dest=[]
        for y in range(len(map_1[0])):
            for x in range(len(map_1)):
                if map_1[x][y] == DEST or map_1[x][y] == PERSO_ON_ZONE:
                    pos_dest.append([x,y])
        return ( pos_dest )
    
    def box_closer(self): # determine la distance avec la boite la plus proche
        perso = self.position_perso()
        liste_box = self.position_box(self.current_field)
        if len(liste_box) != 0 :
            dist = self.distance (liste_box[0], perso)
            for nb in range(len(liste_box)):
                dist_alternative = self.distance (liste_box[nb], perso)
                #print(dist_alternative, 'alter')
                if dist > dist_alternative :
                    
                    dist = dist_alternative
                    #print(dist , 'dist')
            return (dist)    
    
    
    '''determine la distance entre 2 objets'''
    
    def distance(self, boite, dest_or_perso):
        return ( abs(boite[0]-dest_or_perso[0]) + abs(boite[1]-dest_or_perso[1]))                    
    
        
    ''' determine une liste des distances les plus courtes entre les boites et les destinations '''
        
    def coups_box_unique(self, box, map_1): 
        dest = self.position_dest(map_1)
        dist = 0
        if len(dest) != 0 :
            dist = self.distance (box, dest[0])
            indice=0
            for nb in range(len(dest)):
                dist_alternative = self.distance (box, dest[nb])
                if dist > dist_alternative :
                    dist = dist_alternative
                    indice=nb
                    
            [ vide_x , vide_y ] = dest[ indice ]
            self.map_alternative[vide_x][vide_y] = VIDE
        return(dist)
    
    def coups_box_all(self, grille):
        position_box = self.position_box(grille)
        liste_coups=[]
        self.map_altenative = copy.deepcopy(grille)
        for i in range(len(position_box)):
            liste_coups.append(self.coups_box_unique(position_box[i],self.map_alternative))
        self.map_alternative 
        return(liste_coups)
    
    
    '''determine une liste des valeurs de probabiliter pour le noeud ( heuristuque ) '''
 
    def valeur_proba_win(self):
        somme=0
        for i in range(len(self.coups_box_all(self.current_field))):
            somme+= self.coups_box_all(self.current_field)[i]
        if self.box_closer() == None:
            return(somme)
        return (self.box_closer()+somme)
    
    def theorique(self):
        self.cout_theorique=self.valeur_proba_win()
        return self.cout_theorique
        
    def heuristique(self):
        self.cout_heuristique = self.cout+self.cout_theorique
        return self.cout_heuristique
    
    def direction(self, x, y):
        
        xPerso , yPerso = self.position_perso()
        
        map_1=copy.deepcopy(self.current_field)
        
        
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
        
        return(map_1)
    
    
    
    
    
    