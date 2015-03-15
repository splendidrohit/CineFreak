from Tkinter import *
from tkMessageBox import *
from mdb import *
import webbrowser

points=0
chance=5
level=0
hint=1
sub=[0,0,0]
flag=0
flag2=1
def createlevel(root):
	global wid
	global hint,points,level,flag2,flag,chance
	global movie
	if(points<(level*70)):
		showerror("sorry","you do not have enough points to play this level\nplay  level %d again\n or goto any other lower level"%level)
		return 0
	if(sub[level]>=2):
		showinfo("sorry","you already play 'level %d' two times"%(level+1))
		if(sub[2]>0):
			level=3
			next_level(root)
		elif(points<((level+1)*70)):
			showinfo("sorry","you have only 1 altenative left\nincrease your points at cost of chances")
			level+=1
			addp()
		if(chance==0 and points<(level+1)*70):
			showinfo("oops","you have no alternative left \nYOU LOSE")
			sys.exit(0)
			
		return 2
	flag2=1
	flag=1
	hint=1
	level+=1
	movie=choice(level-1)
	text=movie.name
	a=[]
	vowel=('a','e','i','u','o',' ')
	for i in text:
    		if i in vowel:
        		a.append(i)
    		else:
        		a.append('*')
	del vowel
	wid=makewid(root,level,movie,a)
	sub[level-1]+=1
	del a
	return 1


def inc_point(l,w):
	global chance,points,movie
	if(chance<=0):
		showerror("sorry..","you have no chance left")
		w.destroy()
		return
	points+=10
	chance-=1
	l.config(text="chances = %d\npoints = %d "%(chance,points))
	if(flag):
      		wid.l1.config(text="chances remaining are %d \ntotal points are %d"%(chance,points))
def increase(l,w):
	global chance,points,movie
	if(points<50):
		showerror("sorry","your points are less than 50")
		w.destroy()
		return
	if(chance>=5):
		showerror("sorry..","you already have maximum chances")
		w.destroy()
		return
	points-=40
	chance+=1
	l.config(text="chances = %d\npoints = %d "%(chance,points))
	if(flag):
      		wid.l1.config(text="chances remaining are %d \ntotal points are %d"%(chance,points))
def hatao(w):
		if(flag):
	      		wid.l1.config(text="chances remaining are %d \ntotal points are %d"%(chance,points))
		w.destroy()
def addp():
	global chance,points
	if(level==0 or flag2==0):
		showerror("sorry..","you can't do this at this point")
		return
	win=Toplevel()
	win.grab_set()
	win.resizable(0,0)
	win.title("increase points")
	l=Label(win,text="chances = %d\npoints = %d "%(chance,points))
	l.pack()
	Button(win,text="increase",command=(lambda:inc_point(l,win)),bg='tomato').pack(side=LEFT)
	Button(win,text="cancel",command=(lambda:hatao(win)),bg='tomato').pack(side=RIGHT)
def addc():
	global chance,points,wid
	if(level==0 or flag2==0):
		showerror("sorry..","you can't do this at this point")
		return 
	showwarning("beware..","increase every chance will deduce your 40 points")
	win=Toplevel()
	win.grab_set()
	win.resizable(0,0)
	win.title("increase chances..")
	l=Label(win,text="chances = %d\npoints = %d "%(chance,points))
	l.pack()
	Button(win,text="increase",command=(lambda:increase(l,win)),bg='tomato').pack(side=LEFT)
	Button(win,text="cancel",command=(lambda:hatao(win)),bg='tomato').pack(side=RIGHT)
	
def temp(root,wd,n):
	wd.destroy()
	global wid,points
	if(level==0):
		showerror("sorry","you can't do this at this point\nclick play now")
		return
	destroy(root,n-1,wid)
def destroy(root,lev,win):
	global level
	level=lev
	n=createlevel(root)
	if(n==1):
		win.destroy()
	elif(n==2):
		pass
	elif(n==0):
		level-=1
		destroy(root,level,win)
def end(root):
	global wid,points,chance,flag2,sub
	flag2=0
	temp=[2,2,2]
	mf=Frame(root,bg='aquamarine')
	f=Frame(mf,bg='aquamarine')
	wid=mf
	mf.pack(expand=YES,fill=BOTH)
	Label(f,text="GENIUS !!",bg='aquamarine',font=('times',15,'bold')).pack(expand=YES,fill=BOTH)
	Label(f,text="you have cleared all the levels",bg='aquamarine',font=('times',20,'normal')).pack(expand=YES,fill=BOTH)
	Label(f,text="contact techvirtuoso.rohit@gmail.com for code",bg='aquamarine',font=('times',20,'normal')).pack(expand=YES,fill=BOTH)
	f.pack()
	Button(mf,text="BYE",command=(lambda:sys.exit(0)),bg='tomato').pack(side=LEFT)
	if(sub ==temp):
		points+=(chance*30)
		chance=0
		showinfo("congrats","you have scored your heighest possible score\nyour all chances are converted into points\npoints:\t%d"%points)
	Label(f,text="your  score is %d \nget your gift at this score "%points,bg='aquamarine',font=('times',20,'normal')).pack(expand=YES,fill=X)
	Button(mf,text="get your prize",bg='tomato',command=(lambda:webbrowser.open("http://www.youtube.com/watch?feature=player_detailpage&v=W3vzWIU-gsg"))).pack(side=RIGHT)
