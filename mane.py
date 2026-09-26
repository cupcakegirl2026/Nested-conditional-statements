school_fee=2000000
total_classes=84

paid_fee=int(input("Enter the amount of money paid: "))
classes_attended=int(input("Enter the number of classes attended: "))
class_percentage=(classes_attended/total_classes)*100

if paid_fee>=school_fee:
    if class_percentage>=100:   
     print("You are eligible for the exam")

    else:
     print("You can't do the exam,you attened less classes")
else:
    print("You can't do the exam,you haven't paid the full school fee")