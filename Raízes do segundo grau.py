#ax² + bx + c

a = int(input('digite o valor do coeficiente A:'))
b = int(input('digite o valor do coeficiente B:'))
c = int(input('digite o valor do coeficiente C:'))

delta = b**2 - 4*a*c
raiz1 = (-b + delta**0.5) / (2*a)
raiz2 = (-b - delta**0.5) / (2*a)  

X = (-b)/(a*2)
V = (-delta)/(a*4)

print('Essa função tem delta valendo:',delta)
print('Essa função tem como raízes: ',raiz1,'e', raiz2)

if a > 0:
    print('Essa função tem valor mínimo de Y valendo: ',V)
    print('Essa função tem seu valor mínimo de Y para X valendo:', X)
elif a < 0: 
    print('Essa função tem valor máximo de Y valendo:',V)
    print('Essa função tem seu valor máximo de Y para X valendo:', X)
    #Matheus Stepple e Matheus Henrique na calourada CinBebeda2024 