def next_level(root):
	global wid,flag
	wid.pack_forget()
	flag=0
	if(level==3):
		end(root)
	else:
		win=Frame(root,bg='aquamarine')
		wid=win
		Label(win,text="congrats you cleared level %d successfully"%(level),bg='aquamarine',font=('times',20,'bold')).pack()
		Label(win,text="go to level %d\ncutoff for this level is %d"%((level+1),(level)*70),bg='aquamarine',font=('times',20,'normal')).pack()
		Button(win,text="start level %d "%(level+1),command=(lambda:destroy(root,level,win)),bg='tomato').pack(side=LEFT)
		Button(win,text="Download '%s' "%movie.name,command=(lambda:webbrowser.open((movie.url),new=2)),bg='tomato').pack(side=RIGHT)
		win.pack(expand=YES,fill=BOTH)
def update(parent,text):
	global chance,points,level
	if(chance<=0):
   		if(points>=40):
			showinfo("listen..","you have no chance left\nso add your chance")
			addc()
		else:
			showinfo("sorry","you have no alternative left\nYOU LOSE")
			sys.exit(0)			
      	elif('*' not in text):
    		showinfo("CONGRATS","\nyou cleared this level\n your points are %d "%(points))
		next_level(parent)
		
class makewid(LabelFrame):
	inc=0
	def __init__(self,parent,level,movie,name):
		makewid.inc=(10*level/2+5)
		self.parent=parent
		LabelFrame.__init__(self,parent,text="welcome to level %d:"%level,labelanchor='n',font=('times',30,'bold'),bg="black",fg='antique white')
		self.pack(expand=YES,fill=BOTH)
		self.f1=Frame(self,bg='aquamarine')
		self.f1.pack(expand=YES,fill=X)
		Label(self.f1,text="complete this movie :",bg='aquamarine',font=('times',20,'normal')).pack(side=TOP,expand=YES,fill=X)
		self.movie=Label(self.f1,text=" ".join(name),bg='blanched almond',font=('times',25,'italic'))
		self.movie.pack(side=BOTTOM)
		self.f2=Frame(self,bg='aquamarine')
		self.l1=Label(self,text="chances remaining are %d \ntotal points are %d"%(chance,points),bg='dark green',fg='antique white',font=('times',20,'normal'))
		self.f2.pack(expand=YES,fill=X)
		self.tl=Frame(self.f2,bg='aquamarine')
		Label(self.f2,text="enter word here: ",anchor='e',bg='aquamarine',font=('times',25,'italic')).pack(side=LEFT,expand=YES,fill=X)
		self.tl.pack(side=RIGHT)
		self.word=Entry(self.tl,width=2)
		self.help=Button(self.tl,bitmap="question",command=self.gethelp)
		self.f3=Frame(self,bg='aquamarine')
		self.check=Button(self.f3,text="check",bg='tomato',command=(lambda:self.call(movie,name)))
		self.ht=Button(self.f3,text="hint 1",bg='tomato',command=(lambda:self.hint(movie)))
		self.ht.pack(side=RIGHT)
		self.word.pack(side=LEFT)
		self.help.pack(side=RIGHT)
		self.check.pack(expand=YES)
		self.f3.pack(fill=X)
		self.l1.pack(fill=X)

	def gethelp(self):
		showinfo("help","enter one word at a time\nthank you")
	def hint(self,movie):
		global hint,points
		if(hint>3):
			showerror("ooops","you already used all 3 hints")
		else:
			if(hint==1):
				if(points<10):
					showerror("ooops","you do not have sufficient points to use this hint")
					return
				showinfo("hint","%s movie\nreleased in %d"%(movie.cat,movie.yr))
				self.ht.config(text="hint 2")
			elif(hint==2):
				if(points<20):
					showerror("oops","you do not have sufficient points to use this hint")
					return
				showinfo("hint","one co-star is %s"%movie.actor)
				self.ht.config(text="hint 3")
			elif(hint==3):
				if(points<30):
					showerror("oops","you do not have sufficient points to use this hint")
					return
				showinfo("hint","%s"%movie.special)
				self.ht.config(text="hint ")
			points-=(hint*10)
			hint+=1
			self.l1.config(text="chances remaining are %d \ntotal points are %d"%(chance,points))
	def call(self,movie,name=None):
		global points,chance
    		text=movie.name
      		c= self.word.get()
      		self.word.delete(0,END) 
      		if(c is ""):
      			self.l1.config(text="chances remaining are %d \ntotal points are %d"%(chance,points))
	        	return 
		if(len(c)>1):
			showerror("not permitted","please enter one word at a time")
			return  
		if(chance<=0):
			pass
      		elif(c in name):
                	showerror("enter again", "%c already exist\n"%c)
      		elif(c in text):
            		points+=makewid.inc
            		for j in range(len(text)):
                		if(c is text[j]):
                    			name[j]=c
      		else:
            		chance-=1
      		self.movie.config(text=" ".join(name))
		update(self.parent,name)
      		self.l1.config(text="chances remaining are %d \ntotal points are %d"%(chance,points))