print("Standard Deviation")
n = int(input("Enter the number of rows: "))
ciupper = []
cilower = []

print("Enter the class intervals")
for i in range(1, n + 1):
    x = int(input("lower limit: "))
    cilower.append(x)
    y = int(input("upper limit: "))
    ciupper.append(y)

print("Enter the frequencies")
freq = []
for i in range(1, n + 1):
    f = int(input())
    freq.append(f)

print("class interval     frequency")
for i in range (0, n) :
    print(cilower[i],"-",ciupper[i],"        ",freq[i])
xi=[]
for i in range (n) :
    x=(ciupper[i] + cilower[i])/2
    xi.append(x) 
fixi=[]   
for i in range (n) :
    x=freq[i]*xi[i]
    fixi.append(x)
sumfixi=0
for i in range (n) :
    sumfixi=sumfixi+fixi[i]
sumfi=0   
for i in range (n) :
    sumfi=sumfi+freq[i]
mean=sumfixi / sumfi
ximean=[]
for i in range (n) :
    x=xi[i] - mean 
    ximean.append(x) 
ximean2=[]
for i in range (n) :
    x = ximean[i] * ximean[i]
    ximean2.append(x) 
fiximean2=[]
for i in range (n) :
    x = freq[i]* ximean2[i]
    fiximean2.append(x) 
sumfiximean2=0   
for i in range(n) :
    sumfiximean2=sumfiximean2+fiximean2[i]
sd=(sumfiximean2/sumfi)**0.5
print ("class interval   fi     xi     fixi    fi.(xi-mean)2 ") 
for x in range (n) :
    print(cilower[x],"-", ciupper[x],"     ",freq[x],"     ",xi[x],"     ",fixi[x],"     ",fiximean2[x]) 
print("Standard deviation =", sd)
