class square:
    def __init__(self,m,n):
        self.m=m
        self.n=n
        for row in range(m):
            for column in range(n):
                if(row==0 or row==m-1):
                    print("*",end="")
                else:
                    if(column==0 or column == n-1):
                        print("*",end="")
                    else:
                        print(" ",end="")
            print()
height=int(input("Please enter the height of your square/rectangle\n"))
width=int(input("Please enter the width of your square/rectangle\n"))

square(height,width)   
