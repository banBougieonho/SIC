fh = open("test.txt","w")
for i in range(6):
    data = f"Dong thu {i+1}"
    fh.write(data)
fh.close()
