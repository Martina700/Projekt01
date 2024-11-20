'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martina Martinková
email: martinkova.m@post.cz
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
registrovani = {"Bob":"123","Ann":"pass123","Mike":"password123", "Liz": "pass123" }
jmeno = input("Zadej své jméno:")
heslo = input("Zadej své heslo:")
print("-" * 40)
found = False
for key in registrovani:
    
    if jmeno == key:
        found = True
if not found:
    print("Uživatel nenalezen:")
    quit()
if registrovani[jmeno] != heslo:
    print("Špatné heslo.")
    quit()
print(f"Welcome to the app, {jmeno}")

print("We have 3 texts to be analyzed.")
print("-" * 40)
vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
if vyber_textu != "1" and vyber_textu != "2" and vyber_textu != "3":
    print("Wrong input")
    quit()
vybrany_text = TEXTS[int(vyber_textu)-1]
slova = vybrany_text.split()
print("-" * 40)
print(f"There are {len(slova)} words in the selected text.")
pocet_titlecase = 0
for i in slova:
    if i[0].isupper():
        pocet_titlecase += 1
print(f"There are {pocet_titlecase} titlecase words.")
    
pocet_uppercase = 0
for i in slova:
    if i.isupper() and not any(ch.isdigit() for ch in i):
        pocet_uppercase += 1
print(f"There are {pocet_uppercase} uppercase words.")

pocet_lowercase = 0
for i in slova:
    if i.islower():
        pocet_lowercase += 1
print(f"There are {pocet_lowercase} lowercase words.")

pocet_numeric = 0
soucet = 0 
for i in slova:
    if i.isdigit():
        soucet += int(i)
        pocet_numeric += 1
print(f"There are {pocet_numeric} numeric strings.")
print(f"The sum of all the numbers {soucet}")
print("-" * 40)
print("LEN|  OCCURENCES  |NR.")
print("-" * 40)

vyskyty = {}
for i in slova:
    slovo = i.replace(".", "").replace(",", "")
    delka = len(slovo)
    if delka in vyskyty:
        vyskyty[delka] += 1
    else:
        vyskyty[delka] = 1
serazene_vyskyty = dict(sorted(vyskyty.items()))
for key, value in serazene_vyskyty.items():
    km = 1
    if key < 10:
        km = 2
    else:
        km = 1
    print(f"{' ' * km}{key}|{'*' * value}{' ' * (14 - value)}|{value}")




        


        
    
    
 