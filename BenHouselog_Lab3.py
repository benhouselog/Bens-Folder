speed_limit = int(input ("What is the speed limit:"))
demerit_points= 0
while True:
    speed_car = int(input ("Enter the speed of your car:"))
    if speed_car < speed_limit:
        print ("Ok")
    if speed_car > speed_limit:
        demerit_points+= (speed_car-speed_limit)/5
        print (demerit_points)
    if demerit_points >= 12:
        print("License Suspended.")
        break

    










    
    

