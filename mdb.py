import random

moviedb=[]

site="http://www.worldfree4u.com/how-to-free-downoad-300mb-pc-movies-small-size-single-link-mkv-bluray/"

class film:

    def __init__(self,name,yr,actor,cat,special=None):

        self.name=name

        self.yr=yr

        self.actor=actor

	self.special=special

	self.cat=cat

	self.url=site

a=film("rang de basanti",2006,"aamir khan","bollywood","nominate for academy award")

b=film("baazigar",1988,"kajol","bollywood","actor is in negative shade")

c=film("shahib biwi aur gangester",2011,"randip hooda","bollywood","a political drama")

d=film("phata poster nikla hero",2013,"shahid kapoor","bollywood","a rom-com")

e=film("band baaja baarat",2010,"anuska sharma","bollywood","a romance drama")

f=film("koi mil gaya",2004,"hrithik","bollywood")

h=film("zindagi milegi na dobara",2012,"farhan,hrithik and abhay","bollywood")

temp=[a,b,c,d,e,f,h]

moviedb.append(temp)

del a,b,c,d,e,f,h

del temp

a=film("the shawshank redemption",1992,"morgan freeman","hollywood","based on  a novel")

b=film("the tourist",2010,"angie","hollywood","action,drama")

c=film("i am the legend",2004,"will smith","hollywood","jombie movie")

d=film("catch me if you can",1998,"leo de caprio","hollywood","comedy ,drama")

e=film("no string attached",2011,"natali portman","hollywood","romantic adult movie")

f=film("the last samurai",2004,"tom cruise","hollywood","based on history")

g=film("a nightmare on elm street",2010,"kyle garner","5th part of a very famous horror series")

temp=[a,b,c,d,e,f,g]

moviedb.append(temp)

del temp,a,b,c,d,e,f,g

a=film("the good the bad and the ugly",1966,"clint eastwood","hollywood","in imdb top 250")

b=film("one flew over the cuckoos nest",1975,"jack nickolson","hollywood","won 5 oscars")

c=film("the usual suspects",1995,"kevin spacey","hollywood","crime ,mystery and thriller")

d=film("to kill a mocking bird",1962,"john megna","hollywood","based on novel and won 3 oscars")

e=film("eternal sunshine of spotless mind",2004,"kate winslet","hollywood","sci-fi and romance")

f=film("the night of the hunter",1955,"shelley winters","hollywood","in IMDB top 250")

temp=[a,b,c,d,e,f]

moviedb.append(temp)

del temp ,a,b,c,d,e,f 

def choice(level):

	ch= random.choice(moviedb[level])

	moviedb[level].remove(ch)

	return ch