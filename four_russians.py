import  sys

# Approximation of logarythm
def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

def lower(x):
    n = x
    n = int(n)
    return n

def upper(x):
    n=x
    if float(n).is_integer():
        return n
    else :
        n += 1
        n = int(n)
        return n

def subA(A,i,m):
    Ai = []

    for k in range (len(A)):
        line = []
        for l in range(i*m-m,i*m,1):
            if l < len(A[0]):
                line.append(A[k][l])
            else :
                line.append(0)
        Ai.append(line)
    return Ai


def subB(B,i,m):
    Bi = []
    zeroLine = []

    for j in range(len(B[0])):
        zeroLine.append(0)

    for j in range(m):
        if (m*i)-(m-j) < len(B):
            Bi.append(B[(m*i)-(m-j)])
        else :
            Bi.append(zeroLine)
    return Bi

def rowFromBottom(a,n):
    c = a[len(a)-1-n]
    return c

def addArray(a,b):
    Alen = len(a)
    c=[]

    for i in range(Alen):
        c.append(a[i]|b[i])
    return c

#a: small b: big
def addMatrix(a,b):

    c=[]

    Arows = len(a)
    Acolumns = len(a[0])
    Brows = len(b)
    Bcolumns = len(b[0])


    for i in range(Brows):
        line = []
        for j in range(Bcolumns):
            if (i in range(Arows)) and (j in range(Acolumns)):
                k = a[i][j] | b[i][j]
            else :
                k = b[i][j]
            line.append(k)
        c.append(line)
    return c

def addRowMatrix (A,r,offset):
    C = []
    for i in range(len(A)):
        if i == offset :
            C.append(r)
        else :
            C.append(A[i])
    return C

def addItemMatrix (A,x,n,m):

    C = []
    editLine = []

    for i in range(len(A[0])):
        if i != n :
            editLine.append(A[m][i])
        else :
            editLine.append(x)
    Arows = len(A)

    for i in range(Arows):
        if i != m:
            C.append(A[i])
        else :
            C.append(editLine)
    return C

def alignMatrix(a,n,rowOffset,columnOffset):
    c = []
    Arows = len(a)
    Acolumns = len(a[0])

    for i in range(n):
        line = []
        for j in range(n):
            if j >= columnOffset  and j-columnOffset < Acolumns and i >= rowOffset and i-rowOffset < Arows :
                line.append(a[i-rowOffset][j-columnOffset])
            else :
                line.append(0)
        c.append(line)
    return c

def createZeroMatrix(n, m):
    array = []
    line = []

    for i in range(m):
        line.append(0)
    for i in range(n):
        array.append(line)
    return array

def createOneMatrix(n):
    A = []
    line = []

    for i in range(n):
        line = []
        for j in range(n):
            if i == j :
                line.append(1)
            else :
                line.append(0)
        A.append(line)
    return A

def num(a):
    l = len(a)
    x=0

    for i in range(l):
        x = x + a[i]*pow(2,l-i-1)
    return x

# Convert Files to usable Litst
def fileToMatrix(f):

    n=0
    formatedLine = []
    array = []

    file = open(f,"r")
    line = file.readline()

    while len(line)>0:

        for i in range(len(line)):
            if line[i]=="0":
                formatedLine.append(0)
            elif line[i]=="1":
                formatedLine.append(1)

        array.append(formatedLine)
        formatedLine = []
        line = file.readline()

    return array

def fileToGraph(f):
    n=0
    formatedLine = []
    array = []

    file = open(f,"r")
    line = file.readline()

    while len(line)>0:

        for i in range(len(line)):
            if line[i]!="," and line[i]!=" " and line[i]!="\n":
                k = int(line[i])
                formatedLine.append(k)

        array.append(formatedLine)
        formatedLine = []
        line = file.readline()

    return array

#print Arrays
def printMatrix(array):
    for i in range(len(array)):
        line = array[i]
        for j in range(len(line)):
            sys.stdout.write(chr(line[j]+48))
            if j+1 != len(line):
                sys.stdout.write(",")
        print("")

def graphToMatrix(graph):
    n = 0

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]>n:
                n = graph[i][j]

    C = createZeroMatrix(n+1,n+1)

    for i in range(len(graph)):
        C = addItemMatrix(C,1,graph[i][1],graph[i][0])

    return C

def matrixToGraph(A):
    graph=[]

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]==1:
                graph.append([i,j])

    return graph

def closure():
    print("closure")
    inGraph = fileToGraph(sys.argv[1])
    C1 = graphToMatrix(inGraph)
    C2 = createOneMatrix(len(C1))
    C = mult(C1,addMatrix(C1,C2))
    printMatrix(matrixToGraph(C))

    return 0


def mult(A,B):

    n = len(A)
    m = lower(ln(n))
    C = createZeroMatrix(n, n)

    for i in range (int(upper(float(n)/float(m)))):

        Ai = subA(A,i+1,m)
        Bi = subB(B,i+1,m)

        rs=createZeroMatrix(1,n)
        bp = 1
        k =0

        for j in range(pow(2,m)):
            rs.append(addArray(rs[j+1-pow(2,k)],rowFromBottom(Bi,k)))
            if bp==1 :
                bp = j+1
                k = k+1
            else:
                bp = bp+1

        Ci = createZeroMatrix(n,n)

        for j in range(n):
            Ci = addRowMatrix(Ci,rs[num(Ai[j])],j)

        C = addMatrix(C,Ci)
    return C

if len(sys.argv)==2:
    closure()
elif len(sys.argv)==3:
    A = fileToMatrix(sys.argv[1])
    B = fileToMatrix(sys.argv[2])
    printMatrix(mult(A,B))
else :
    print("please insert correct arguments")
