# python-basic
print("MEELO EVARU KOTISWARUDU")
print("1.Questin no.1")
print("2.Questin no.2")
print("3.Questin no.3")
print("4.Questin no.4")
print("5.Questin no.5")
while(True):
    ch=int(input("\nchoose your quetion: "))
    match ch:
        case 1:
            print("1.what is the fullform of otp")
            ans=str(input("enter your answer:"))
            if(ans=="one time password"):
                print("correct answer")
                print("marks=",1)
            else:
                print("wrong answer")
                print("marks=",0)
        case 2:
            print("2.who is the prime minester of the India")
            ans=str(input("enter your answer:"))
            if(ans=="narendhra modi"):
                print("correct answer")
                print("marks=",2)
            else:
                print("wrong answer")
                print("marks =",1)
        case 3:
            print("3.which animal is known as ship of the desert")
            ans=str(input("enter your answer:"))
            if(ans=="camel"):
                print("correct answer")
                print("marks=",3)
            else:
                print("wrong answer")
                print("marks =",2)
        case 4:
            print("4.name of the national flower of india")
            ans=str(input("enter your answer:"))
            if(ans=="lotus flower"):
                print("correct answer")
                print("marks =",4)
            else:
                print("wrong answer")
                print("marks =",3)
        case 5:
            print("5.name of the national fruit")
            ans=str(input("enter your answer:"))
            if(ans=="mango"):
                print("correct answer")
                print("marks =",5)
            else:
                print("wrong answer")
                print("marks =",4)
            
            
    
