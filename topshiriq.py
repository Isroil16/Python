# 1-fuksiya
# son = int(input("Biron bir son kiriting >>>"))
# s= 0
# for a in range(son):
#      s+=a
# print(s)
# 2-fuksiya

# son = int(input("Biron bir son kiriting >>>"))
# a =list()
# a.append(son)
# print(a)
import random
def son_top(x = 37):
    global taxminlar
    tasodifiy = random.randint(25,37)
    taxminlar = 0
    print(f"Men 25 dan {x} gacha son o'yladim. Topa olasizmi")
    while True:
        taxminlar +=1
        taxmin = int(input(">>>"))
        if tasodifiy > taxmin:
            print("Men o'ylagan son kattaroq.Yana o'rinib kuring")
        elif tasodifiy <taxmin :
            print("Men o'ylagan son kichikroq.Yana o'rinib kuring")
        else :
             break
    print(f"Tabriklaymiz Topdingiz.Men {tasodifiy} sonini uylagan edim. {taxminlar} taxmin bilan topdingiz !!! \n")
    print(f"1 dan 10 gacha son o'ylang. Men topishga xarakat qilaman.\n")
    return taxminlar



def sontop_pc(x=10):
    global sonlar
    input(f"Son o'ylagan bulsangiz  istalgan tugmani bosing.Men topaman >>>")
    quyi =1
    yuqi = x
    sonlar = 0
    while True:
        sonlar +=1
        if quyi != yuqi:
            taxmin_buldi = random.randint(quyi,yuqi)
        
        else :
            taxmin_buldi = quyi
        javob = input(f"\nSiz {taxmin_buldi} soni uylagansiz.To'g'ri(t) katta bulsa(+) yoki (-) >>>".lower())

        if javob == '-':
            yuqi = taxmin_buldi - 1
        elif javob =="+":
            quyi = taxmin_buldi +1
        else:
            break
    print(f"\nTabriklaymiz.Kompyuter {sonlar} taxmin bilan topdi.\n")
    return sonlar
    
def play( x= 10):
    yana = True
    while yana:
        play_son = son_top(x)
        play_pc = sontop_pc(x)
        if play_son>play_pc:
            print(f"Kompyuter {play_pc} taxmin bilan topib yutdi\n")
        elif play_son<play_pc:
            print(f"Siz {play_son} taxmin bilan topib yutdingiz\n")
        else:
            print(f"Durrang. Ikkimiz ham {play_son} taxmin bilan topdik\n")
        yana = int(input("Yana o'ynaysizmi? Ha(1) / Yo'q(0) >>>"))

play( x= 10)


