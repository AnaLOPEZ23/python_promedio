x = 2000

def local_functional():
    x = 2000#Variable local
    print(f"El valor de la variable es{x}")
    

def show_global():
    print(f"El valor de la variable global es{x}")
local_functional()
print(x)