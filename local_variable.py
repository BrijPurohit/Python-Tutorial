__author__ = 'Gaurav'
#When you declare variables inside a function definition, they are not related in any way to other variables
# with the same names used outside the function - i.e. variable names are local to the function
x = 50
def func(x):
    print ('x is', x)
    x = 2
    print ('Changed local x to', x)
func(x)
print ('x is still', x)
