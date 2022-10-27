from datetime import datetime
print('---------------- Welcome to virtual market ----------------------')
name = input('Enter your name : ')
#list of items and prices
itm_list = '''
ice cream - rs.45/cup
rice - rs.20/kg
salt - rs.30/kg
sugar - rs.50/kg
oil - rs.80/pack
paneer - rs.115/kg
maggi - rs.10/pack 1reel
Boost - rs.75/pack
colgate - rs.60/each
chocalate - rs.80/each
'''
price = 0
price_list = []
totalprice = 0
quantity = []
final_price = 0
item_list =[]
pricelist =[]

items = {'rice' : 20 , 'icecream' :45 ,'salt' : 30,'sugar' :50,'oil' : 80,'paneer' :115,'maggi' :10 ,'boost' : 75 ,'colgate' : 60,'chocalate' : 80}

print('''
[one] - see the items of the market
[two] - Buy the items of the market
''')
option = input('What do you want : ')
loop = True

while loop :
	if option=='one' :
	 	print(item_list)
	if option == 'two' :
	 	print(itm_list)
	 	print('''
	 	After shopping Enter 'No, bill it' to bill
	 	''')
	 	while loop:
	 		item = input('Enter your item :  ')
	 		if item in items.keys():
	 			quan = input('Enter how much qunantity : ')
	 			price = int(quan)*int((items[item]))
	 			totalprice+=int(price)
	 			item_list.append(item)
	 			pricelist.append((item,quan,items,price))
	 			price_list.append(price)
	 			quantity.append(quan)
	 			cst_gst = (totalprice*5)/100
	 			final_price = cst_gst+totalprice
	 		if 'No' and 'bill' in item : 
	 			if int(final_price) != 0 :
	 				print(25*'*','Virtual Supermarket',25*'*')
	 				print(68*'*')
	 				print('Name : ',name,30*' ','Date : ',datetime.now())
	 				print('s.no',8*' ','Items',8*' ','Quantity',3*' ','Prices')
	 				for i in range(len(pricelist)) :
	 					print(i,11*' ',item_list[i],17*' ',quantity[i],9*' ',price_list[i])
	 				print(68*'-')
	 				print(50*' ','Totalamount','Rs.',totalprice)
	 				print(50*' ','gst+cst','Rs.',cst_gst)
	 				print(50*' ','Final amount',final_price)
	 				print(68*'-')
	 				print(38*' ','Thank you for visit,Visit again')
	 				print(68*'-')
                                        loop = False

	
	 		elif item not in items.keys() :
	 			print('The item is not available')
	 				
