import random




array= []

for i in range(10000):
    array.append(random.randint(0,30000)) #10000 elemanlı bir dizinin elemanlarını 0 ile 30000 arasında olacak şekilde rastgele oluşturuyorum


max=array[0]
for i in array:
    if max<i:
        max=i        #dizideki her elemanın bir öncekinden büyük olup olmadığını inceleyip en büyüğü bulan döngü

print("En Büyük Sayı:",max)     #kodun çalışma süresi 0.115 saniye

print(array)