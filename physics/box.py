import pygame


class Box:
    def __init__(self, coords_display, parameters):
        self.coords = coords_display[0]
        self.display = coords_display[1]
        self.forces = []
        self.parameters = parameters
        # self.parameters = {"mass":,
        #                    "speed":,
        #                    "side area":,} # трение об воздух будет зависеть от длины поверхности (ну типа площади в 2д), угла и скорости. Надо будет подрегуллировать
        #                    # дополнять этот список по мере необходимости

    def apply_force(self, amount):
