# login = "Isroil"
# parol = "1234567"
  
# a = input("Loginni kiritin:")
# b = input("Parolni kiriting:")


# if   login == a:
#       if parol == b:
#           print("Salom Admin")
#       else:
#          print("Sizda parol noto'g'ri")
# elif:        
# else:
#       print("Login noto'g'ri")
# a = 1

# while a<900:
  
#     a+=1
#     print("Natija")
# for a in range(10):
#     print("Salom" )
# mylist =[1,2,3,4,5]


# for x in mylist:
#     print(x**2)
# def hello():
#     print("salom hammaga")


# hello()
# def ayirish(a,b):
#     print(a-b)
# ayirish(19,15)

# def karta(*raqamlar):
#     natija = 0
#     for raqam  in raqamlar:
#         natija+=raqam
#     return natija 
# print(karta(5000,10000,78000))       
# try:
#      a = int(input("A son:"))
#      b = int(input("B son:")) 
#      print(a / b)
# except ZeroDivisionError:
#      print("0 ga bo'lib bo'lmaydi")

# except ValueError:
#       print("Siz noto'g'ri qiymat kiritingiz ")

# #zero


try:
   file = open("ideeeks.html","r")
   connect = file.read()
   print(connect)

except FileNotFoundError:
    file = open("404.html","r")
    connect = file.read()
    print(connect)