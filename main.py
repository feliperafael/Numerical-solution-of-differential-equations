import math
alpha = 0.0
beta  = 0.1

def function(t):
	return alpha*math.cos(t) + beta*math.sin(t)

inicio_dominio = 0.0
final_dominio  = 2.0*math.pi
delta_t =8
passo = (final_dominio - inicio_dominio)/float(delta_t)

u_0 = alpha
u_1 = beta
u_2 = beta*delta_t + alpha

n = []
malha = []
x = []

malha.append(beta)

aux = inicio_dominio
for i in range(delta_t):
	n.append(function(aux))
	x.append(aux)
	aux += passo

def calcula_fx1(fx0,f_linha_x0):
	fx1 = fx0 + passo*(f_linha_x0)
	return float(fx1)

def derivada_segunda(u_0,u_1,u_2):
	derivada_segunda = (u_2 -2*u_1 + u_0)/(delta_t)
	return derivada_segunda
 
for i in range(delta_t-2):
	#print i
	aux = derivada_segunda(u_0,u_1,u_2)
	print("numerica : "+str(aux))
	print("exata    : "+str(-1*math.sin(i)))
	print "" 	
	
	u_0 = u_1
	u_1 = u_2
	u_2 = u_2 + aux*passo + malha[i]*passo + x[i]
	malha.append(aux)
	
