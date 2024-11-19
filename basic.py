# python-basic
print("MEELO EVARU KOTISWARUDU")
print("1.Questin no.1")
print("2.Questin no.2")
print("3.Questin no.3")
print("4.Questin no.4")
print("5.Questin no.5")
marks=0
print("1.what is the fullform of otp")
ans=str(input("enter your answer:"))
if(ans=="one time password"):
    print("correct answer")

    marks1=10

else:
    print("wrong answer")
    marks1=0
print("2.who is the prime minester of the India")
ans=str(input("enter your answer:"))
if(ans=="narendhra modi"):
    print("correct answer")
    marks2=marks1+10
    # print("score"marks2)
else:
    print("wrong answer")
    
    marks2=marks1
    # print("score="marks2)
print("3.which animal is known as ship of the desert")
ans=str(input("enter your answer:"))
if(ans=="camel"):
    print("correct answer")
    marks3=marks2+10
else:
    print("wrong answer")
    marks3=marks2
print("4.name of the national flower of india")
ans=str(input("enter your answer:"))
if(ans=="lotus flower"):
    print("correct answer")
    marks4=marks3+10
else:
    print("wrong answer")
    marks4=marks3
print("5.name of the national fruit")
ans=str(input("enter your answer:"))
if(ans=="mango"):
    print("correct answer")
    marks5=marks4+10
    
else:
    print("wrong answer")
    marks5=marks4
print("total score=",marks5)
                
            
            
    
