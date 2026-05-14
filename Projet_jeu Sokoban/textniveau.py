import pygame

class TextNiveau(pygame.sprite.Sprite):
    def __init__(self, var_n):
        super().__init__()
        self.niveau = var_n
        self.update()
    
    def update (self) :
        if self.niveau.num_niveau < 10 :
            self.image = pygame.Surface((250,100))
        elif self.niveau.num_niveau >= 10 :
            self.image = pygame.Surface((290,100))
        self.image.fill((255,255,255))
        font_type = 'ressources/police/Patiska.ttf'
        color , size, x , y = ((200, 000, 000), 90 , 20 , 20 )
        myfont = pygame.font.SysFont(font_type, size)
        text = str("Level "+str(self.niveau.num_niveau))
        textsurface = myfont.render(text, False, color)
        text = self.image.blit(textsurface,(x,y))