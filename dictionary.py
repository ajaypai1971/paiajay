 # in this file we will experiment with dictionaries
# agenda:
# create a dictionary with  diff types of values
#
# then try to print only the values for each key.
#
#     use dict.items , iteritems, dict.keys  ordereddict.
#
# also learn about.
#
# loop through dictionary usin pythonic way.. not using for loop
# resources:
 # internet and some very good tips here: link to the pdf: https://speakerd.s3.amazonaws.com/presentations/c56b00e084950130ac8e22000a1c4bc5/BeautifulCode.pdf
#https://www.youtube.com/watch?v=OSGv2VnC0go
# Raymond Hettinger
# Learn to take better advantage of Python's best features and improve existing code through a series of code transformations, "When you see this, do that instead.

#simple dict with diff types of key/value pairs


simple_dict = {"key1": "val1", "key2": "int2", "key3": 3, "key4": [0,1], "key5": {"k1": "v1", "k2": 2}}
print("the dictioary is:", simple_dict)



#to print only the keys by iterating over the keys.
# NOTE: in this fashion you may only go throguh the dict and not mutate it.
print("print only the keys")
for key in simple_dict:
     print(key)

# if you try to mutate the dict , it will throw an error like below:
# for k in simple_dict:
#      del simple_dict[k] # you are trying to mutate it here . i.e manipulating the key or values
#
# output is as below:
#      Traceback (most recent call last):
#   File "C:/Users/paiajay/dictionary.py", line 22, in <module>
#     for k in simple_dict:
# RuntimeError: dictionary changed size during iteration
#


print("printing the key value pair using simple looping")
for key in simple_dict:
     print(key , "-->" , simple_dict[key])
# you can also use items() method when looking for values in a dict. this a better pythonic way. lookup the video above.

print("printing key,value pairs below using the .items() method on dict")
for key, value in simple_dict.items():
     print(key , "==>" , value)

# items() makes big huge list. a more efficient way is to use iteritems() this will use a iterator and then iterate
# over a single tuple instead of a big list of tuples unpacking in the items() way as below

# for key, value in simple_dict.iteritems():
#      print(key , "=***=>" , value)
# HOWEVER, with python 3 iteritems no longer needed/exists as changes are done to items() itself. so we can use items() instead of iteritems
# http://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems
#

# NOw to build a dict from a couple of lists:

key_list = ["key1", "key2", "key3", "key4", "key5"]
val_list = ["val1", "int2", 3, [0,1],  {"k1": "v1", "k2": 2}]

print("generating a dictionary from two lists using the \"zip\" function")

dict_from_lists = dict(zip(key_list,val_list))
print("dictionary from lists:", dict_from_lists)

# could not get izip to work http://stackoverflow.com/questions/4989763/when-is-it-better-to-use-zip-instead-of-izip