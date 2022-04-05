import numpy as np

### 0.3 Excercises
print("0.3 Exercises: ")
list_1= list(range(1,11))
print("E1) ", list_1)

list_2=list(range(11,21))
list_2=[float(x) for x in list_2]
print("E2) ", list_2)

list_stringForm=["one","two","three"]
list_1[:3]=list_stringForm
print("E3) ", list_1)

list_tuple=["eleven","twelve","thirteen"]
list_2[:3]=list_tuple
print("E4) ", list_2)

joint_1=[]
joint_1.extend(list_1)
joint_1.extend(list_2)
joint_2= list_1+list_2
print("E5i) ", joint_1)
print("E5ii) ", joint_2)

def list_shift(base_list, new_data):

    for x in new_data:
        base_list.pop(0)

    base_list+=new_data
    return base_list

fixed_len_list = [1,2,3,4]
new_data=[5,6,7]
print("E6) ", list_shift(fixed_len_list,new_data))

### 1.4 Excercises
print("1.4 Exercises: ")
commands = ["STATUS", "ADD", "COMMIT", "PUSH"]
for x in commands:
    print(x)
other_commands=["PUSH FAILED", "BANANAS", "PUSH SUCCESS", "APPLES"]
text = "SUCCESS"
print("SUCCESS" in "SUCCESS")  # TRUE
print("SUCCESS" in "ijoisafjoijiojSUCCESS")  # TRUE
print("SUCCESS" == "ijoisafjoijiojSUCCESS")  # FALSE
print("SUCCESS" == text)  # TRUE
# the == is going character by character and the in is going through the second string and searching for the first
print("5) the == is going character by character and the in is going through the second string and searching for the first")
i=0
while i<len(other_commands):
    if text in other_commands[i]:
        print("This worked!")
        break

    else:
        print(other_commands[i])
    i+=1


### 2.2 Excercises
fName="zach"
byte_name=fName.encode('utf-8')
byte_name_bad=byte_name+b'\xef'

#4 UnicodeDecodeError: 'utf-8' codec can't decode byte 0xef in position 4: unexpected end of data
#5
def decodeMyBytes(byte_to_decode):
    try:
        byte_to_decode.decode()
        return byte_to_decode
    except UnicodeDecodeError:
        return ""
#6
print(decodeMyBytes(byte_name))
print(decodeMyBytes(byte_name_bad))

