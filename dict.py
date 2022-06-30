"dictionary:it is a data type python. it is represented as{ : } . dict it is a combination of 'keyvalue pair' "
'the value can be accessed with the help of a key . dict can have a several data types in it .'
'it can also have one more dict inside it '
# a={1:'prava',
#    2:'niha',
#    3:1,
#    'r':'frnds'}
# print(a[1])    #  'prava'
# print(a[2])    #   'niha'
# print(a[3])    #   1
# print(a['r'])  #  'frnds'
# print(a[23])   #   key error 

   #       "dictionary _ methods"
# a={1:"", 2:'prava', 3:15, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}}
# a.clear()
# print(a)    #   {} when it is a empty curly set then is know as 'dictionary set{}'   

# a={1:"", 2:'prava', 3:15, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}}   # it is a get 
# print(a.get(2))    # 'prava'
# print(a.get(8))     # {1:'cute'}
# print(a.get(11))    #  none  if the key is there. it will show the value but ,if the key is not there then it shows "none"

'if we want to add the value or variable to the key , then we use fromkeys'
# a={1,2,3,4,5,6,7}  # it is a fromkeys 
# print(dict.fromkeys(a,'good'))  # {1:'good', 2:'good', 3:'good', 4:'good', 5:'good', 6:'good', 7:'good', 8:'good'} 
# print(dict.fromkeys(a))    # it is give none {1:none,2:none,3:none} like this

'if we want to remove a particular value in the key, then we use pop '
# a={1:"", 2:'prava', 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}}
# # a.pop(2)
# # print(a)  # {1:"", 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}}
# a.pop(22)
# print(a)    #  keyerror:22 bcoz 22 value is not there in the key 
'if we want to remove the last keyvalue pair use to remove popitem'
# a={1:"", 2:'prava', 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}}
# a.popitem()
# print(a)    #  {1:"", 2:'prava', 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}}

'if we want to add & remove the keyvalue pairs then we use update '
# a={1:"", 2:'prava', 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}}
# # a.update({1:'good'})
# # print(a)  #  {1:'good', 2:'prava', 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}}
# a.update({10:'python'})
# print(a)    # {1:"", 2:'prava', 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}, 10:'python'}

'''in setdefault if we add the keyvalue ,it doesn't add but, we cannot replace the keyvalue '''
# a={1:"", 2:'prava', 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}}
# # a.setdefault(2,'hi')
# # print(a)   # the same input will come bcoz we cannot add 
# a.setdefault(10,22)
# print(a)   # a={1:"", 2:'prava', 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}, 10:22}

a={1:"", 2:'prava', 3:13, 4:0.1, 5:[1,8], 6:(2,6), 7:{3,5}, 8:{1:'cute'}}
# print(a.keys())# {1, 2, 3, 4, 5, 6, 7, 8}
print(a.values())   # a={"", 'prava', 13, 0.1, [1,8], (2,6), {3,5}, {1:'cute'}}




