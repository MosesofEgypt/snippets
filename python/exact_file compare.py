from struct import unpack
path1 = "marine.model_animations"
path2 = "marine.ORIG.model_animations"

with open(path1, "br") as f:
    file1 = f.read()
    
with open(path2, "br") as f:
    file2 = f.read()

found = False
diff = 0
for i in range(len(file1)):
    if file1[i] != file2[i]:
        diff += 1
    elif diff:
        print('    %s difference of %s bytes' % (i - diff, diff))
        diff = 0
        found = False

print('finished')
input()
