class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_picture(self):
        chart = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for y in range(self.height):
            for x in range(self.width):
                chart += "*"
            chart += "\n"
        return chart

    def get_amount_inside(self, anotherShape):
        return int(self.get_area() / anotherShape.get_area())


class Square(Rectangle):
    def __init__(self, line):
        super().__init__(line, line)
    
    def __repr__(self):
        return "Square(side={})".format(self.width)

    def set_side(self, l):
        self.width = l
        self.height = l