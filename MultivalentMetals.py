questions = []
answers = []
import random
n = 0

def multivalent (answer, question):
    questions.append(question)
    answers.append(answer)

multivalent("Copper I","cuprous")
multivalent("Copper II", "cupric")
multivalent("Gold I","aurous")
multivalent("Gold III", "auric")
multivalent("Mercury I","mercurous")
multivalent("Mercury II","mercuric")
multivalent("Chromium II","chromous")
multivalent("Chromium III","chromic")
multivalent("Manganese II","manganous")
multivalent("Manganese III","manganic")
multivalent("Iron II","ferrous")
multivalent("Iron III","ferric")
multivalent("Cobalt II","cobaltous")
multivalent("Cobalt III","cobaltic")
multivalent("Nickel II","nickelous")
multivalent("Nickel III","nickelic")
multivalent("Tin II","stannous")
multivalent("Tin IV","stannic")
multivalent("Lead II","plumbous")
multivalent("Lead IV","plumbic")
multivalent("Cerium III","cerous")
multivalent("Cerium IV","ceric")
multivalent("Arsenic III","arsenous")
multivalent("Arsenic V","arsenic")
multivalent("Antimony III","antimonous")
multivalent("Antimony V","antimonic")
multivalent("Bismuth III","bismuthous")
multivalent("Bismuth V","bismuthic")

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


    
