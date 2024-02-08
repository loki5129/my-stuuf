a= 10
file=open("crazy.txt", "a")
while 10>0:
 file.write(" crazy I was crazy once they locked me in a room a rudder room, a rudder room with rats and the rats made me crazy")
 a=a-1
file.close
if a == 0:
     print("end")

print(a)

