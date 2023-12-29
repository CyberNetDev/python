import random 
def notation_numerique(score):
    score=int(score)
    if score < 10:
        print("Reveillez vous avant qu'il soit trop tard !!!!")
        print('★' * score)
    elif score >=10 and score <12:
        print("Passable")
        print('★' * score)
    elif score >= 12 and score <14:
        print ("Assez bien")
        print('★' * score)
    elif score >= 14 and score <16:
        print("Bien")
        print('★' * score)
    elif score >= 16 and score <18:
        print("Tres bien ")
        print('★' * score)
    elif score >= 18 and score <=20:
        print("Execellent")
        print('★' * score)
    elif score > 20:
        print("Eleve depansent son maitre")
        print('★' *  score)
    

#resultat = int( &input("Veillez saisir la note de l'eleve "))  # Score sur 10
for i in range(0,11) :
    s=random.random()*10
    print ("la note : ",s)
    notation_numerique(s)