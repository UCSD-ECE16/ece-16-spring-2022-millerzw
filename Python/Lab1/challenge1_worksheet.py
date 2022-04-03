import numpy as np

### 0.3 Excercises
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

