a = True
b = False
resultado1 = a and b # FALSE
resultado2 = a or b # TRUE
resultado3 = not a # FALSE

# A ordem de precedência dos operadores lógicos é: NOT , AND e por fim, OR.

c = 3 
c == 4 # FALSE
c > 2 # TRUE
c != 3 # FALSE
d = 4 
c is d # FALSE
c is not d # TRUE

# a ordem dos operadores podem mudar utilizando-se dos parenteses

x = True
y = False
z = True
teste1 = x or y and not z  # Essa expressão é lida pelo interpretador dessa forma: x or (y and (not z)) TRUE

# Utilizando os parenteses podemos mudar o resultado da expressão lógica:

teste2 = (x or y) and (not z) # FALSO
