
import random
import string

laenge = int(input("Wie lang soll das Passwort sein? "))

zeichen = string.ascii_letters + string.digits + string.punctuation

passwort = ""

for i in range(laenge):
    passwort += random.choice(zeichen)

print("\nDein Passwort lautet:")
print(passwort)