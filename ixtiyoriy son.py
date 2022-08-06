import random 

    
while True:
      if True :
          
         s =( random.randint(1, 50))
         d=( random.randint(1, 50))
         try:
             e =int(input(f" Bu dasturdan chqish uchun 123 deb yozing \n {s} + {d} = "))
             z = s+d
             if z == e:
                      print(" To'g'ri")
         
             elif e ==123:
                  print(" Dastur to'xatadi")    
                  break
             else:
                print(" Noto'g'ri")
    
         except:
            print(" Notug'ri ma'lumot kitingiz")

     
