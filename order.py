#List=["cutleries", "sardines", "groceries", "VAT"]

def order():
    print("What is the total amount in your wallet?")
    walletamount=float(input())
    print("What did you order")
    cutleries=input()
    print("enter the price")
    cutleriesamount=float(input())
    print("What else did you order")
    sardines=input()
    print("enter the price")
    sardinesamount=float(input())
    print("What else did you order")
    groceries=input()
    print("enter the price")
    groceriesamount=float(input())
    print("Service Charge")
    VAT=input()
    print("enter the amount")
    VATamount=float(input())
    total=cutleriesamount+sardinesamount+groceriesamount+VATamount
    walletbalance=walletamount-total
    print("My orders are: " + cutleries + "," + str(cutleriesamount) + "," + sardines + "," + str(sardinesamount) + "," + groceries + "," + str(groceriesamount) + "," + VAT + "," + str(VATamount) + ","  + str(total) + "," + str(walletbalance))   
    
order()   

