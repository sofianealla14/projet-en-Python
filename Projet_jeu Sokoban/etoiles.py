# from niveau import Niveau
from variables import PERSO , MUR , DEST , BOX , BOX_ON_ZONE , PERSO_ON_ZONE , VIDE # * pour tous les elements
import copy
from noeud import Noeud
#from niveau import Niveau
from deplacement_algo import direction

            # 0   1   2   3   4   5   6   7   8   9   10
map_test = [['#','#','#','#','#','#','#','#','#','#','#'],  #0
            ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],  #1
            ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],  #2
            ['#',' ',' ',' ',' ','$',' ',' ',' ',' ','#'],  #3
            ['#',' ',' ',' ',' ','.',' ',' ',' ',' ','#'],  #4
            ['#',' ','@',' ','$',' ',' ',' ','.',' ','#'],  #5
            ['#',' ','$',' ','.',' ',' ',' ',' ',' ','#'],  #6
            ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],  #7
            ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],  #8
            ['#','#','#','#','#','#','#','#','#','#','#']] #9


class Etoile() :
    
    def __init__(self, terrain ):
        
        self.open_lst=[Noeud(None)] # liste des noeud utilisable init avec un noeud sans parent car c'est l "encetre" de tt les noeuds
        self.map_IA=terrain # de base la grille e l'ia a T0 est la grille de base
        self.closed_lst=[] # liste des noeud deja visite
        
        self.open_lst[0].current_field = terrain
        self.open_lst[0].grille = self.open_lst[0].current_field
        self.open_lst[0].map_alternative = copy.deepcopy(self.open_lst[0].current_field)
        self.open_lst[0].cout_theorique = self.open_lst[0].valeur_proba_win()
        self.open_lst[0].cout = 0
        self.open_lst[0].cout_heuristique = self.open_lst[0].cout_theorique
        
        self.num_coup=0
        self.start()


    def affiche(self, grille):
        affichage = ""
        for i in grille:
            for j in i:
                affichage += str(j + "|")
            affichage += "\n"
        print(affichage)


    def start(self):
        
            while len(self.open_lst) != 0 :
                
                #print(self.dernier_noeud())
                #self.affiche(self.open_lst[-1].current_field)
                print(self.open_lst[-1].heuristique())
                self.nouveau_noeud()
                if self.dernier_noeud() :
                    print("il y a une solution")
                    return self.dernier_noeud()
            print("il n'y a pas de solutions")
            return None


    def grille_str(self, grille):
        str_grille=""
        for ligne in grille :
            for casse in ligne :
                str_grille+=str(casse)
        return str_grille



    '''comparer le cout total de 2 noeud retourne le celui qui a le plus petit n'estplus utilise mais interessant quand meme '''
    
    def comparer_deux_noeud( self, noeud_1, noeud_2 ): # comparer les coup totaux
        if noeud_1.cout_heuristique <= noeud_2.cout_heuristique :
            lequel=noeud_1
        else:
            lequel=noeud_2
        return lequel
    
    '''determine le noeud avec le " cout total " le plus petit '''
    
    def cout_le_plus_petit(self):
        plus_petit=self.open_lst[0]
        for i in self.open_lst :
            if i.heuristique() < plus_petit.heuristique() :
                plus_petit=i

        return plus_petit
    
    
    '''cree un nouveau noeud a partir d un noeud parent deja existant '''
    
    
    def nouveau_noeud(self):
        plus_petit = self.cout_le_plus_petit()
        
        noeud_du_haut=Noeud(plus_petit)
        haut=copy.deepcopy(plus_petit).direction(-1,0)
        noeud_du_haut.direction_dep=(-1,0)
        self.ajouter(noeud_du_haut,haut)

        
        noeud_du_bas=Noeud(plus_petit)
        bas=copy.deepcopy(plus_petit).direction(1,0)
        noeud_du_bas.direction_dep=(1,0)
        self.ajouter(noeud_du_bas,bas)

            
        
        noeud_de_gauche=Noeud(plus_petit)
        gauche=copy.deepcopy(plus_petit).direction(0,-1)
        noeud_de_gauche.direction_dep=(0,-1)
        self.ajouter(noeud_de_gauche,gauche)

        
        
        noeud_de_droite=Noeud(plus_petit)
        droite=copy.deepcopy(plus_petit).direction(0,1)
        noeud_de_droite.direction_dep=(0,1)
        self.ajouter(noeud_de_droite,droite)

        
        
        self.closed_lst.append(plus_petit.str_grille)
        self.open_lst.remove(plus_petit)
        return
    
    
    def ajouter(self, nouveau_noeud , grille):
        nouveau_noeud.current_field=grille
        nouveau_noeud.str_grille=nouveau_noeud.grille_str(grille)
        if self.verif(nouveau_noeud , grille):
            self.open_lst.append(nouveau_noeud)
            

        
        
    
    '''verifie si le noeud est deja visite et si il est utilisable'''
    
    def verif(self, nouveau_noeud , grille ):
        
        for i in self.open_lst:
            #if i.current_field == grille:
            if i.str_grille == nouveau_noeud.str_grille :
                return False   
        for i in self.closed_lst :
            #if i.current_field == grille:
            if i == nouveau_noeud.str_grille :
                return False
        if self.utilisable(nouveau_noeud, grille) == False :
            self.closed_lst.append(nouveau_noeud.str_grille)
            return False
        return True
    
    
    ''' determine si le noeud est utilisables cad qu'on ne reste pas bloquer dessus '''
    
    
    def utilisable_opsolete(self, nouveau_noeud): #permiere version pour rendre le programme plus rapide, cause qq problemes, laisse car interessante mais inutilisable et inutilise
        grille=nouveau_noeud.current_field
        for pos in nouveau_noeud.position_box(grille) :

            y=pos[0]
            x=pos[1]
            if grille != None and grille != [] and x < len(grille) and y < len(grille[0]) :
                if grille[x][y] == BOX: # inutile de verifier les BOX_ON_ZONE
                    
                    if ( grille[x-1][y]==MUR and ( grille[x][y-1]==MUR or grille[x][y+1] ) ) or ( grille[x+1][y]==MUR and ( grille[x][y-1]==MUR or grille[x][y+1] ) ):
                        
                        print(grille)
                        return False
    
    
    def utilisable(self, nouveau_noeud, grille):
        #grille=nouveau_noeud.current_field
        
        
        # rajout de la V2
        
        for x in range(len(grille)):
            for y in range(len(grille[0])):
                if grille[x][y]==BOX :
                    for var_devant in [-1,1]:
                        if grille[x+var_devant][y] == MUR:
                            for var_coter in [-1,1]:
                                if  grille[x][y+var_coter] in [ MUR , BOX , BOX_ON_ZONE ] :
                                    if grille[x][y+var_coter] in [ BOX , BOX_ON_ZONE ] :
                                        if grille[x+var_devant][y+var_coter] == MUR :
                                            return False
                                    elif grille[x][y+var_coter] == MUR :
                                        return False
                            
                        if grille[x][y+var_devant] == MUR:
                            for var_coter in [-1,1]:
                                if  grille[x+var_coter][y] in [ MUR , BOX , BOX_ON_ZONE ] :
                                    if grille[x+var_coter][y] in [ BOX , BOX_ON_ZONE ] :
                                        if grille[x+var_coter][y+var_devant] == MUR :
                                            return False
                                    elif grille[x+var_coter][y] == MUR :
                                        return False
        #fin rajout de la V2
        
        
        
        pos_perso=nouveau_noeud.position_perso()
        x,y=pos_perso
        
        direction_x = 0
        direction_y = 0
        is_wall=True
        
        direction_x,direction_y=nouveau_noeud.direction_dep
        
        if direction_x != 0 :
            if grille[x+direction_x][y] == BOX :
                
                for i in grille[x+2*direction_x] :
                    if i != MUR :
                        is_wall = False
                        
                if is_wall :
                    for i in grille[x+direction_x]:
                        if i == DEST:
                            return True
                    
                    return False
         
                
                    
                
        
        if direction_y != 0 :
            if grille[x][y+direction_y] == BOX :
                
                for i in grille:
                    if i[y+2*direction_y] != MUR :
                        is_wall = False
                        
                if is_wall :
                    for i in grille:
                        if i[y+direction_y] == DEST:
                            return True
                    
                    return False
                

        
        return True
 
    
    
    
    
    
    '''determine si un noeud est le dernier '''
    
    def dernier_noeud(self):
        if len(self.open_lst)!=0:
            if len(self.open_lst) <= 4:
                for i in self.open_lst :
                    if self.is_finish(i.current_field):
                    
                        return i
            else:
                for i in [-1,-2,-3,-4]: # permet de ne pas reverifier les map deja test et donc gagner en vitesse
                    if self.is_finish(self.open_lst[i].current_field):
                    
                        return self.open_lst[i]
        return None
    
    def is_finish(self, grille):
        
        for ligne in grille :
            for c in ligne :
                if c == DEST or c == PERSO_ON_ZONE :
                    return False
        return True
    
    
    ''' determine une liste avec les coups que l ordi va devoir faire pour resoudre la map'''
    
    def lst_coup(self):
        i=self.dernier_noeud()
        lst_direction=[] # la liste des coups
        if i==None:
            return []
        while i.parent :
            lst_direction.insert( 0 , i.direction_dep )
            i=i.parent
       
        return(lst_direction)
    

    def deplacement_IA (self) :
        
        
        lst_coup=self.lst_coup()
        if lst_coup != None : # peut etre nul si il n'y a pas de solutions
            if self.num_coup < len(lst_coup) :
                
                axe_x,axe_y = lst_coup[self.num_coup]
                self.map_IA = direction( axe_x, axe_y , self.map_IA)

                self.num_coup+=1
                return self.map_IA
            return self.map_IA
        return None