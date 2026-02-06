# Broadcasting in Advance Numpy is used to perform operations on arrays of different shapes and sizes.

prices=[100,200,300]
discount= 10 # 10% discount
final_prices=[]
for price in prices:
    final_price= price - (price * discount/100)
    final_prices.append(final_price)
    
print(final_prices)
# the output will be :
# [90.0, 180.0, 270.0]


# the above method is not efficient as it uses a loop to calculate the final prices.
# We can use broadcasting to perform the same operation without using a loop

#broadcasting solution is in other file named solution 
