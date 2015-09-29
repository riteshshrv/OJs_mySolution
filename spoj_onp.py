'''Program to convert given expression to 
    Reverse Polish Notaion.
    SPOJ: ONP'''

def toRPN(a):
	operators="+-*/^"
	alphabets="abcdefghijklmnopqrstuvwxyz"
	opd=[]
	opt=[]
	for i in range(len(a)):
		if a[i]=="(":
			pass
		elif a[i] in operators:
			opt.append(a[i])
		elif a[i] in alphabets:
			opd.append(a[i])
		elif a[i]==")":
			opd.append(opt.pop())
		else:
			print("error")
			return -1
	return ''.join(opd)

if __name__ == '__main__':
a1='(a+(b*c))'
a2='((a+b)*(z+x))'
a3='((a+t)*((b+(a+c))^(c+d)))'
print(toRPN(a1))
print(toRPN(a2))
print(toRPN(a3))

'''Output:
abc*+
ab+zx+*
at+bac++cd+^*
'''
