import string
file = open(input('Εισάγετε το όνομα ενός ascii αρχείου: '), 'r')
keimeno = file.read()
disallowed_characters = string.punctuation + string.digits + "\n\t''"
for i in disallowed_characters:
    # if i == "\n" or i == "\t":
    keimeno = keimeno.replace(i, " ")
    # else:
    # keimeno = keimeno.replace(i, "")

a = keimeno.split(" ")

for i in range(0, len(a) - 2):
    if a[i] != '':
        ath = 0
        j = i+1
        m = len(a[i])
        while j <= (len(a) - 1):
            if a[j] != '':
                t = len(a[j])
                ath = m + t
                if ath == 20:
                    del(a[i])
                    del(a[j])
                    break
                else:
                    j += 1
            else:
                j += 1

pl = [[len(i)] for i in a]
Sum = [int(0) for i in a]
print(Sum)
for i in a:
    if len(i) > 0:
        Sum[len(i)] += 1
        t = [pl[len(i), Sum[len(i)]]]

print(t)