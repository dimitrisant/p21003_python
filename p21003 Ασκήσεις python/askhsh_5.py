import string

file = open(input('Εισάγετε όνομα αρχείου: '), 'r')
keimeno = file.read()
keimeno = keimeno.lower()

disallowed_characters = string.punctuation + string.digits + "\n\t"

for i in disallowed_characters:
	# if i == "\n" or i == "\t":
	keimeno = keimeno.replace(i, " ")
	# else:
	# keimeno = keimeno.replace(i, "")

a = keimeno.split(" ")
d = dict()
for i in a:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1

print("Οι 10 δημοφιλέστερες λέξεις είναι: ")
af = sorted(d.items(), key=lambda x: x[1], reverse=True)
pl = 0
kena = int(a.count(''))
for i in range(0, len(a)-1):
	if pl < 10 and af[i][0] != '':
		print(pl + 1, ": ", af[i])
		pl += 1
	elif pl >= 10:
		break


k = a
for i in range(0, len(k)-1):
	if len(k[i]) >= 2:
		k[i] = k[i][:2]
	else:
		k[i] = ''


s = [[x, k.count(x)] for x in set(k)]
af2 = sorted(s, key=lambda x: x[1], reverse=True)


print("\n Οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι: ")
pl = 0
for i in range(0, len(k)-1):
	if pl < 3 and af2[i][0] != '':
		print(pl + 1, ": ", af2[i])
		pl += 1
	elif pl >= 3:
		break

t = keimeno.split()
for i in range(0, len(t)-1):
	if len(t[i]) >= 3:
		t[i] = t[i][:3]
	else:
		t[i] = ''


s2 = [[x, t.count(x)] for x in set(t)]
af3 = sorted(s2, key=lambda x: x[1], reverse=True)

print("\n Οι τρεις πρώτοι συνδυασμοί τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι: ")
pl = 0
for i in range(0, len(t)-1):
	if pl < 3 and af[i][0] != '':
		print(pl + 1, ": ", af3[i])
		pl += 1
	elif pl >= 3:
		break
