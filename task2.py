lines=""
with open("txtd.txt","r") as f:
    for i in f:
        if "hi" in i:
            lines+=i
    print(lines)
        
