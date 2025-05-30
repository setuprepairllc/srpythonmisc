"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000, print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 24000

# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
      usd_value = bitcoin_amount * bitcoin_value_usd
      
      if(usd_value < 30000):
         print("Value is less than 30,000")
    
      return usd_value
  
  
  
# 2) use function to calculate if the investment is below $30,000
value = bitcoinToUSD(investment_in_bitcoin,bitcoin_to_usd)
print(value)


