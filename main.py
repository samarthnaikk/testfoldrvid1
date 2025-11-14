s=""
for i in range(1,5):
    f=open(f"data/text{i}.txt",'r')
    s+=f.read()
    f.close()

f=open("final.txt","w")
f.write(s)
f.close()

print("executed all commands")
f=open("final.txt","r")
f.read()
f.close()