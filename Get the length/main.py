from rect import *

Width, Height = 1000, 600
Center = (Width // 2, Height // 2)
Image_path = "test.png"
Red = (255, 0, 0)
Rectangles = []

dx, dy, dw, dh, dtheta = 6, 6, 6, 2, 2

def initialize():
    pygame.init()
    scrn = pygame.display.set_mode((Width, Height))
    scrn.fill(pygame.Color('darkslategray'))
    pygame.display.set_caption('image')
    return scrn


scrn = initialize()

img = pygame.image.load(Image_path).convert()

img_dim = (img.get_width(), img.get_height())

img_start_Pos = (Center[0] - (img_dim[0] // 2), Center[1] - (img_dim[1] // 2))

rect_x = 30
rect_y = 30
rect_w = 60
rect_h = 10
std_rectangle = Rectangle(rect_x, rect_y, rect_w, rect_h, Red)
last_rect = std_rectangle
Rectangles.append(std_rectangle)


def scrn_update():

    scrn.fill(pygame.Color('darkslategray'))
    scrn.blit(img, img_start_Pos)
    for rectangle in Rectangles:
        rectangle.draw(scrn)
    pygame.display.flip()
    


# Flag to indicate whether the rectangle is being dragged
dragging = False
input  = False
status = True

while status:
    scrn_update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # input  = True
                for rectangle in Rectangles:
                    if rectangle.collidepoint(event.pos):
                        dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle.rect.x - mouse_x
                        offset_y = rectangle.rect.y - mouse_y
                        last_rect = rectangle
            elif event.type == pygame.MOUSEBUTTONUP:
                input  = False
                dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    last_rect.drop(mouse_x + offset_x, mouse_y + offset_y)
            elif event.type == pygame.KEYDOWN:

                if input:
                    if event.key == pygame.K_BACKSPACE: 
                        last_rect.text = last_rect.text[:-1]  
                    if event.key == pygame.K_DELETE: 
                        last_rect.text = ''  
                    else:
                        last_rect.text += event.unicode

                if event.key == pygame.K_d:
                    last_rect.change_width(dw)   # Increase width by 5 pixels
                elif event.key == pygame.K_a:
                    last_rect.change_width(-dw)  # Decrease width by 5 pixels
                elif event.key == pygame.K_w:
                    last_rect.change_height(dh)   # Increase height by 5 pixels
                elif event.key == pygame.K_s:
                    last_rect.change_height(-dh)  # Decrease height by 5 pixels
                elif event.key == pygame.K_q:
                    last_rect.change_angle(dh)   
                elif event.key == pygame.K_e:
                    last_rect.change_angle(-dh)
                elif event.key == pygame.K_RIGHT:
                    last_rect.move(dx, 0) 
                elif event.key == pygame.K_LEFT:
                    last_rect.move(-dx, 0)  
                elif event.key == pygame.K_UP:
                    last_rect.move(0, -dy) 
                elif event.key == pygame.K_DOWN:
                    last_rect.move(0, dy)   
                elif event.key == pygame.K_PAGEUP:
                    dtheta += 1
                    dx = dy = dw = dtheta * 3
                    dh = dtheta 
                  
                elif event.key == pygame.K_PAGEDOWN:
                    if dtheta != 0:
                        dtheta -= 1
                        dx = dy = dw = dtheta * 3
                        dh = dtheta 
                
                elif event.key == pygame.K_n:
                    new_rectangle = Rectangle(rect_x, rect_y, rect_w, rect_h, Red)
                    Rectangles.append(new_rectangle)
                elif event.key == pygame.K_p:
                    last_rect.print()
                
                


pygame.quit()
