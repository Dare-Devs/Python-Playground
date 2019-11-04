# FUNCTIONS

print('''
    MATH MANIPULATION - LIST OF FUNCTIONS
    matrice_mutiplication(n1 = [8, 19, 148, 4], n2 = [9, 1, 33, 83])
    square(a)
    quadruple(x)
    half(a)
    double(x)
    triple(w)
    cubed(c)
    ''')

def double(x):
    y = x * 2
    return y

def matrice_mutiplication(n1 = [8, 19, 148, 4], n2 = [9, 1, 33, 83]):
    #n1 = [8, 19, 148, 4]
    #n2 = [9, 1, 33, 83]
    n3 = list()
    
    for y in range(0, 4):
        for x in range(0, 4):
            z = n1[y] * n2[x]
            n3.append(z)
    return (n3)

def cubed(c):
    return (c * c * c)


def triple(w):
    return (w * 3)


def abbrevName(name):
    name = name.split(" ")
    hi = list()
    for i in range (len(name)):
        a = name[i]
        initial = a[0:1]
        initial = initial.upper()
        hi.append(initial)
    return (hi[0] + "." + hi[1])
    
def square(a):
    """
    :param a: int.
    :return: prints a multiplied by itself.
    """
    a = int(input("Please enter an integer: "))
    b = a * a
    return b



def q3(a,b,c,d=1,e=4):
    """
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int.
    :param e: int.
    :return: int sum of a and b and c and d and e.
    """
    a = input("enter something")
    b = input("enter something")
    c = input("enter something")
    d = input("enter something if you like")
    e = input("enter something if you like")
    print(a, b, c, d, e)



def half(a):
    """
    prints x
    :param a: int
    :return: int half of a
    """
    return a/2

def quadruple(x):
    """
    Returns x * 4
    :param x:
    :return: int x multiplied by 4
    """
    return x * 4



def q5(a):
    """
    Checks for possible errors and returns a.
    :param a: int.
    :return:
    """
    try:
        a = input("Please enter a string: ")
        b = float(a)
        return b
    except ValueError:
        print ("Invalid Type Conversion!")

        
