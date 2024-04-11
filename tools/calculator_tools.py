from langchain.tools import tool

class CalculatorTools():

    @tool("Calculate final rating for an AWS well-architected pillar")
    def calculate(expression):
        """Useful to perform any mathematical calculations,
        like sum, minus, multiplication, division, etc.
        The input to this tool should be a mathematical
        expression, a couple examples are `{"expression": 200*7}` or `{"expression": 5000/2*10}`
        """
        try:
            return eval(expression)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"
