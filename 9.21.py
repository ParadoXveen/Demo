sumn=int(input('样本总数x(2<x<300'))
pre=[]
while len(pre)<sumn:
    key=input("键入数值，每个用空格分开，可换行")
    nat=map(float,key.split())
    pre.extend(nat)
print("calculating...")
pre.sort()
pre=pre[1:-1]
res1=sum(pre)/len(pre)

res2=abs(pre[-1]-res1) if abs(pre[-1]-res1)>abs(pre[0]-res1) else abs(pre[0]-res1)
print('result:','%.2f'%res1,"%.2f"%res2)
