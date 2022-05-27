class Numbers:

    def _init_(self):

        pass

    def iterator(self,num):

        l = []

        for i in range(num):

            l.append(i+1)

        return iter(l)



n=int(input("enter no. :"))    

m = Numbers()

lis = m.iterator(n)

for i in range(n):

    print(next(lis))
