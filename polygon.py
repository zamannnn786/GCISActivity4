class polygon:
    NameOfPolygon = "Square"
    Sides = [4, 4, 4, 4]
    
    """This function has the job of initializing the polygon object"""

    def __init__(self, NameOfPolygon = "Square", Sides = [4, 4, 4, 4]):
        self.NameOfPolygon = NameOfPolygon
        self.Sides = Sides

    """This function has the job of printing and returning the name of the polygon object"""

    def get_name(self):
        print("The name for the polygon is", self.NameOfPolygon)
        return self.NameOfPolygon
    
    """This function has the job of setting a new name for the polygon object"""

    def set_name(self, NewName):
        self.NameOfPolygon = NewName
        print("The new name for the polygon has been set")

    """This function has the job of printing and returning the sides of the polygon object"""

    def get_sides(self):
        print("The sides are", self.Sides)
        return self.Sides
    
    """This function has the job of setting a new list of sides for the polygon object"""

    def set_sides(self, NewList):
        self.Sides = NewList
        print("The new sides for the polygon has been set")


