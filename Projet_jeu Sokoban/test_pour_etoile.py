import pygame
from niveau import Niveau
from etoiles import Etoile


            # 0   1   2   3   4   5   6   7   8   9   10
map_test = [['#','#','#','#','#','#','#','#','#','#','#'],  #0
            ['#',' ',' ','#','#','#','#','#',' ',' ','#'],  #1
            ['#',' ',' ','#',' ',' ',' ','#',' ',' ','#'],  #2
            ['#',' ',' ','#',' ','$',' ','#','#','#','#'],  #3
            ['#','#','#','#',' ','.',' ','#','#','#','#'],  #4
            ['#',' ','@',' ','$',' ',' ',' ','.','#','#'],  #5
            ['#',' ','$',' ','.','#','#','#','#','#','#'],  #6
            ['#','#','#','#','#','#','#',' ',' ',' ','#'],  #7
            ['#',' ',' ',' ',' ',' ','#',' ',' ',' ','#'],  #8
            ['#','#','#','#','#','#','#','#','#','#','#']] #9



var_n=Niveau()


# commencer_nouvel_etoile=map_test.next_level()
# if commencer_nouvel_etoile is True :
#var_n.grille=var_n.recommencer=map_test
var_etoile=Etoile(map_test)
#print(var_n.grille)
var_etoile.start()
print (var_etoile.open_lst[0].position_box(var_etoile.open_lst[0].current_field))
print (var_etoile.lst_coup())