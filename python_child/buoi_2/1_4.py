# for y in range (0,10,1):
#     print (y),
#     print("   "),
#bai2
# for y in range (6,102,2):
#     if 5<=y<=100:
#         print (y),
#         print ("  "),
#bai3
# for x in range (0,500,1):
#     if 100<=x<=200: 
#         if x%2==0:
#             print (x),
#     elif 300<=x<=400:
#         if x%2==1:
#             print (x),

# for x in range (101,-1,-2):
#     print 
# x=0
# while x<100:
#         if x%2==1:
#                 print (x),
#         x+=1


import random
x= random.randint(0,20)
playing = True 
while playing: 
	y= int (input ("nhap so"))
	if x>y: 
		print ("lon hon")
	elif x<y:
		print ("nho hon")
	elif x==y:	
		print("win")
		break
#baitap: minh nhap so, may doan so