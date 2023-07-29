Product_Name = input_data.get('Product_Name')
List_Price = input_data.get('List_Price')
Quantity = input_data.get('Quantity')
Amount = input_data.get('Amount')
Discount = input_data.get('Discount')
Tax = input_data.get('Tax')
Total = input_data.get('Total')
Shiping_Code = input_data.get('Shiping_Code')
Customer_Name = input_data.get('Customer_Name')
First_Name = input_data.get('First_Name')
Last_Name = input_data.get('Last_Name')
Email = input_data.get('Email')
Billing_Street = input_data.get('Billing_Street')
Billing_City = input_data.get('Billing_City')
Billing_State = input_data.get('Billing_State')
Billing_Code = input_data.get('Billing_Code')
Shipping_Street = input_data.get('Shipping_Street')
Shipping_City = input_data.get('Shipping_City')
Shipping_Code = input_data.get('Shipping_Code')
Shipping_State = input_data.get('Shipping_State')
try:
    Subject =First_Name +" "+Last_Name +" "+ Product_Name
except:
    Subject = Product_Name
output = {"Subject":Subject,'Product Name ': Product_Name, 'List Price':List_Price,'Quantity':Quantity,'Amount':Amount,'Discount':Discount,'Tax':Tax,'Total':Total,"Customer Name":Customer_Name,"First Name":First_Name,"Last Name":Last_Name,"Email":Email,"Billing Street":Billing_Street,"Billing City":Billing_City,"Billing State":Billing_State,"Billing Code":Billing_Code,"Shipping Street":Shipping_Street,"Shipping City":Shipping_City,"Shipping Code":Shipping_Code,"Shipping State":Shipping_State}