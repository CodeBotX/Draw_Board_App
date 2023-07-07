import pygame
import pygame.font

class Button:
    #  Phương thức khởi tạo của lớp. Nó nhận vào các tham số như vị trí (x, y), 
    #  kích thước (width, height), màu sắc của nút và màu sắc khi nút được di chuột qua (color và hover_color), 
    #  văn bản của nút (text), màu sắc của văn bản (text_color) và font chữ (font).

    def __init__(self, x, y, width, height, color, hover_color, text, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont('Arial',(height-10))
    # Phương thức để xử lý sự kiện. .
    # Trong ví dụ này, chúng ta chỉ xử lý sự kiện nhấn chuột trái (MOUSEBUTTONDOWN) 
    # và kiểm tra xem nút có được nhấn không.
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return 1
    # Phương thức để vẽ nút lên màn hình. Chúng ta sử dụng 
    def draw(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class Button_icon:
    def __init__(self, x, y, width, height, icon_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.icon = pygame.image.load(icon_path)
        self.icon = pygame.transform.scale(self.icon, (self.rect.width, self.rect.height))


    def draw(self, screen):
        screen.blit(self.icon, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return 1