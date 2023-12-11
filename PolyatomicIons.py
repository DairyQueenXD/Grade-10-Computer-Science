questions = []
answers = []
import random
n = 0

def polyatomic (question, answer):
    questions.append(question)
    answers.append(answer)

polyatomic("perbromate","BrO4 1-")
polyatomic("bromate","BrO3 1-")
polyatomic("bromite","BrO2 1-")
polyatomic("hypobromite","BrO 1-")
polyatomic("perchlorate","ClO4 1-")
polyatomic("chlorate","ClO3 1-")
polyatomic("chlorite","ClO2 1-")
polyatomic("hypochlorite","ClO 1-")
polyatomic("periodate","IO4 1-")
polyatomic("iodate","IO3 1-")
polyatomic("iodite","IO2 1-")
polyatomic("hypoiodite","IO 1-")
polyatomic("nitrate","NO3 1-")
polyatomic("nitrite","NO2 1-")
polyatomic("hydroxide","OH 1-")
polyatomic("cyanide","CN 1-")
polyatomic("thiocyanate","SCN 1-")
polyatomic("acetate","C2H3O2 1-")
polyatomic("permanganate","MnO4 1-")
polyatomic("bicarbonate", "HCO3 1-")
polyatomic("carbonate","CO3 2-")
polyatomic("phthalate","C8H4O4 2-")
polyatomic("sulfate","SO4 2-")
polyatomic("sulfite","SO3 2-")
polyatomic("chromate","CrO4 2-")
polyatomic("dichromate","Cr2O7 2-")
polyatomic("oxalate","C2O4 2-")
polyatomic("peroxide","O2 2-")
polyatomic("phosphate","PO4 3-")
polyatomic("phosphite","PO3 3-")
polyatomic("arsenate","AsO4 3-")
polyatomic("ammonium","NH4 1+")

for i in range (len(questions)):
    n = random.randint(0,len(questions)-1)
    print("Question:",questions[n],"\nWhat is the answer?: ")
    answer = str(input())
    if answer == answers[n]:
        print("Correct!")
    else:
        print("Wrong! The answer is",answers[n])
    questions = questions[:n] + questions[n+1:]
    answers = answers[:n] + answers[n+1:]


    
