def gameover(dood):
    print("helaas,", dood)
    print("G A M E  O V E R")
    
    


def cijfercheck(vraag, antwoord1, antwoord2):
    print(vraag)
    while True:
     print(antwoord1,"=1")
     print(antwoord2,"=2")
     antwoord=input(" ")
     if antwoord!="1" and antwoord!="2":
         print("dat is geen '1' of '2'")
     if antwoord=="1":
         return int(antwoord)
         break
     if antwoord=="2":
         return int(antwoord)  
         break


       
    

print("hallo!")
print("deze 'game' gaat over een jongen die in een wereld is belandt die hij niet kent.")
print("je moet proberen te overleven, ik stel een vraag bijvoorbeeld:")
print("je ziet een boom met vreemd fruit dat je niet kent, je kunt twee dingen kiezen:")
print("1 (het fruit eten)  2 (verderlopen)")
print("dan zou je bijvoorbeeld '1' kunnen invullen")
print("oke, nu is het jouw beurt!")
print("")
if cijfercheck("je wordt ergens wakker waar je nog nooit bent geweest! je kunt twee dingen kiezen:", "eten zoeken", "een slaapplek zoeken")==1:
    if cijfercheck("je vindt een boom met fruit dat je nog nooit hebt gezien! je kunt twee dingen kiezen:", "het fruit eten", "verderlopen")==1:
        print("je eet het fruit.")
        gameover("het fruit was vergiftigd!")
        
    else:
        print("je loopt verder, je ziet niks meer dat eetbaar lijkt.")
        if cijfercheck("je ziet wel een grot met een meer, je kunt twee dingen kiezen", "slapen in de grot", "verderlopen")==1:
            print("Goed zo!")

else:
    print("2")



