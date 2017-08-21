import math
alpha = 0.0
beta  = 0.1

inicio_dominio = 0
final_dominio  = 2*math.pi
delta_t = 4
passo = (final_dominio - inicio_dominio)/delta_t

u_0 = alpha
u_1 = beta
u_2 = beta*delta_t + alpha

u_n_menos_1 = u_0
u_n = u_1
u_n_mais_1 = u_2

n = []
malha = []
aux = inicio_dominio
for i in range(delta_t):
	n.append(aux)
	aux += passo
print n

def calcula_u_n_mais_1(u_n_menos_1,u_n):
	u_n_mais_1 = u_n_menos_1*delta_t + u_n
	return u_n_mais_1 
def derivada_segunda(u_n_menos_1,u_n,u_n_mais_1):
	derivada_segunda = (u_n_mais_1 -2*u_n + u_n_menos_1)/(delta_t**2)
	return derivada_segunda
 
for i in range(delta_t):
	print("numerica : "+str(derivada_segunda(u_n_menos_1,u_n,u_n_mais_1)))
	print("exata    : "+str(-1*math.sin(i)))
	u_n_menos_1 = u_n
	u_n = u_n_mais_1
	u_n_mais_1 = calcula_u_n_mais_1(u_n_menos_1,u_n)
	
