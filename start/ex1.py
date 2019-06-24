#!/usr/local/bin/python3.7
print ("Hello, world!")

# Comment 
if True:
	print("True")
else:
	print("False")

word = "Some text here"
sentence = 'Fixed sentence'

counter = 50
miles = 700.0
name = "Joe"

a = b = c = 0

complex_type = 1+2j
ss = 1+2j + 2+5j
print("Real: " + str(ss.real) + " Imaginário: " + str(ss.imag))
print("Conjugado: " + str(ss.conjugate()))


s='Hello, World!!'
print(s[0])
print(s[1:5])
print(s[:5])
print(s[5:])
print(s[1]*100)


lista=[1,2,3,4,"Text"]
print(lista)

tupla=(1,2,2,"Text")
print(tupla)

print(lista+lista)
print(tupla+tupla)

dic={}
dic['a']='aaaa'
dic['b']='bbbb'

dic2={'name':'rui', 'age':37}

print(dic)
print(dic2)

x=10+5*(3//5)
print(x)
print(x>>1)

print(30>=50 and 7!=10)


l=(1,2,3,4,7,7,7,7,10)
for i in l:
	print(i),

if 10 in l:
	print("Achou")
else:
	print("Não achou")

if 10 not in l:
	print("Achou")
else:
	print("Não achou")

score=float(input("Digite a nota:"))
if (score>=6.0 and score<=10.0):
	print("APROVADO!")
elif (score>=5.0 and score<6.0):
	print("EXAME!")
elif (score>=0 and score<5.0):
	print("REPROVADO!")
else:
	print("NOTA INVALIDA!")

i=0
while i<100:
	print(i),

for i in range(0,100):
	print(i)

for i in range(0,10):
	for j in range(0,20)
		print "*"*i, j,