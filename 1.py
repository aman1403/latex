import sys
# import 2.py
import os
a=str()
sl="\ "
sl=sl.strip()
a=sl+"documentclass{article}"+"\n"+sl+"usepackage{tikz}"+"\n"+sl+"usetikzlibrary{arrows,shapes}"+"\n"+sl+"begin{document}"+"\n"+sl+"begin{tikzpicture}[scale=2.0,blue,>=stealth,auto,thick,node/.style={circle,black,draw,font="+sl+"sffamily"+sl+"Large"+sl+"bfseries}]"+"\n"+sl+"tikzstyle{every node}=[draw,shape=circle];"+"\n"
# print (a)
f=open("pr.tex","w")
f.write(a)
r=int(input("Which Graph You Want to Draw"+"\n"+"\n"+"1 : Directed Graph"+"\n"+"2 : Undirected Graph" +"\n"+"\n"+"Enter your choice : "))
if(r==2):
	b=int(input("Enter no. of vertices : "))
	for i in range(b):
		c=sl+"path"+" "+"("+str(i*(360//b))+":"+str(3)+"cm)"+" "+"node"+" "+"[fill=green]"+" "+"(v"+str(i)+")"+" "+"{$v_"+str(i)+"$};"+"\n"
		# print(c)
		f.write(c)
	d=(b*(b-1)//2)
	# print(d)	
	for i in range(b):
		u=sl+"draw"+" "+"(v"+str(i)+")"
		# j=i+1
		for j in range(i+1,b):
			e=u+"--"+" "+"(v"+str(j)+")"+";"+"\n"
			print(e)
			f.write(e)
	for i in range(b):
		# u=sl+"draw"+" "+"(v"+str(i)+")"
		# e1=u+" "+"to[bend left]"+" "+"(v"+str(i)+")"+";"+"\n"
		e1=sl+"draw[thick,->,shorten >=1pt] (v"+str(i)+") to [out=90,in=180,loop,looseness=4.8]"+" "+"(v"+str(i)+");"+"\n"

		f.write(e1)
	r=sl+"end{tikzpicture}"+"\n"
	q=sl+"end{document}"
	#i=sl+"draw[thick,->,shorten >=1pt] (v0) to [out=90,in=180,loop,looseness=4.8]"+" "+"(v0);"
	f.write(r+q)
	f.close()
	# c="pdflatex pr.tex"
	# os.system(c)
	os.system("pdflatex pr.tex")
	os.system("evince pr.pdf")
elif(r==1):
	l=input("Enter input file name : ")
	g=open(l,"r")
	e=g.readlines()
	d=[]
	for i in range(len(e)):
		d.append(e[i].split())
# print(d)
	for h in range(len(d)):
		c=sl+"path"+" "+"("+str(h*(360//len(d)))+":"+str(3)+"cm)"+" "+"node"+"[fill=green]"+" "+"(v"+str(h)+")"+" "+"{$v_"+str(h)+"$};"+"\n"
		f.write(c)
	for i in range(len(e)):
		for j in range(len(d[0])):
			if(i==j and d[i][j]!=0):
				e1=sl+"draw[thick,->,shorten >=1pt] (v"+str(i)+") to [out=90,in=180,loop,looseness=4.8]"+" "+"(v"+str(i)+");"+"\n"
				f.write(e1)
			if(d[i][j]!=0 and i!=j):
				u=sl+"draw"+" "+"(v"+str(i)+")"+"[->,blue]"
				e=u+" "+"to[bend left]"+" "+"(v"+str(j)+")"+";"+"\n"
				f.write(e)
	r=sl+"end{tikzpicture}"+"\n"
	q=sl+"end{document}"
	#i=sl+"draw[thick,->,shorten >=1pt] (v0) to [out=90,in=180,loop,looseness=4.8]"+" "+"(v0);"
	f.write(r+q)
	f.close()
	# c="pdflatex pr.tex"
	# os.system(c)
	os.system("pdflatex pr.tex")
	os.system("xdg-open pr.pdf")
else:
	print("Choose valid choice no.")				
		# print(c)
		
		

					