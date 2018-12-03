import sys
import os
a=str()
sl="\ "
sl=sl.strip()
# WROTE LATEX CODE SYNTAX IN TEX FILE
a=sl+"documentclass{article}"+"\n"+sl+"usepackage{tikz}"+"\n"+sl+"usetikzlibrary{arrows,shapes}"+"\n"+sl+"begin{document}"+"\n"+sl+"begin{tikzpicture}[scale=2.0,blue,>=stealth,auto,thick,node/.style={circle,black,draw,font="+sl+"sffamily"+sl+"Large"+sl+"bfseries}]"+"\n"+sl+"tikzstyle{every node}=[draw,shape=circle];"+"\n"
f=open("pr.tex","w")
f.write(a)
r=int(input("Which Graph You Want to Draw"+"\n"+"\n"+"1 : Directed Graph"+"\n"+"2 : Undirected Graph" +"\n"+"\n"+"Enter your choice : "))
# CHECK FOR THE GRAPH WHICH USER WANTS
if(r==2):
	# FOR UNDIRECTED GRAPH
	b=int(input("Enter no. of vertices : "))
	# CREATED NODES
	for i in range(b):
		c=sl+"path"+" "+"("+str(i*(360//b))+":"+str(3)+"cm)"+" "+"node"+" "+"[fill=green]"+" "+"(v"+str(i)+")"+" "+"{$v_"+str(i)+"$};"+"\n"
		f.write(c)
	d=(b*(b-1)//2)
	#CONNECTING NODES
	for i in range(b):
		u=sl+"draw"+" "+"(v"+str(i)+")"
		for j in range(i+1,b):
			e=u+"--"+" "+"(v"+str(j)+")"+";"+"\n"
			print(e)
			f.write(e)
	#FOR SELF LOOP 
	for i in range(b):
		e1=sl+"draw[thick,shorten >=1pt] (v"+str(i)+") to [out=90,in=180,loop,looseness=4.8]"+" "+"(v"+str(i)+");"+"\n"
		f.write(e1)
	r=sl+"end{tikzpicture}"+"\n"
	q=sl+"end{document}"
	f.write(r+q)
	f.close()
	# FOR OPENING PDF
	os.system("pdflatex pr.tex")
	os.system("evince pr.pdf")
	os.system("rm pr.tex")
elif(r==1):
	# FOR DIRECTED GRAPH
	t=int(input("Which input you want to give :  "+"\n"+"\n"+"1: Matrix file"+"\n"+"2: no. of vertices"+"\n"+"\n"+"Enter your choice : "))
	if(t==1):
		# IF INPUT IS MATRIX FILE
		l=input("Enter input file name : ")
		g=open(l,"r")
		e=g.readlines()
		d=[]
		a=-1
		for i in range(len(e)):
			d.append(e[i].split())
# FOR SQUARE MATRIX
		if(len(d)==len(d[0])):
			# CREATED NODES
			for h in range(len(d)):
				c=sl+"path"+" "+"("+str(h*(360//len(d)))+":"+str(3)+"cm)"+" "+"node"+"[fill=green]"+" "+"(v"+str(h)+")"+" "+"{$v_"+str(h)+"$};"+"\n"
				f.write(c)
				# CONNECTING NODES
			for i in range(len(e)):
				for j in range(len(d[0])):
					if(d[i][j]!="0"):
						if(i==j):
							print(d[i][j])
							e1=sl+"draw[thick,->,shorten >=1pt] (v"+str(i)+") to [out=90,in=180,loop,looseness=4.8]"+" "+"node[anchor=north,draw=none,fill=none,above,sloped]"+"{"+str(d[i][j])+"}"+" "+"(v"+str(i)+");"+"\n"
							f.write(e1)
							# FOR SELF LOOP
					if(i!=j):
						if(d[i][j]!="0"):
							u=sl+"draw"+" "+"(v"+str(i)+")"+"[->,blue]"
							e=u+" "+"to[bend left]"+" "+"node[anchor=north,draw=none,fill=none,above,sloped,yshift=+1ex]"+"{"+str(d[i][j])+"}"+" "+"(v"+str(j)+")"+";"+"\n"
							f.write(e)
			r=sl+"end{tikzpicture}"+"\n"			
			q=sl+"end{document}"
			f.write(r+q)
			f.close()
			os.system("pdflatex pr.tex")
			os.system("evince pr.pdf")
			os.system("rm pr.tex")
		else:
			#FOR M*N MATRIX
			 #GIVEN ANY MATRIX CONVERTED TO SQUARE MATRIX 
			if(len(d[0])>len(d)):
				l=len(d[0])
			else:
				l=len(d)
			v=[["0" for x in range(l)]for y in range(l)]
			for i in range(len(d)):
				for j in range(len(d[0])):
		   			v[i][j]=d[i][j]
			# CREATED NODES
			for h in range(len(v)):
				c=sl+"path"+" "+"("+str(h*(360//len(v)))+":"+str(3)+"cm)"+" "+"node"+"[fill=green]"+" "+"(v"+str(h)+")"+" "+"{$v_"+str(h)+"$};"+"\n"
				f.write(c)
				# CONNECTING NODES
			for i in range(len(v)):
				for j in range(len(v)):
					# SELF LOOP
					if(i==j):
						if(v[i][j]!="0"):
							print(v[i][j])
							e1=sl+"draw[thick,->,shorten >=1pt] (v"+str(i)+") to [out=90,in=180,loop,looseness=4.8]"+" "+"node[anchor=north,draw=none,fill=none,above,sloped]"+"{"+str(v[i][j])+"}"+" "+"(v"+str(i)+");"+"\n"
							f.write(e1)
					if(i!=j):
						if(v [i][j]!="0"):
							u=sl+"draw"+" "+"(v"+str(i)+")"+"[->,blue]"
							e=u+" "+"to[bend left]"+" "+"node[anchor=north,draw=none,fill=none,above,sloped,yshift=+1ex]"+"{"+str(v[i][j])+"}"+" "+"(v"+str(j)+")"+";"+"\n"
							f.write(e)
			r=sl+"end{tikzpicture}"+"\n"			
			q=sl+"end{document}"
			f.write(r+q)
			f.close()
			os.system("pdflatex pr.tex")
			os.system("evince pr.pdf")
	else:
		# FOR DIRECTED GRAPH
		# IF INPUT IS NO. OF VERTICES
		b=int(input("Enter no. of vertices : "))
		for i in range(b):
			# CREATING NODES
			c=sl+"path"+" "+"("+str(i*(360//b))+":"+str(3)+"cm)"+" "+"node"+" "+"[fill=green]"+" "+"(v"+str(i)+")"+" "+"{$v_"+str(i)+"$};"+"\n"
			f.write(c)
		for i in range(b):
			# CONNECTING NODES
			u=sl+"draw"+" "+"[->]"+" "+"(v"+str(i)+")"
			for j in range(b):
				if(i!=j) :
					e=u+"to[bend left]"+" "+"(v"+str(j)+")"+";"+"\n"
					f.write(e)
		for i in range(b):
			# SELF LOOP
			e1=sl+"draw[thick,->,shorten >=1pt] (v"+str(i)+") to [out=90,in=180,loop,looseness=4.8]"+" "+"(v"+str(i)+");"+"\n"
			f.write(e1)
		r=sl+"end{tikzpicture}"+"\n"
		q=sl+"end{document}"
		f.write(r+q)
		f.close()
	# COMPLETE GRAPH WILL BE DISPLAYED 
		os.system("pdflatex pr.tex")
		os.system("evince pr.pdf")
		os.system("rm pr.tex")		
else:
	print("Choose valid choice no.")

		
		

					