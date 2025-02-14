out = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"
# len(out) == 237 
lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"
chars = ""

cur = [] 
for i in range(len(out)):
    cur.append(lookup2.index(out[i]))


for i in range(1, len(cur)): 
    prev = cur[i-1]
    cur[i] += prev
    cur[i] = cur[i]%40 

for i in range(len(cur)): chars += lookup1[cur[i]]
    
print(chars)
