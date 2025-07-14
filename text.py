#SAYI TAHMİN OYUNU
import random

def sayitahmin(): 
  print("Sayı tahmin oyununa hoş geldin!")
  print("Zorluk seviyesi seçmek ister misinn: kolay(1-50), orta(1-100), zor(1- 500)")
  zorluk=input("zorluk seviyesini seç:")
  if zorluk=="kolay":
   sayi=random.randint(1,50)
  elif zorluk=="orta":
   sayi=random.randint(1,100)
  else: 
   sayi=random.randint(1,500)

  print("Bir sayı tuttum. Bakalım tahmin edebilecek misin balım!")
  tahminler=[]
  puan=10

  for deneme in range(1,11):
      try:
        tahmin=int(input(f"{deneme}.tahminin: "))
        tahminler.append(tahmin)
      
      except ValueError:
          print("Lütfen sadece sayı gir canim!")
          continue

      if sayi==tahmin:
          tebrikler = ["Harikasın!", "Doğru bildin!", "Bravo!", "Tebrikler!"]
          mesaj=random.choice(tebrikler)
          print(f"{mesaj} {deneme}.denemede buldunn!")
          print(f"skorun: {puan} puan ")
          break
          
      elif sayi>tahmin:
          print("daha büyük bir sayi dener misinn?")
          

      else:
          print("daha küçük bir sayi dener misin? ")

      puan-=1
          
  else:
      print(f"tahmin hakkın bitti. Tuttuğum sayı {sayi}")
      print("tahminleriniz:",tahminler)
  cevap=input("tekrar oynamak ister misin canımm <3 (e/h)" )
  if cevap== "e":
      sayitahmin()
  else:
      print("güle güle ballı turtam :)")
sayitahmin()
