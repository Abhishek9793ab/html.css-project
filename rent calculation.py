rent=int(input("Enter the hostel/flat rent="))
food=int(input("Enter the amount of food orderd="))
spend_electricity=int(input("Enter the total spend electricty="))
charge_per_unit=int(input("Enter the charge per unit="))
total_bill=spend_electricity*charge_per_unit
output=(food+rent+total_bill)
print("Enter the person will pay=",output)