# Rakamı kullanıcı belirlesin istedim.
liste = [1,2,1,1,3,6,6,7,2,5,3,2,1,6,5,4,3,2,2,1]
secilen = input("Listenin içinde hangi rakamı aramak istediğinizi yazınız: ")
sayac = 0
if secilen.isdigit() == True:
    for x in range(0,len(liste)):
        if liste[x] == int(secilen):
            sayac += 1
    if sayac != 0:
        print("Listenin içinde",sayac,"tane",secilen,"rakamı bulunuyor.")
    else:
        print("Belirttiğiniz rakam liste içinde bulunmuyor!")
else:
    print("Bir rakam girmediniz!!!")
