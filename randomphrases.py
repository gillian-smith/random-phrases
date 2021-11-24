from random import randint
import sys

def randword(lst):
	return lst[randint(0,len(lst)-1)]

def randpair(lst1, lst2):
	return randword(lst1) + " " + randword(lst2)

def randtriple(lst1, lst2, lst3):
	return randword(lst1) + " " + randword(lst2) + " " + randword(lst3)

#Print an adjective and a noun
#print(randpair(adjs, nouns))

def main(args):
	with open("adjs.txt", 'r') as f:
		adjs = [line.rstrip('\n') for line in f]
	with open("nouns.txt", 'r') as f:
		nouns = [line.rstrip('\n') for line in f]
	with open("pnouns.txt", 'r') as f:
		pnouns = [line.rstrip('\n') for line in f]
	with open("propers.txt", 'r') as f:
		propers = [line.rstrip('\n') for line in f]
	with open("advbs.txt", 'r') as f:
		advbs = [line.rstrip('\n') for line in f]
	with open("vbgs.txt", 'r') as f:
		vbgs = [line.rstrip('\n') for line in f]
	with open("vbzs.txt", 'r') as f:
		vbzs = [line.rstrip('\n') for line in f]
	with open("preps.txt", 'r') as f:
		preps = [line.rstrip('\n') for line in f]
	with open("fws.txt", 'r') as f:
		fws = [line.rstrip('\n') for line in f]

	phrase = ""
	for arg in args:
		if arg=="adj":
			phrase = phrase + randword(adjs) # Adjective
		elif arg=="noun":
			phrase = phrase + randword(nouns) # Noun
		elif arg=="pnoun":
			phrase = phrase + randword(pnouns) # Plural noun
		elif arg=="proper":
			phrase = phrase + randword(propers) # Proper name
		elif arg=="advb":
			phrase = phrase + randword(advbs) # Adverb
		elif arg=="vbg":
			phrase = phrase + randword(vbgs) # Verb: gerund (ends with ing)
		elif arg=="vbz":
			phrase = phrase + randword(vbzs) # Verb: present 3rd person (e.g. deserves, believes, goes. Comes after he/she/it)
		elif arg=="prep":
			phrase = phrase + randword(preps) # Preposition
		elif arg=="fw":
			phrase = phrase + randword(fws) # Foreign words
		phrase = phrase + " "
	print(phrase)

if __name__ == "__main__":
	main(sys.argv[1:])