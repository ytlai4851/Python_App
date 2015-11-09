f = open("C:\\Users\\user\\Downloads\\bricks", "rb")
w=open('C:\\Users\\user\\Downloads\\bricks1111','wb')

iv = [0x43, 0x41, 0x53, 0x48]
header = [0x24, 0x58, 0x4d, 0x54]
key=[ 0x42, 0x49, 0x5a, 0x5a]
data=[]

for i in xrange(769180):
	data.append(ord(f.read(1)))

for i in xrange(192295):
	tem=[]
	for j in xrange(4):
		tem.append(data[i*4+j]^key[j]^iv[j])
		iv[j]=data[i*4+j]
		w.write(chr(tem[j]))