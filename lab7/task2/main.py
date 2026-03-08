import random

from models import ITStudent, KMAStudent

sanurik = KMAStudent("Alexander", 20)
rodik = ITStudent("Rodion", 19)

first = random.choice([sanurik,rodik])
while(sanurik.is_alive() and rodik.is_alive()):
    if first == rodik:
        rodik.attack(sanurik)
        sanurik.attack(rodik)
    else:
        sanurik.attack(rodik)
        rodik.attack(sanurik)
    print("-------HEALTH-------")
    print(f"Rodion | {rodik.get_health()}")
    print(f"Alexander | {sanurik.get_health()}")
    print("--------------------")

winner = rodik if rodik.is_alive() else sanurik

print(f"{str(winner)} has won the fight!!!")
