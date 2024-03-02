import pygame


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.theta = 0
        self.image = pygame.Surface((width , height)) 
        self.image.fill(color)
        self.image.set_colorkey(pygame.Color('darkslategray')) 
        self.rect = self.image.get_rect()  
        self.rect.center = (x + width//2, y + height//2)
        self.text = ''
      
    def draw(self, screen):
        old_center = self.rect.center

        self.image = pygame.Surface((self.width , self.height))
        self.image.fill(self.color)
        self.image.set_colorkey(pygame.Color('darkslategray')) 
        self.image = pygame.transform.rotate(self.image , self.theta)  

        self.rect = self.image.get_rect()  
        self.rect.center = old_center

        base_font = pygame.font.Font(None, 32) 
        text_surface = base_font.render(self.text, True, (255, 255, 255)) 

        screen.blit(self.image, self.rect)
        screen.blit(text_surface, self.rect)

    def drop(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)

    def change_width(self, dw):
        self.width += dw

    def change_height(self, dh):
        self.height += dh

    def change_angle(self, dtheta):
        self.theta += dtheta
        self.theta %= 360

    def print(self):
        print(f"width: {self.width}, height: {self.height}, real width: {self.text}")

