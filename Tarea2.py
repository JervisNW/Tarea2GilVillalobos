def Tarea2(A,B):
    try:
        if A>=B:
            return(int(A)+int(B), int(A)-int(B),int(A)*int(B))
        else:
            return(-2)
    except:
        return(-2)

F=Tarea2(3,"f")
print(F)
            
