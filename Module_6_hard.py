import math
class Figure:
    sides_count = 0
    def __init__(self,color,filled,*sides):
        self.__sides = [*sides]
        if self.set_color(*color):
            self.__color = color
        else:
            self.color = [0,0,0]
        self.filled = filled
    def get_color(self):
        return self.__color
    def __is_valid_color(self,r, g, b,):
        if isinstance(r, int) and isinstance(g,int) and isinstance(b, int):
            if r <= 255 and g <= 255 and b <= 255 and r >= 0 and g >= 0 and b >= 0:
                return True
    def set_color(self,r, g, b,):
        if self.__is_valid_color(r,g,b,):
            self.__color = [r,g,b]
    def __is_valid_sides(self,*args):
        if len(args) == self.sides_count:
            valid_side = True
            for i in args:
                if isinstance(i,int) and i > 0:
                    continue
                else:
                    valid_side = False
            return valid_side
        else:
            return False
    def get_sides(self):
        return self.__sides
    def set_sides(self,*new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = []
            for side in new_sides:
                self.__sides.append(side)
    def __len__(self):
        return  sum(self.__sides)
class Circle(Figure):
    sides_count = 1
    def __init__(self,color,*sides,filled=True):
        if len(sides) != self.sides_count:
            sides = []
            for i in range(self.sides_count):
                sides.append(1)
        super().__init__(color,filled, *sides)
    def __radius(self):
        radius = self.get_sides()[0]/2/math.pi
        return radius
    def get_square(self):
        return math.pi * (self.__radius()**2)
class Triangle(Figure):
    sides_count = 3
    def __init__(self,color,*sides,filled=True):
        if len(sides) != self.sides_count:
            sides = []
            for i in range(self.sides_count):
                sides.append(1)
        super().__init__(color,filled, *sides)
    def get_square(self):
        p = self.__len__()/2
        s = (p*(p - self.get_sides()[0])*(p-self.get_sides()[1])*(p-self.get_sides()[2])) ** 0.5
        return s
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides, filled=True):
        if len(sides) == 1:
            side_ = []
            for i in range(self.sides_count):
                side_.append(*sides)
            sides = side_
        else:
            sides = []
            for i in range(self.sides_count):
                sides.append(1)
        super().__init__(color, filled, *sides)
    def get_volume(self):
        return self.get_sides()[0] ** 3



if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())




