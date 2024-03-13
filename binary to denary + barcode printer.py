import turtle as t
def binarytodenary():
  print("Welcome to the binary to denary calculator")
  inp = input("Which binary number would you like to change?: (Binary numbers are made of 1's and 0's only)")
  binary_code=list(inp)
  r = (len(binary_code)-1)
  index = 0
  denary_code=[]
  while r >= 0:
    if binary_code[index]=="1":
      denary_code.append(2**r)
    r = r-1
    index = index+1
  for i in range(len(denary_code)):
    denary_code[i]=int(denary_code[i])
  s=sum(denary_code)
  print(s)

def ba(number, big):
  for i in number:
    big.append(i)
    
def draw():
  t.left(90)
  t.pendown()
  t.begin_fill()
  t.forward(150)
  t.right(90)
  t.forward(3)
  t.right(90)
  t.forward(150)
  t.left(90)
  t.end_fill()
  t.penup()
def skip():
  t.penup()
  t.forward(3)

def barcodecreator():
  tn=[]
  print("Welcome to the barcode creator!")
  binary=list(input("What is your code number,(total of 12 numbers and 1 space, include 0 and 9 at the start and the end) separate the middle with the space:"))
  l0=list("0001101")
  l1=list("0011001")
  l2=list("0010011")
  l3=list("0111101")
  l4=list("0100011")
  l5=list("0110001")
  l6=list("0101111")
  l7=list("0111011")
  l8=list("0110111")
  l9=list("0001011")
  r0=list("1110010")
  r1=list("1100110")
  r2=list("1101100")
  r3=list("1000010")
  r4=list("1011100")
  r5=list("1001110")
  r6=list("1010000")
  r7=list("1000100")
  r8=list("1001000")
  r9=list("1110100")
  sides=list("101")
  middle=list("01010")
  #add left guard to total_number variable
  ba(sides,tn)
  #left side
  for i in range(6):
    if binary[i]=="0":
      ba(l0,tn)
    elif binary[i]=="1":
      ba(l1,tn)
    elif binary[i]=="2":
      ba(l2,tn)
    elif binary[i]=="3":
      ba(l3,tn)
    elif binary[i]=="4":
      ba(l4,tn)
    elif binary[i]=="5":
      ba(l5,tn)
    elif binary[i]=="6":
      ba(l6,tn)
    elif binary[i]=="7":
      ba(l7,tn)
    elif binary[i]=="8":
      ba(l8,tn)
    elif binary[i]=="9":
      ba(l9,tn)
  #middle
  ba(middle,tn)
  #right side
  for i in range(6):
    if binary[i+7]=="0":
      ba(r0,tn)
    elif binary[i+7]=="1":
      ba(r1,tn)
    elif binary[i+7]=="2":
      ba(r2,tn)
    elif binary[i+7]=="3":
      ba(r3,tn)
    elif binary[i+7]=="4":
      ba(r4,tn)
    elif binary[i+7]=="5":
      ba(r5,tn)
    elif binary[i+7]=="6":
      ba(r6,tn)
    elif binary[i+7]=="7":
      ba(r7,tn)
    elif binary[i+7]=="8":
      ba(r8,tn)
    elif binary[i+7]=="9":
      ba(r9,tn)
  #add the right guard
  ba(sides,tn)
  #print the final numbers
  for i in tn:
    t.speed(0)
    if i=="1":
      draw()
    elif i=="0":
      skip()

barcodecreator()
  
