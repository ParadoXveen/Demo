firstkey=(input(' 人数及水口数，以空格间隔')).split()
peo,tap=int(firstkey[0]),int(firstkey[1])
uset=[]
sumtime=0
while len(uset)<peo:
    
  scekey=(input('各人取水量'))
  nat=map(int,scekey.split())
  uset.extend(nat)
while len(uset)>tap:
    using=sorted(uset[:tap])
    out=using[0]
    uset.remove(out)
    for i in range(tap-1):
        uset[i]=uset[i]-out
        if uset[i]==0:
            uset.remove(0)
    sumtime=sumtime+out
last=sorted(uset)
sumtime+=last[-1]

        

print(sumtime)
