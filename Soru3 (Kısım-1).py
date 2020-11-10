liste = [9,5,3,0,-12,43,62,18,-7,-2000,5,7,11,38]
for x in range(0,len(liste)):
    for y in range(x,len(liste)): # Belirlenen x değerini baz alarak onun sağında kalan değerleri sıralamak için kullanıcaz.
        if liste[x] > liste[y]: # Büyük olan değeri sağa doğru taşımamıza yardım ediyor.
            temp = liste[x] # temp diye adlandırığımız geçici değer sayesinde liste[x] ilk değerini kaybetmeyecek.
            liste[x] = liste[y]
            liste[y] = temp
print("Listenin sıralanmış hali şu şekildedir:\n",liste)
