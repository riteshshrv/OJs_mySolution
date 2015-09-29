def spiral_2(matrix):
    i_max=len(matrix)-1
    j_max=len(matrix)-1
    i_min,j_min,d=0,0,0
    #result=[]
    n=1
    while(i_min<=i_max and j_min<=j_max):
            if d==0:
                for k in range (j_min,j_max+1):
                    matrix[i_min][k]=n
                    #result.append(matrix[i_min][k])
                    n+=1
                i_min+=1
            elif d==1:
                for k in range (i_min,i_max+1):
                    matrix[k][j_max]=n
                    #result.append(matrix[k][j_max])
                    n+=1
                j_max-=1
            elif d==2:
                for k in range (j_max,j_min-1,-1):
                    matrix[i_max][k]=n
                    #result.append(matrix[i_max][k])
                    n+=1
                i_max-=1
            elif d==3:
                for k in range (i_max,i_min-1,-1):
                    matrix[k][j_min]=n
                    #result.append(matrix[k][j_min])
                    n+=1
                j_min+=1
            d=(d+1)%4
    return matrix

x=[[None for x in range(3)] for x in range(3)]
print(spiral_2(x))