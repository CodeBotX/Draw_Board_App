#Module này chứa các hàm và lớp liên quan đến việc vẽ trên bảng, bao gồm:

# Hàm để vẽ đường cong hoặc đường thẳng trên bảng.
# Lớp để lưu trữ các đường vẽ đã được tạo ra và quản lý chúng.
import pygame
black = (0, 0, 0)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
aqua = (0, 255, 255)
purple = (128, 0, 128)

class Draw:
    # phương thức khởi tạo
    def __init__(self):
        self.colors = [black, red, lime, blue, yellow, aqua, purple,(255,255,255)]
        self.points = []
        self.lable = []
        self.index_color = 0
        self.size = 6
    # Phương thức được gọi khi bắt đầu vẽ. Nó thêm điểm đầu tiên (pos) vào danh sách self.points.
    def drawing(self, pos):
        self.lable.append(self.index_color)
        self.points.append(pos)
   
    def delete(self):
        self.points=[]
        self.lable=[]
    def return_color_draw(self):
        return self.colors[self.index_color]
    def set_color(self, index):
        if 0 <= index < len(self.colors):
            self.index_color = index
    def set_size(self, index):
        if index == 1:
            if self.size <10:
                self.size = self.size + 1
        elif index == 0:
            if self.size >6:
                self.size = self.size - 1
    def draw(self, surface):
        if len(self.points) > 1:
            for i in range(len(self.points)):
                pygame.draw.circle(surface, self.colors[self.lable[i]], (self.points[i][0], self.points[i][1]),self.size)

    def eraser (self):
        self.index_color = 7

    