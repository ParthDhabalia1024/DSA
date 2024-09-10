# Remove brackets from an algebraic expression
# In this article we will see how to Remove brackets from an equation in Python. User are supposed to enter equation and then we will remove brackets.

# In an algebraic expression, brackets show the priority of the operation. If the operator outside the bracket has more precedence than the operator between the operands in the brackets the operation inside the brackets will be performed first 
# and then the output of the operation will be operated with operand outside the brackets.



def removebrackets(exp):
    a = ['(', ')', '[', ']','{', '}']
    result = ""
    for i in exp:
        if i not in a:
            result+=i
    return result



#take user input
exp = "(a-b)+[c*d]+{e/f}"
print(removebrackets(exp))