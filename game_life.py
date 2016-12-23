import pygame
from pygame.locals import *
import random


class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):              # по ширине с шагом размера ячейки
            pygame.draw.line(self.screen, pygame.Color('black'),    # поверхность - экран, цвет - чёрный,
                             (x, 0), (x, self.height))              # стартовая позиция и конечная
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self):
        pygame.init()                                               # инициализация всех модулей pygame
        clock = pygame.time.Clock()                                 # создание объекта для отслеживания времени
        pygame.display.set_caption('Game of Life')                  # установить заголовок окна
        self.screen.fill(pygame.Color('white'))                     # заполнить поля белым цветом
        c_list = self.cell_list(randomize=True)
        self.draw_cell_list(c_list)
        running = True
        while running:
            for event in pygame.event.get():                        # для каждого события из полученных
                if event.type == QUIT:                              # если событие завершилось, то конец
                    running = False
            c_list = self.update_cell_list(c_list)
            self.draw_cell_list(c_list)
            self.draw_grid()
            pygame.display.flip()                                   # обновляем полную поверхность дисплея
            clock.tick(self.speed)                                  # обновляем время
        pygame.quit()                                               # закрываем модули

    def cell_list(self, randomize=False):
        if randomize is True:
            cell_matrix = []
            for i in range(self.cell_height):
                row_matrix = []
                for j in range(self.cell_width):
                    row_matrix.append(random.randrange(0, 2, 1))
                cell_matrix.append(row_matrix)
        return cell_matrix

    def draw_cell_list(self, rects):
        y = 0
        for row in rects:
            x = 0
            for cell in row:
                if cell == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (x, y, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size))
                x += self.cell_size
            y += self.cell_size

    def get_neighbours(self, cell):
        x, y = cell
        neighbours = [(x + i, y + j)
                      for i in range(-1, 2)
                      for j in range(-1, 2)
                      if not i == j == 0]
        return neighbours

    def update_cell_list(self, cell_list):
        new_cell_matrix = []
        for i in range(self.cell_height):
            new_row_matrix = []
            for j in range(self.cell_width):
                neighbours = self.get_neighbours((i, j))
                count_alive = 0
                for neighbour in neighbours:
                    p, l = neighbour
                    if 0 <= p < self.cell_height and 0 <= l < self.cell_width:
                        if cell_list[p][l] == 1:
                            count_alive += 1
                if cell_list[i][j] == 1 and (count_alive == 2 or count_alive == 3):
                    new_row_matrix.append(1)
                elif cell_list[i][j] == 0 and count_alive == 3:
                    new_row_matrix.append(1)
                else:
                    new_row_matrix.append(0)
            new_cell_matrix.append(new_row_matrix)
        return new_cell_matrix


if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()
