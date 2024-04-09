# ToDo task 3: Создать класс Point, который представляет собой точку в двумерном пространстве.
#  Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки,
#  а также для получения и изменения координат.

class Point:
    def __init__(self, x: int, y: int):
        assert isinstance(x, int) and isinstance(y, int)
        self.x = x
        self.y = y

    def get_distance(self, to: "Point") -> float:
        assert isinstance(to, Point)
        return ((to.x - self.x) ** 2 + (to.y - self.y) ** 2) ** 0.5

    def get_coordinates(self) -> tuple[int, int]:
        return self.x, self.y

    def set_coordinates(self, x: int, y: int) -> None:
        assert isinstance(x, int) and isinstance(y, int)
        self.x, self.y = x, y
