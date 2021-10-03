import datetime
import pandas as pd


print('''
*************************************
        Welcome to MCEGY 
**************************************

Menue Item                        Price 
1 - Beef Burger                     2.50
2 - Chickn Burger                   2.00
3 - Pizza                           3.50
4 - Chips
*******************************************
999 to quit
''')
orderItemList= []
orderPriceList =  []
OrderItem =0
total=0
paymentProcessed = False 
paymentType=""
while OrderItem !=999:
  OrderItem = int(input("Enter the order"))
  if OrderItem ==1:
    print("you have ordered Beef Burger          $2.5")
    orderItemList.append("Beef Burger")
    orderPriceList.append(2.5)
  elif OrderItem ==2:
    print("you have ordered Chickn Burger        $2.00")
    orderItemList.append("Chickn Burger")
    orderPriceList.append(2)
  elif OrderItem ==3:
    print("you have ordered Pizza                $3.5")
    orderItemList.append("burger")
    orderPriceList.append(3.5)
  elif OrderItem ==4:
    print("you have ordered Chips                $3.5")
    orderItemList.append("burger")
    orderPriceList.append(3.5)  
  else:
    print("no such an item in the menue")

print("******************************************")
print("Thank you for your order")
print("******************************************")

for i in range (len(orderItemList)):
  print(orderItemList[i],end="         ")
  print("$",orderPriceList[i])
  total=orderPriceList[i]+total
tax =total*0.175
gtotal=total+tax
print('''
**********************************
Total        $''',total,'''
Tax 17.5%    $''',tax,'''
Grand Total  $''',gtotal) 

paymentMethood= int(input("1- Cash Payment/n 2- Card paymet"))
if paymentMethood ==1:
  cash = float(input("Cash amount?"))
  while cash<gtotal:
    print("the amount paid is not suffecient")
    cash = float(input("Cash amount?"))
    
  change= cash-gtotal
  print("your change is",change)
  paymentProcessed = True
  paymentType="Cash"
  
else:
  paymentProcessed = True
  paymentType="Card"
now = datetime.datetime.now()
now= now.strftime("%Y-%m-%d %H:%M:%S")
print(now)

content =(now,orderItemList,orderPriceList,total,tax,gtotal,paymentType)

dataframe = [{'Order Date and Time':now, 'Items':orderItemList,'Price': orderPriceList,'total':total, 'Tax':tax, 'Grand Total ':gtotal, 'Payment Type':paymentType }]
print(dataframe)
###############Saving the delattr
f = open("sales.txt",'a')
f.write(str(content))
f.close()
fo =open('sales.txt','r')
fo.read()
fo.close()

writeframe = pd.DataFrame(dataframe)
writeframe = writeframe[['Order Date and Time', 'Items','Price','total', 'Tax', 'Grand Total ' ,'Payment Type']]
writeframe.append(dataframe)
writeframe.to_csv('sales.csv', index=True)
writeframe.to_excel('sales.xls')