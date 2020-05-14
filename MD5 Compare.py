import hashlib


#File 1

hasher1 = hashlib.md5()
print("First File Absolute Path")
afile1 = open(input(""), 'rb')
buf1 = afile1.read()
a = hasher1.update(buf1)
md5_a=(str(hasher1.hexdigest()))
#File 2

hasher2 = hashlib.md5()
print("Second file Absolute Path")
afile2 = open(input(""), 'rb')
buf2 = afile2.read()
b = hasher2.update(buf2)
md5_b=(str(hasher2.hexdigest()))
#Compare md5

if(md5_a==md5_b):
    print("Yes")
else:
    print("No")
print(str(md5_a) == str(md5_b))
print(str(hasher1.hexdigest()))
print(str(hasher2.hexdigest()))