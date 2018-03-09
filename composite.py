a=int(raw_input())
p=0
for i in range(1,500):
  if(a%i==0):
    p=p+1
if(p==1):
  print "no"
else:
  print "yes"
