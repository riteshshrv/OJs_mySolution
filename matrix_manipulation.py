class matrix_manipulation:
    def print_serial(self,a):
        for i in a:
            for j in i:
                print (j," ",end="")

    def print_reverse(self,a):
        for i in reversed(a):
            for j in reversed(i):
                print (j," ",end="")

    def print_spiral(self, matrix):
        i_max=len(matrix)-1
        j_max=len(matrix[0])-1
        i_min,j_min,d=0,0,0
        while(i_min<=i_max and j_min<=j_max):
            if d==0:
                for k in range (j_min,j_max+1):
                    print(matrix[i_min][k])
                i_min+=1
            elif d==1:
                for k in range (i_min,i_max+1):
                    print(matrix[k][j_max])
                j_max-=1
            elif d==2:
                for k in range (j_max,j_min-1,-1):
                    print(matrix[i_max][k])
                i_max-=1
            elif d==3:
                for k in range (i_max,i_min-1,-1):
                    print (matrix[k][j_min])
                j_min+=1
            d=(d+1)%4

    def pretty_print(self,n):
        t=1+(n-1)*2
        matrix=[[None for x in range(t)] for x in range(t)]
        i_max=len(matrix)-1
        j_max=len(matrix[0])-1
        i_min,j_min,d,c=0,0,0,0
        while(i_min<=i_max and j_min<=j_max):
            if d==0:
                for k in range (j_min,j_max+1):
                    matrix[i_min][k]=n
                i_min+=1
            elif d==1:
                for k in range (i_min,i_max+1):
                    matrix[k][j_max]=n
                j_max-=1
            elif d==2:
                for k in range (j_max,j_min-1,-1):
                    matrix[i_max][k]=n
                i_max-=1
            elif d==3:
                for k in range (i_max,i_min-1,-1):
                    matrix[k][j_min]=n
                j_min+=1
            
            d=(d+1)%4
            c+=1
            if c%4==0:
                n-=1
        print(matrix)

def main():
    a=[[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    #a=[[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21,8], [13, 12, 11, 10, 9]]
    m=matrix_manipulation()
    m.print_serial(a)
    print("\n")
    m.print_reverse(a)
    print("\n")
    m.print_spiral(a)

if __name__ == "__main__": main()
    

            
