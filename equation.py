import re

class Term:
    def __init__(self, coefficient = None, variable = None):
        self.coef = coefficient
        self.variable = variable
        
class Equation:
    
    # TODO: add format option, implement other format parsing
    def __init__(self, equation_str, variable):
        self.parse_equation(equation_str, variable)
        
        

    # def replace_minuses(match):
        
    
    def parse_equation(self, equation_str, variable):
        
        # remove all whitespace
        equation_str = ''.join(equation_str.split())
        
        # split two sides of equation
        sides = equation_str.split("=")
        left = sides[0].strip()
        right = sides[1].strip()
        
        left_terms = left.split("+")
        right_terms = right.split("+")
        
        self.lhs = []
        for term in left_terms:
            coef = 
            self.lhs.append(Term())