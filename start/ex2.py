#!/usr/local/bin/python3.7
# Read /etc/passwd file

print("Exemplo #1")
with open('/home/erik/.bash_history', 'r') as reader:
	print(reader.read())

print("Exemplo #2")
with open('/home/erik/.bash_history', 'r') as reader2:
	print(reader2.readline(5))

print("Exemplo #3")
with open('/home/erik/.bash_history', 'r') as reader2:
	print(reader2.readlines())

print("Exemplo #4","*"*200)
with open('/home/erik/.bash_history', 'r') as reader2:
	line = reader2.readline()
	while line!='':
		print(line, end='')
		line=reader2.readline()