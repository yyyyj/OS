t=[0b1,0b11,0b1001,0b101,0b1100,0b101,0b1101,0b1111]
def crypt(s,c):
 s,m,e,c=s%len(t),list(map(lambda x:ord(x)<<s,c)),[],1
 for(i,m)in enumerate(m):(e,c)=(e+[(t[_]<<s)^c for(_)in range(s)]+[m],c+1)if(not i%s)else(e+[m],c)
 return(e)
def decrypt(u):
 f,d,a,r,o=u[0]^1,0,[],0,0
 while(f!=t[0]):d,f=d+1,f>>1
 for(i,m)in enumerate(u):v=a.append(m) if o else None;r+=1;o=(~o)if(not r%d)else(o)
 return("".join(chr(c>>d)for(c)in a))

if(__name__=='__main__'):print(crypt(int(input("sel> ")), input("message> ")))
