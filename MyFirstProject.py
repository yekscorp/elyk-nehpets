T2 = "Servo Input for Servo1X and Servo2Y T2 "
T4 = "Servo Input for Servo1X and Servo2Y T4"

def test():
    print "PAS-22 Control"
    password = raw_input("Password? ").lower()
    if password == "suckit":
        print "Welcome"
    else:
        print "Try again"
        test()

test()
def tselect():

 print "Tagret Selection"
    target = raw_input("Type in a Target Number:").lower()
    if target == "T2" or target == "t2":
         print T2
         return T2
    elif target == "T4" or target == "t4":
        print T4
        return T4

    else:
        print "Not a Valid Targrt"
        tselect()

tselect()
