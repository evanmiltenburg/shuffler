import random
import pickle
import time

print("Hello! My name is shuffler, I was coded by MCoury and I love fumbling with English words!")
print()
name = input('What\'s your name?...')
print()
print('It\'s a pleasure to meet you',name,'!')
print()

def prompt():
	global words
	global lwords
	global r
	words = input('Give me a set of words...')
	print()
	lwords = list(words)
	r=int(input(''''How many shufles would you like me to make?
Note that more shuffling means more processing time...'''))
	print()
	main()

try:
	with open('mydict.txt','rb') as fo:
		content=pickle.load(fo)
except IOError:
	print('Can\'t find my dictionary file!...')



def main():
	global l
	global total
	l =[]
	print("I'm working...")
	start_time=time.time()
	for n in range(r):
		random.shuffle(lwords)
		nwords=''.join(lwords)
		swords=nwords.split(' ')
		for item in swords:
			if item in content:
				if item !='':
					if not item in l:
						l.append(item)
						print(item)
	total = round(time.time()-start_time,3)
	print()
	res()

def res():
	if len(l) == 0:
		print('Could\'t make any words!!')
	else:
		print('''I was able to make''',len(l),'words from that sentence in', r, '''shuffles...
And it took me''',total,'seconds')
	print()

prompt()

while True:
	if input('Enter yes to play again or anything else to close me..').lower()=='yes':
		print()
		print('YAY!')
		print()
		prompt()
	else:
		print()
		print('Goodbye! Come back soon!')
		quit()