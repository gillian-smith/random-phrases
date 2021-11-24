from nltk.corpus import brown

tagged_words = brown.tagged_words()

adjs = [x for (x,y) in tagged_words if y=='JJ']
nouns = [x for (x,y) in tagged_words if y=='NN']
pnouns = [x for (x,y) in tagged_words if y=='NNS']
propers = [x for (x,y) in tagged_words if y=='NP']
advbs = [x for (x,y) in tagged_words if y=='RB']
vbgs = [x for (x,y) in tagged_words if y=='VBG']
vbzs = [x for (x,y) in tagged_words if y=='VBZ']
preps = [x for (x,y) in tagged_words if y=='IN']
fws = [x for (x,y) in tagged_words if y.startswith('FW')]

with open("adjs.txt",'w') as f:
	for x in adjs:
		f.write(x + '\n')

with open("nouns.txt",'w') as f:
	for x in nouns:
		f.write(x + '\n')

with open("pnouns.txt",'w') as f:
	for x in pnouns:
		f.write(x + '\n')

with open("propers.txt",'w') as f:
	for x in propers:
		f.write(x + '\n')

with open("advbs.txt",'w') as f:
	for x in advbs:
		f.write(x + '\n')

with open("vbgs.txt",'w') as f:
	for x in vbgs:
		f.write(x + '\n')

with open("vbzs.txt",'w') as f:
	for x in vbzs:
		f.write(x + '\n')

with open("preps.txt",'w') as f:
	for x in preps:
		f.write(x + '\n')

with open("fws.txt",'w') as f:
	for x in fws:
		f.write(x + '\n')
