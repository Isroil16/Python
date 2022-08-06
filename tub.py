


while True:
    while True:
        try:
            n = int(input("Bu dasutr tub sonlarni aniqlaydi (dasturdan chiqish \nuchun 1 ni kiriting) Biron bir son kiriting >>> "))
        except:
            print("Notug'ri son kiritildi")
        try:
            if n>0:
               break
        except:
            print("0 dan katta son kiriting")
    
    tub = True
    m=2
    for i in range(1,n-1):
         if n%m==0:
             tub=False
        
    m=m+1
    if tub==True:
        print(f" {n} soni tub son" ,end='\n')
        if n==1:
           print(" ham murakkab son ham emas")
           break
    else:
         print(f" {n} soni tub son emas")
   
print("\n Dastur tugadi") 




   
   
   
   
   
   
   
   
   
 #  for (i=2; i<$n ; $i++) { 
  # 	if ($n%$i==0){
  # 		$tub =false;
   #	}
   #}
   #// if ($n==1) {
   #// 	echo $n ." soni tub ham murakkab ham son emas";
   #// }
   #if ($tub==true) {
   #	echo $n." soni tub son";
    # if ($n ==1) {
   #		echo " ham murakkab son ham emas";
   #	}
   	
   		
   #}
   #else{
   	#echo $n. " soni tub son emas";
   #}
   
