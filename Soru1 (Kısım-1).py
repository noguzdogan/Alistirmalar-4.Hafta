toplam = 0.0
liste = [17,15,13,11,9,7,5,3,1]
hata = 0
for x in range(0,len(liste)):
    if (type(liste[x]) == float) or (type(liste[x]) == int) and hata != 1:
        toplam += liste[x]
    else:
        hata = 1 # Listenin içinde string cinsinden bir veri olduğuna işaret eder.
if hata == 0:
    print("Liste içinde belirlediğiniz sayıların toplamı: ",toplam)
else:
    print("Lütfen sadece sayılardan oluşan bir liste tanımlayınız!!")
