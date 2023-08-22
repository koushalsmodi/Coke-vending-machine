def main():
     print('Amount Due:', 50) # original line
     amount_due() # calling function

def amount_due():
    change = 50 # base amount

    while change != 0: # loop as long as is change owed is not equal to 0

         insert = int(input('Insert Coin: ')) # asking for user input to insert coin
         if insert in [25,10,5]: # validating coin denominations
             change -= insert # decreasing change owed by customer by the coin value
             print('Amount Due:', change) # printing change
         else:
             print('Amount Due:', change) # if coin is not 25,10,5 then display error message and show amount due
             print('Error invalid coin entered')

    print('Change Owed:', change) # finally showcase change owed


main()