import sys
import pygame as pg


class App:
    """
    Экземпляр приложения
    """

    def __init__(self, HEIGHT: int, WIDTH: int, PIXEL_SIZE: int):
        """
        Инициализирует настройки экрана, библеотеку pygame
        :param HEIGHT: Высота окна в пикселях
        :param WIDTH: Ширина окна в пикселях
        :param PIXEL_SIZE: Размер игрового пикселя в пикселях
        """
        pg.init()

        # Инициализация окна
        self.icon = pg.image.load('images/icon/icon_app.png')
        self.WINDOW = pg.display.set_mode((HEIGHT, WIDTH))
        pg.display.set_icon(self.icon)
        pg.display.set_caption('Пинг Понг')

        # Управление производителностью
        self.clock = pg.time.Clock()
        self.FPS = 60


    def run(self):
        """
        Основной цикл приложения
        :return: None
        """
        while True:
            self.__check_event()
            self.__draw()
            self.clock.tick(self.FPS)

    def __draw(self):
        """
        Отрисовывает все, что происходит в окне
        :return: None
        """
        self.WINDOW.fill((155, 155, 155))


    def __check_event(self):
        """
        Отслеживает нажатые клавиши
        :return: None
        """
        [sys.exit() for event in pg.event.get() if event.type == pg.QUIT]

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_w]:
            print('w')
        if keys_pressed[pg.K_a]:
            print('a')
        if keys_pressed[pg.K_s]:
            print('s')
        if keys_pressed[pg.K_d]:
            print('d')

        if keys_pressed[pg.K_UP]:
            print('up')
        if keys_pressed[pg.K_DOWN]:
            print('down')
        if keys_pressed[pg.K_LEFT]:
            print('left')
        if keys_pressed[pg.K_RIGHT]:
            print('right')



if __name__ == '__main__':
    app = App(900, 900, 1)
    app.run()
