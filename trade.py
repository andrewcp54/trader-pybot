lastPrice = 100
#algorithm to determine if stay in buy state
def buy(price):
    check = lastPrice/100
    if(price/check >= 102):
        state = 0
        return False
    if(price/check <=98):
        return True
    else:
        return True

#algorithm to determine if stay in sell state
def sell(price):
    check = lastPrice/100
    if(price/check >= 102):
        return True
    if(price/check <=98):
        state = 1
        return False
    else:
        return True

p = open("price.txt","r")
currentPrice =int(p.readline())
p.close()
s = open("state.txt","r")
state = int(s.readline())
s.close()

if(state == 1):
    if(buy(currentPrice))==False:
        state = 0
    print("buy")
else:
    if(sell(currentPrice))==False:
        state = 1
    print("sell")
s = open("state.txt","w")
s.write(str(state))
s.close()
print(state)
