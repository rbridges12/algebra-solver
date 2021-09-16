
class Term:
    def __init__(self, coefficient, variable):
        self.coef = coefficient
        self.variable = variable
        
class Equation:
    
    # TODO: add format option, implement other format parsing
    def __init__(self, equation_str):
        
        # split two sides of equation
        sides = equation_str.split("=")
        left = sides[0].strip()
        right = sides[1].strip()
        
        
        self.lhs = []
        self.rhs = []
        