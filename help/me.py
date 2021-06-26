class railway():
    def __init__(self,fr,to,db):
        self.fr=fr
        self.to=to
        self.db=db
        self.k=0
    def fare(self,age,a,b):
       #FARE
        ch=23
        tsp=3.68
        k=0
        #babies
        if age<=5:
            charge=0
            coach=0
            seat=0
        #child
        elif age>=6 and age<=12:
            if a=='gen' and b=='sl':
                charge=ch+tsp+450
            elif a=='gen' and b=='st':
                charge=ch+225+tsp
            elif a=='1t' and b=='sl':
                charge=ch+800+tsp
            elif a=='1t' and b=='st':
                charge=ch+575+tsp
            elif a=='2t' and b=='sl':
                charge=ch+700+tsp
            elif a=='2t' and b=='st':
                charge=ch+475+tsp
            elif a=='3t'and b=='sl':
                charge=ch+600+tsp
            elif a=='3t' and b=='st':
                charge=ch+375+tsp
    #adult
        elif age>=13and age<=60:
            if a=='gen' and b=='sl':
                charge=ch+900+tsp
            elif a=='gen' and b=='st':
                charge=ch+450+tsp
            elif a=='1t' and b=='sl':
                charge=ch+1600+tsp
            elif a=='1t' and b=='st':
                charge=ch+1150+tsp
            elif a=='2t' and b=='sl':
                charge=ch+1400+tsp
            elif a=='2t' and b=='st':
                charge=ch+950+tsp
            elif a=='3t'and b=='sl':
                charge=ch+1200+tsp
            elif a=='3t' and b=='st':
                charge=ch+750+tsp
    #senior citizen
        else:
            if a=='gen' and b=='sl':
                charge=ch+600+tsp
            elif a=='gen' and b=='st':
                charge=ch+300+tsp
            elif a=='1t' and b=='sl':
                charge=ch+1300+tsp
            elif a=='1t' and b=='st':
                charge=ch+850+tsp
            elif a=='2t' and b=='sl':
                charge=ch+1100+tsp
            elif a=='2t' and b=='st':
                charge=ch+650+tsp
            elif a=='3t'and b=='sl':
                charge=ch+900+tsp
            elif a=='3t' and b=='st':
                charge=ch+450+tsp     
    #station charge       
        if to=="ers":
            self.k+=350+charge
        elif to=="tcr":
            self.k+=200+charge
        elif to=="clt":
            self.k+=200+charge
        elif to=="can":
            self.k+=200+charge
        elif to=="majn":
            self.k+=300+charge
        elif to=="mao":
            self.k+=300+charge
        elif to=="rn":
            self.k+=200+charge
        elif to=="bsr":
            self.k+=200+charge
        elif to=="st":
            self.k+=300+charge
        elif to=="brs":
            self.k+=200+charge
        elif to=="adi":
            self.k+=350+charge
        elif to=="rji":
            self.k+=200+charge
        elif to=="hapa":
            self.k+=250+charge
        elif to=="okha":
            self.k+=250+charge
        if age<=5:
            self.k=0
        
    def cls(self):
        print ('\n'*100)    
    def details(self,fr,to,db,ch,n,age,s,mn,ad):
        self.cls()
        print"____________ELECTRONIC RESERVATION SLIP____________"
        print"FROM :",fr
        print"TO :",to
        print"DATE OF BOARDING :",db
        if ch==1:
            print"train name:okha express"
        else:
            print"train name:hapa express"
        if age<=5:
            print"QUOTA:nil"
            print"CLASS:nil"
        elif age>=6 and age<=12:
            print"quota:",a
            print"class:",b
        elif age>=13 and age<=60:
            print"quota:",a
            print"class:",b
        else:
            print"quota:",a
            print"class:",b      
        print"_________PASSENGER DETAILS____________"
        import random
        coach=random.randint(1,10)
        seat=random.randint(1,60)
        if age<=5:
            coach=0
            seat=0
        print"passenger name:",n
        print"age:",age
        print"sex:",s
        print"mobile no:",mn
        print"address:",ad
        print"coach no. :",coach
        print"seat no. :",seat
        print"ticket fare=Rs",self.k
        print"____________________________________"
##main
f1=open(r"C:\Users\MY PC\Desktop\railway.txt","r")
count=raw_input("DO YOU WANT TO ENTER ?(Y/N):" )
if count=="y" or count=="Y":
    str=" "
    while str:
        str=f1.readline()
        print str,
    fr=raw_input("from:")
    to=raw_input("to:")
    db=raw_input("date of boarding:")
    ch=input("""enter train choice
            1-okha express
            2-hapa express:""")
    if ch==1 or ch==2:
        print"""        GENERAL
        1 TIER
        2 TIER
        3 TIER"""
        a=raw_input("your choice for quota(gen/1t/2t/3t):")
        print"""        SLEEPER
        SITTING"""
        b=raw_input("your choice for class(sl/st):")
        print"_________________________________________________________" 
    obj1=railway(fr,to,db)
    boktic=raw_input("do you want to book a ticket:")
    if boktic=="y" or boktic=="Y":
        np=input("enter no of passengers:")
        for i in range(np):
            n=raw_input("passenger name :")
            age=int(raw_input("age:"))
            s=raw_input("sex(m/f):")
            mn=int(raw_input("mobile no. :"))
            ad=raw_input("address:")
            obj1.fare(age,a,b)
            obj1.details(fr,to,db,ch,n,age,s,mn,ad)
       

    
        
else:
    print"THANK YOU !!!"
    print"PLEASE DO VISIT AGAIN !!!...."
f1.close()

