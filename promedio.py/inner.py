x = "global" #Variable global

#Funcion externa
def outer_functional():
    x = "enclosing"
    
#Funcion interna
    def inner_function():
        x = "local"
        print(x)
    
    inner_function()
    print(x)
    
outer_functional()
print(x)

