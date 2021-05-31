class Matrix2x2:
    def __init__(self, x00, x01, x10, x11):
        self.x00 = x00
        self.x01 = x01
        self.x10 = x10
        self.x11 = x11
        self.A = [[self.x00, self.x01], [self.x10, self.x11]]

    def __str__(self):
        """
        Prints out the nice string representation of the matrix
        :return:
        """
        print(('\n'.join(['|'.join([str(cell) for cell in row]) for row in self.A])))

    def determinant(self):
        """
        calculates the determinant of a 2D matrix using th
        det(A) = ad - bc
        :return:
        """
        return self.A[0][0] * self.A[1][1] - self.A[0][1] * self.A[1][0]

    def transpose(self):
        """
        Rearranges the values in the matrix to rearrange the rows and columns
        :return:
        """
        result = [[0, 0],
                  [0, 0]]

        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                result[j][i] = self.A[1 - i][1 - j]

        return result


class GRectangle:
    def __init__(self, x, y, width, height, linecolor, fillcolor):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        self.linecolor = linecolor
        self.fillcolor = fillcolor
        pass


class GPanel(GRectangle):
    """Instances are a panel that can store GRectangles (including other GPanels).INSTANCE ATTRIBUTES (in addition
    to those inherited from GRectangle): contents [list of GRectangle (or subclass of GRectangle) objects]."""

    def add_contents(self, rect):
        """Adds the GRectangle (or subclass of GRectangle) rect to _contents. Precondition: rect is an instance
         of GRectangle, and is contained inside of the GPanel (left is >= panel’s left,
         right is <= panel’s right and so on)."""
        self._content.append(rect)

    def remove_contents(self, rect):
        """Removes the GRectangle (or subclass of GRectangle) rect from _contents.
        Precondition: rect is an element of _contents."""
        self._content.remove(rect)

    def clear(self):
        """Removes all elements from _contents"""
        self._content.clear()

    def get_contents(self):
        """Returns: a COPY of the list of GRectangles in this GPanel.
        The GRectangles do not need to be copied; only the list."""
        if super.contains(self.x, self.y):
            return self._content

    def __init_(self):  # FILL IN
        """Creates a new GPanel of the given dimensions and color.Parameters x and y specify
        the bottom left corner of the panel. Parameters wand h are the width and height.
        Parameter color is the fillcolor. A new GPanel has no GRectangles stored inside it.
        Precondition: x, y, w, and h are floats with w, h > 0. color is an instance of class RGB;
        its default value is WHITE."""
        super().__init__(x=0, y=0, height=10, width=10, linecolor='RED', fillcolor="RED")
        self._content = []

    def draw(self, view):
        """Draws this GPanel AND ITS CONTENTS to the parameter view.The drawing order is
        important for this method. First it draws the GPanel itself. Then it draws all of the contents,
        in the order that they are given in the list _contents (so items at the end of the list are on top).
        Precondition: view is an instance of GView."""
        super().draw()


def main():
    mat = Matrix2x2(3, 4, 2, 9)
    mat.__str__()
    print(mat.determinant())
    print(mat.transpose())
    """

    :return:
    """
    return None


if __name__ == "__main__":
    main()
