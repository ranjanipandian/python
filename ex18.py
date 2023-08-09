# Automatic pizza order program


size=(input("Enter the size of pizza you needed:"))
bill=0
if size=='S' or size=='s':
    bill+=100
    print(f"Small Pizza is 100")
elif size=='M' or size=='m':
    bill+=200
    print(f"Medium size pizza is 200")
else:
    bill+=300
    print(f"Large size pizza is 300")

pepperoni=input("Do you want pepperoni?")
if pepperoni=='Y' or 'y':
    if size=='S' or size=='s':
        bill+=30
    else:
        bill+=50

extracheese=input("Do you want extracheese?")
if extracheese=='Y' or 'y':
    if size=='S' or size=='s':
       bill+=40
    else:
       bill+=50

print(f"Your final bill is{bill}")

