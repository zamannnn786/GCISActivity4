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

    """checks if two polygons are equal."""
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.NameOfPolygon == other.NameOfPolygon and self.Sides == other.Sides
        else:
            return None
        
    """Check if two polygons are not equal."""

    def __ne__(self, other):
        return not self.__eq__(other)

    """this function calculates the circumference of the polygon"""

    def calculate_circumference(self):
        return sum(self.Sides)
         #or (for simplified understanding)
        #total = 0 
        #for side in self.Sides:  
        #    total += side  
        #return total  

    """This function returns the string representation of the polygon""" 

    def __str__(self):
        return str(self.NameOfPolygon) + " with sides: " + str(self.Sides)
    
    
    def main():
        # Instantiate three Polygon objects
        triangle = polygon("Triangle", [3, 3, 3])
        square = polygon("Square", [4, 4, 4, 4])
        hexagon = polygon("Hexagon", [6, 6, 6, 6, 6, 6])

        # Print string representation and calculated circumference
        print(triangle)
        print("Circumference:", triangle.calculate_circumference())

        print(square)
        print("Circumference:", square.calculate_circumference())

        print(hexagon)
        print("Circumference:", hexagon.calculate_circumference())

    if __name__ == "__main__":
        main()




