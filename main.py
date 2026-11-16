import os,json,urllib.request as w;V=(0,100,320,330,500,900,0);ND=(33,18,-14,-31,-33,-18,14,31);BD=(15,17,-15,-17);RD=(1,16,-1,-16);KD=BD+RD
SQ=[s for s in range(128)if not s&136];CM={4:12,0:13,7:14,116:3,112:7,119:11};BUD=70000
def ok(t):return-1<t<128 and not t&136
def HY():return(bytes([p+6 for p in B]),S)
def A(s,by):
 for ds,pv in(((-15*by,-17*by),1),(ND,2),(KD,6)):
  for o in ds:
   t=s+o
   if ok(t)and B[t]==pv*by:return 1
 for o in KD:
  t=s+o
  while ok(t)and not B[t]:t+=o
  if ok(t)and B[t]*by in(5,3 if o in BD else 4):return 1
 return 0
def G(cap):
 ms=[]
 for s in SQ:
  p=B[s]
  if not p or(p>0)^(S>0):continue
  a=abs(p)
  if a==1:
   d=16*S
   for dd in(d-1,d,d+1):
    t=s+dd
    if dd==d:
     if B[t]or(cap and(t>>4)not in(0,7)):continue
    elif not ok(t)or not((B[t]and(B[t]>0)^(S>0))or t==E):continue
    if(t>>4)in(0,7):ms+=[s|t<<7|q<<14 for q in(5,4,3,2)]
    else:
     ms.append(s|t<<7)
     if dd==d and(s>>4)==(7-5*S)//2 and not B[s+2*d]:ms.append(s|(s+2*d)<<7)
  else:
   ds=(0,0,ND,BD,RD,KD,KD)[a];sl=2<a<6
   for o in ds:
    t=s+o
    while ok(t):
     q=B[t]
     if q:
      if(q>0)^(S>0):ms.append(s|t<<7)
      break
     if not cap:ms.append(s|t<<7)
     if not sl:break
     t+=o
 if not cap:
  e=K[S];cb=4-3*(S>0)
  for bb,dd in((cb,1),(cb*2,-1)):
   if C&bb and not(B[e+dd]or B[e+2*dd]or(dd<0 and B[e+3*dd]))and all(not A(e+i*dd,-S)for i in(0,1,2)):ms.append(e|e+2*dd<<7)
 return ms
def M(m):
 global S,C,E
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;p=B[f];cap=B[t];u=[cap,C,E,-1]
 if p*p==1 and t==E:
  u[3]=t-16*S;u[0]=B[u[3]];B[u[3]]=0
 B[f]=0;B[t]=pr*S if pr else p
 if p*p==36:
  K[S]=t
  if abs(t-f)==2:
   df=1 if t>f else-1;rf=f+(3 if df>0 else-4);B[f+df]=B[rf];B[rf]=0
 E=t-16*S if p*p==1 and t-f==32*S else-1
 C&=CM.get(f,15)&CM.get(t,15);S=-S
 return u
def U(m,u):
 global S,C,E
 cap,oc,oe,ct=u;S=-S;f=m&127;t=(m>>7)&127;pr=(m>>14)&7;p=B[t]
 B[f]=S if pr else p;B[t]=cap if ct<0 else 0
 if ct>=0:B[ct]=cap
 if p*p==36:
  K[S]=f
  if abs(t-f)==2:
   df=1 if t>f else-1;rf=f+(3 if df>0 else-4);B[rf]=B[f+df];B[f+df]=0
 C,E=oc,oe
def W():
 s=0
 for q in SQ:
  p=B[q]
  if not p:continue
  a=abs(p);r=q>>4;f=q&7;rr=r if p>0 else 7-r;c=min(f,7-f)+min(r,7-r);v=V[a]
  if a==1:v+=rr*4
  elif a==6:v-=c*5
  s+=v if p>0 else-v
 return s
def F(d,a,b,ply):
 global N
 N+=1
 if N>BUD:raise Exception
 c=A(K[S],-S);tm=0
 if d<=0:
  if not c:
   st=S*W()
   if st>=b:return b
   if st>a:a=st
  ms=G(0 if c else 1)
 else:
  y=HY();e=T.get(y);tm=e[3]if e else 0
  if e and e[0]>=d and(e[1]==0 or e[2]>=b):return e[2]
  ms=G(0)
 def sk(m):
  if m==tm:return 1<<27
  f=m&127;t=(m>>7)&127;v=B[t]
  if v or(abs(B[f])==1 and t==E):return(1<<24)+V[abs(v)if v else 1]*16
  if m==KLR.get(ply):return 1<<22
  return 0
 ms.sort(key=sk,reverse=True)
 a0=a;bst=-10**9;lg=0
 for m in ms:
  u=M(m)
  if A(K[-S],S):U(m,u);continue
  lg+=1;nd=0 if d<=0 else d-1+c
  sc=-F(nd,-b,-a,ply+1)
  U(m,u)
  if sc>bst:bst=sc;bmv=m
  if sc>a:a=sc
  if a>=b:
   if d>0 and not u[0]:KLR[ply]=m
   break
 if not lg:return-900000+ply if c else(a if d<=0 else 0)
 if d>0 and bst>a0:T[y]=(d,1 if bst>=b else 0,bst,bmv)
 return bst if d>0 else a
def BM():
 global N
 N=0;root=0;rh=HY()
 for d in range(1,60):
  try:
   F(d,-10**9,10**9,0);root=(T.get(rh)or[0,0,0,root])[3]
  except Exception:break
 if not root:root=G(0)[0]
 return u(root)
def u(m):
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 return"%c%d%c%d%s"%(97+(f&7),(f>>4)+1,97+(t&7),(t>>4)+1,"__nbrq"[pr]if pr else"")
def ST(moves):
 global B,S,C,E,K,T,KLR
 B=[0]*128
 for i,v in enumerate((4,2,3,5,6,3,2,4)):B[i]=v;B[112+i]=-v;B[16+i]=1;B[96+i]=-1
 S=1;C=15;E=-1;K={1:4,-1:116};T={};KLR={}
 for x in moves:M(next(m for m in G(0)if u(m)==x))
def main():
 url=os.environ["MAKEFUN_ENV_URL"]
 post=lambda p,o:json.loads(w.urlopen(w.Request(url+p,json.dumps(o).encode())).read())
 while 1:
  g=post("/game",{})
  if g["status"]=="done":return
  while g["status"]=="your_move":
   ST(g["moves"]);mv=BM()
   if mv not in g["legal_moves"]:mv=g["legal_moves"][0]
   g=post("/move",{"game":g["game"],"move":mv})
if __name__=="__main__":main()
