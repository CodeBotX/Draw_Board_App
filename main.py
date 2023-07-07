import pygame
import pygame.font
from pygame.locals import *
from drawing import Draw
from button import Button,Button_icon
# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ Pygame
width, height = 1200, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Board App")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
VIOLET = (238,130,238)
light_pink = (255,182,193)
GRAY = (128,128,128)
font= pygame.font.SysFont('Latin Modern Math',40)
mouse=[]
status_eraser = False
status_pen = True

status_color = 0
draw_tool = Draw()
status_draw = False

# Vòng lặp chính
running = True
while running:
    # Cập nhật giao diện
    screen.fill(light_pink)  
    #  lấy tọa độ chuột
    mouse_x, mouse_y = pygame.mouse.get_pos()
    Pos = [mouse_x,mouse_y]
    text_mouse = font.render(f"{mouse_x} {mouse_y}", True, BLACK)
    # Vẽ các thành phần giao diện và các đường vẽ lên màn hình
    button_color = Button(1015, 190, 150, 50, BLACK, GRAY, "COLOR", WHITE)
    button_color.draw(screen)  
    button_Delete = Button(1015, 270, 150, 50, BLACK, GRAY, "DELETE", WHITE)
    button_Delete.draw(screen)  
    button_Size_Plus = Button(1015, 350, 50, 50, BLACK, GRAY, "+", WHITE)
    button_Size_Plus.draw(screen)
    button_Size_Minus = Button(1115, 350, 50, 50, BLACK, GRAY, "-", WHITE)
    button_Size_Minus.draw(screen)
    button_Logo = Button(1015, 600, 150, 40, BLACK, BLACK, "MINH TIEN", WHITE)
    button_Logo.draw(screen)
    
    pygame.draw.rect(screen,WHITE,(20,20,950,650))
    pygame.draw.rect(screen,GRAY,(1002,17,186,136))
    pygame.draw.rect(screen,draw_tool.return_color_draw(),(1005,20,180,130))
    # screen.blit(text_mouse,(10,10))
    button_pen = Button_icon(1015, 450, 50, 50, 'icon\pen.png')
    button_pen.draw(screen)
    button_eraser = Button_icon(1115, 450, 50, 50, 'icon\eraser.png')
    button_eraser.draw(screen)

    button_color_0 = Button(1005, 20, 60, 65, (0,0,0),(0,0,0) , "", WHITE)
    button_color_1 = Button(1065, 20, 60, 65, (255,0,0),(255,0,0) , "", WHITE)
    button_color_2 = Button(1125, 20, 60, 65, (0,255,0),(0,255,0) , "", WHITE)
    button_color_3 = Button(1005, 85, 60, 65, (0,0,255),(0,0,255) , "", WHITE)
    button_color_4 = Button(1065, 85, 60, 65, (255,255,0),(255,255,0) , "", WHITE)
    button_color_5 = Button(1125, 85, 60, 65, (0,255,255),(0,255,255) , "", WHITE)
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # xử lý các phím chức năng
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Xử lý sự kiện chuột nhấn
            if button_color.handle_event(event)== 1:
                status_color = True
            if status_color == True:
                if button_color_0.handle_event(event)== 1:
                    draw_tool.set_color(0)
                    status_color = False
                elif button_color_1.handle_event(event)== 1:
                    draw_tool.set_color(1)
                    status_color = False
                elif button_color_2.handle_event(event)== 1:
                    draw_tool.set_color(2)
                    status_color = False
                elif button_color_3.handle_event(event)== 1:
                    draw_tool.set_color(3)
                    status_color = False
                elif button_color_4.handle_event(event)== 1:
                    draw_tool.set_color(4)
                    status_color = False
                elif button_color_5.handle_event(event)== 1:
                    draw_tool.set_color(5)
                    status_color = False
                else:
                    status_color = True
            elif button_Delete.handle_event(event) == 1:
                draw_tool.delete()
            elif button_Size_Minus.handle_event(event)==1:
                draw_tool.set_size(0)
            elif button_Size_Plus.handle_event(event) == 1:
                draw_tool.set_size(1)
            button_Logo.handle_event(event)
            if button_eraser.handle_event(event) == 1:
                status_eraser=True
                status_pen=False
                # status_draw=False
                draw_tool.eraser()
            if button_pen.handle_event(event)== 1:
                status_pen = True
                status_eraser=False
            elif event.button == 1:
                status_draw = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:  
                status_draw = False


    #Vẽ 

    if status_color == True:
        button_color_0.draw(screen)
        button_color_1.draw(screen)
        button_color_2.draw(screen)
        button_color_3.draw(screen)
        button_color_4.draw(screen)
        button_color_5.draw(screen)

    if status_draw == True:
        if 23<mouse_x<967 and 23<mouse_y<667:
            draw_tool.drawing(Pos)

        
    draw_tool.draw(screen)
    # khi bấm nút eraser
    if status_eraser == True:
        mouse=[]
        x=[mouse_x-5,mouse_y-25]
        mouse.append(x)
        eraser = pygame.image.load('icon/eraser.png')
        eraser = pygame.transform.scale(eraser, (30, 30))
        for i in range (len(mouse)):
            screen.blit(eraser, (mouse[i][0], mouse[i][1]))
    
    if status_pen == True:
        mouse=[]
        x=[mouse_x-5,mouse_y-25]
        mouse.append(x)
        pen = pygame.image.load('icon/pen.png')
        pen = pygame.transform.scale(pen, (30, 30))
        for i in range (len(mouse)):
            screen.blit(pen, (mouse[i][0], mouse[i][1]))

    pygame.display.flip()  # Hiển thị màn hình
# Kết thúc Pygame
pygame.quit()
