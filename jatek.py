import random

def gepszinek():
    szinek = ["🟥", "🟦", "🟩", "🟨", "🟧", "🟪"]
    gepszinei = []
    p = 5
    for i in range(4):
        randomindex = random.randint(0, p)
        gepszinei.append(szinek[randomindex])
        szinek.remove(szinek[randomindex])
        p -= 1
    print("ép színei (teszt):", *gepszinei,sep=" ")
    return gepszinei

def jatekos():
    print("1 = 🟥\n2 = 🟦\n3 = 🟩\n4 = 🟨\n5 = 🟧\n6 = 🟪")
    jatekoslista = []
    for i in range(0,4,1):
        tipp = int(input("tippelj egy számot: "))
        if tipp == 1:
            jatekoslista.append("🟥")
        elif tipp == 2:
            jatekoslista.append("🟦")
        elif tipp == 3:
            jatekoslista.append("🟩")
        elif tipp == 4:
            jatekoslista.append("🟨")
        elif tipp == 5:
            jatekoslista.append("🟧")
        elif tipp == 6:
            jatekoslista.append("🟪")
        else:
            print("érvénytelen")
            return jatekos()
    print()
    print(*jatekoslista,"\n",sep=" ",end="")
    return jatekoslista

def helyese(gep):
    vegjel = ""
    for o in range(0,10,1):
        jelzes = []
        jatekostipp = jatekos()
        for i in range(4):
            if gep[i] == jatekostipp[i]:
                jelzes.append("⬛")
            elif gep.count(jatekostipp[i]) > 0:
                jelzes.append("⬜")
            else:
                jelzes.append("❌")
        print("------------")
        print(*jelzes,sep=" ")
        print()
        if jelzes == ["⬛", "⬛", "⬛", "⬛"]:
            vegjel = print("************\n* Nyertél! *\n************")
            return vegjel
    vegjel = print("***************\n* Vesztettél! *\n*!*************")
    return vegjel