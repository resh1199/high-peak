class highpeak:
    def mindiff(self,n,m,a='none'):
         if a is None:
             a = []
         global res1
         res1=0
         for i in range(0 ,m):
            res1=max(res1,a[m-1]-a[i])
         return res1
    def findele(self, res2, n, m, a='none'):
         for i in range (0,n-1):
             res2=min(res2,a[m-1]-a[i])
             if res1==res2:
                 return i
         return i
    def input(self):
        arr=[999,2195,2799,4999,7980,9800,9999,11101,22349,229900]
        items=["MI Band: 999","Sandwich Toaster: 2195","Cult Pass: 2799","Scale: 4999","Fitbit Plus: 7980","Microwave Oven: 9800","Alexa: 9999","Digital Camera: 11101","Ipods: 22349","Macbook Pro: 229900"]
        f = open("demofile2.txt", "a")
        f.write("MI Band: 999",)
        f.write("Sandwich Toaster: 2195")
        f.write("Cult Pass: 2799")
        f.write("Scale: 4999")
        f.write("Fitbit Plus: 7980")
        f.write("Microwave Oven: 9800")
        f.write("Alexa: 9999")
        f.write("Digital Camera: 11101")
        f.write("Ipods: 22349")
        f.write("Macbook Pro: 229900")
        n=len(arr)
        s=input("Enter the number of Employees")
        m=int(s)
        res=h.mindiff( n, m, arr)
        f.write("Number of the Employees:{}".format(m))
        print("Number of the Employees:",m)
        startindex=h.findele(res,n,m, arr)
        f.write("Here are the goodies that are selected for distribution")
        print("Here are the goodies that are selected for distribution")
        for i in range(startindex,startindex+m):
            print(items[i])
            f.write(items[i])
        print("\n")
        print("And the difference between the choosen goodies with highest price and lowest price is : ", res)
        f.write("And the difference between the choosen goodies with highest price and lowest price is :{} ".format(res))
        f.close()
h=highpeak()
h.input()
