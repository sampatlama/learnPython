#Price of house is 1M
#ifbuyerhasgood credit,
#They need to put down 10%
#otherwise they need to put down 20%
#print downpayment
price_of_house = 1000000
is_buyer_creditgood = False
if is_buyer_creditgood:
    print(f"They need to put ${(10/100)*price_of_house}")
else:
    print(f"They need to put ${(20/100)*price_of_house}")    
