# gets operator and operand from user and performs operation
from operator import pow, truediv, mul, add, sub

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}


def evaluate_math_expression(input_expression):
    if input_expression.isdigit():
        return float(input_expression)
    for key in operators.keys():
        left, operator, right = input_expression.partition(key)
        if operator in operators:
            return operators[operator](evaluate_math_expression(left), evaluate_math_expression(right))


calc = input("Type calculation:\n")
print("Answer: " + str(evaluate_math_expression(calc)))
