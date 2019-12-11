import csv
from orders.models import Pizza
from orders.models import Topping

f = open('data.txt', 'r')  
for line in f:  
   line =  line.split(',')  
   product = Pizza()  
   product.product = line[0]  
   product.tipe = line[1]
   product.size = line[2]
   product.price = float(line[3]) #data is missing from file  
   product.save()  

f.close()


f = open('data1.txt', 'r')  
for line in f:  
   line =  line.split(',')  
   print(line)
   product = Topping()  
   product.product = line[0]  
   product.tipo = line[1]
   product.save()  

f.close()
