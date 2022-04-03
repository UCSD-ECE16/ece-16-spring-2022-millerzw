import numpy as np

a = np.array([1, 2, 3])

a = np.array([(1,2,3),(4,5,6)])

a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

myList = [1,2,9,8]
a = np.array(myList)

a = np.zeros((2,2))
a = np.ones((3,3))

a = np.array([(1,2,3),(4,5,6)])
a.reshape(3,2)

a = np.array([(1,2,3),(4,5,6)])
b = a.flatten()
b.shape # (6,) NOT (6,1)!

a = np.array([1,2,3,4,5,6,7])
b = np.resize(a, (1,4)) # array([[1, 2, 3, 4]])

array1=np.array([0,10,4,12])
def ques1():
    array1=np.array([0,10,4,12])
    array1=array1-20
    print(array1)
    # the result is [-20 -10 -16  -8], a 1x4 array
ques1()

def ques2():
    array2=np.array([(0,10,4,12),(1,20,3,41)])
    top=array2[0][2:]
    bottom=array2[1][:2]
    array2_new=np.vstack((top,bottom))
    print(array2_new)
    #I used the vstack as well as indexing
ques2()

def ques3():
    finArray=np.hstack((array1,array1))
    finArray=np.vstack((finArray,finArray,finArray,finArray))
    print(finArray)
ques3()

def ques4():
    array4a=np.arange(-3,21,6)
    print(array4a)
    array4b=np.arange(-7,-21,-2)
    print(array4b)
ques4()

def ques5():
    array5=np.linspace(0,100,49,True)
    print(array5)
    #this is different because we can specifiy the inclusion of the end value and the step number is how many
    #indexes are between, not how many to increment our number
ques5()

def ques6():
    array6=np.zeros((3,4))
    row3=np.arange(4,0,-1)
    temp=row3[1]
    row3[1]=row3[2]
    row3[2]=temp
    print(row3)

    rcorner=np.ones((2,2))
    rcorner[:,1]=rcorner[:,1]*2
    print(rcorner)

    tl_line=np.arange(12,-6,-9)
    print(tl_line)

    array6[2]=row3
    array6[0:2,2:4]=rcorner
    array6[0,0:2]=tl_line

    print(array6)

ques6()

def ques7():
    string7="1,2,3,4"
    array_numbers=string7.split(",")
    #print(array_numbers)
    full_stack=np.array(array_numbers)
    for x in range(99):
        full_stack=np.vstack((full_stack,array_numbers))
    print(full_stack)
ques7()

