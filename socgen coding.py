inp=[3,3,3,3]
c=0
for i in range(len(inp)):
    if inp[i]==inp[0]:
        c+=1
        
if c==len(inp):
        print("isequal")
for i in range(len(inp)):
    
    if inp[i]%inp[0]==0:

        print("isarithmetic")
        break
    else:
        print("other")
