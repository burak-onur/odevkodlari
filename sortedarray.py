import random
array= []

for i in range(10000):
    array.append(random.randint(0,30000)) #10000 elemanlı bir dizinin elemanlarını 0 ile 30000 arasında olacak şekilde rastgele oluşturuyorum

def bubbleSort(x):
    for i in range(len(x)):
        for j in range(0, len(x)-i-1):
            if x[j]> x[j + 1]:                  #bubblesort algoritmasıyla diziyi sıralıyorum
                temp=x[j]
                x[j]=x[j+1]
                x[j+1]=temp    
                
bubbleSort(array)

max=array[9999]
print("En Büyük Sayı:",max)                 #dizinin son elemanını en büyük sayı olarak yazdırıyorum
