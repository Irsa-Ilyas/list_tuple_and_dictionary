"""Sequence Data types
string list tuple and range
"""
"""List
are used to store and manage collection of data efficiently
list are 
ordered (means that items have a  specific order)
mutable(means that lists can be modified)
indexed(means that list can be accesed by their indexeed number)
dynamic size(means that list can grow or shrink as elements canbe added or removed)
Heterogenous(means that list contain different data typeslike string boolean)
supports duplicate vlaues(means repeted values on ifferent indexes)



"""
mylist:list=["apple",10,True,"cat"]
print(mylist)
"""Accesing list element"""
print(mylist[1])
print(mylist[-1])
print(mylist[-4])
"""Modifying List Element"""
mylist[3]="orange"
print(mylist)
mylist[1]=20
print(mylist)
"""List Slicing
method [0:2]
"""
print("slicing result")
print(mylist[0:])    
print(mylist[0:3]) 
print(mylist[0:4]) 
"""Lists method
some built in lists method 
for handling data efficiently
"""
""".append(adds a single  element at the end)
.extend(adds multiple elements at the end)
"""
flowerlist:list=["Rose","Lily","Daffodil"]
flowerlist.append("Daisy")
print(flowerlist)
flowerlist.extend(["tulip","sunflower","gentina"])
""".extend (list ,tuple, string, set) as an argument leta haii is ka argument iterable huta haii"""
flowerlist.extend("Leaves")
print(flowerlist)
""".append aik argument leta hai .extend multiple arguments leta haii lekin list mein donon list k end mein hi element ko add krty hain """
"""
Feature             | remove()                             | pop()
Purpose             | Element ko value se hataata hai      | Element ko index se hataata hai
Return Value        | None return karta hai                | Removed item return karta hai
Default Behavior    | value nahi deta to kaam nahi karega  | Index nahi deya to last item hatayega
Error if not found  | Value agar list mein nahi ho to ValueError deta hai | Index galat ho to IndexError deta hai"""
# flowerlist.remove()   #give typeerror  needs indexvalue to be remove
# print("flowerlist")


result=flowerlist.remove("Rose")

print(result) #none return kryga q k remove kuch return nahin krta lekin list sy remove krdeta hai
print(flowerlist) #yahan updates rose ko remove krk  result dega
# flowerlist.remove("4") #it will raise value error bcoz 4 is not in list
# print(flowerlist)

animallist:list=["cat","dog","lion"]
res=animallist.pop(1)
print(res)    #pop mein mujhy deleted value dega 
print(animallist)
animallist.pop()   #agher index nahin dengy to last item remove krdega
print(animallist)
"""Sorting a List
.sort() (Ascendin gorder smaller to  greater)default terteeb sy likhta hai
"""
mynums:list=[4,3,5,2,1]    #12345 print jryga
res=mynums.sort()
print(res) 
mynums.sort()  #it will printnone q k sort new list return nahin krta hai
print(mynums) #yahan original list change hujyegy
"""Sorting in descending order when reverse=True
greater to smaller number
"""
mynums.sort(reverse=True)
print(mynums)
myvalues:list=["python","web","scrapper","developer","stack"]
myvalues.sort(key=len)
print(myvalues) #element ki legth k hisab sy value dega
"""lambda arguments: expression
aik anonymous or temporay function hai
"""
mywords:list=["hypertext","markup","language"] 
mywords.sort(key=lambda mywords:mywords[-1]) #-1 sy printing start hugyy
print(mywords)
"""Reverse List 
reverse krdeta hai means last sy shoro krta hai"""
myvalues.reverse()
print(myvalues)
for items in myvalues:
    print(items) 
print("-----Dictionaries In Python----")
"""A dictionary is a collection of key value pair
it is
ordered (items are stored in order they were inserted)
un-indexed (items are accesed according to key not indexes)
mutable (can add remove or modified)
witout duplicate (key must be unique but values can be duplicated)
"""
"""dict constructor sy bhi dictionary create krsakty hain dict()"""
person2:dict=dict(
    name2="maria",
    age2=19,
    Qualification2="Inter"
)
print(person2)
person:dict={
   "name":"Ali",
   "age":20,
   "Qualification":"Inter",
   "status":"single"
}
print(person)
"""donon tareeqon sy dictionaries ko likh sakty hain sirf syntax farq hai dict constructor k sath () or keys ko quote mein nahin likhty is k ilawa =ki jagah : lagaty hain """
"""Accessing key"""
print("""Accessing Values""")
"""we can accesss values with a key using [] or get method"""
print(person["name"])  #Ali
print(person.get("age"))
print(person.get("age","21"))   #default value di hai yahan agher age ki value nahin dengy to 21 print hujyega
print(person.get("Gender","Male")) #yahan meny key value pair add kia haii
"""Modifying dictionary"""
"""can add key value piars also can update existing once"""
person["email"]="abc@gmail.com"
person["name"]="Aly"
print(person)
"""Deleting Items
we can delete a key value pair using del or pop method 
del doesnot return anything whereas pop returns removed key value pairs
"""
"""using del keyword"""
del person["name"]
print(person)
"""using pop meyhod"""
person_status= person.pop("status","not found")  
"""above example  mein pop(key,default value) di hai yeh check krta ahi k status hai ya nahin agher 
huga to to uski value hi print krega warna 
status not found ko print kryga"""  
print(person_status)
print(person)
poped_value=person.pop("color_complexion","normal") #is ka dictionary mein koii change nahin huga 
print(poped_value)  

print("""Dictionary Methods""")

"""Method	        Description	
keys()	        Returns a list of all keys in the dictionary.	
values()	    Returns a list of all values in the dictionary.	
items()	        Returns a list of key-value pairs as tuples.	
clear()	        Removes all items from the dictionary.	
update()	    Adds or updates multiple key-value pairs from another dictionary.	"""
print(person.keys())
print(person.values())
print(person.items())
"""update in python
update method 2 dictionaries ko milaty hai agher aik dictionary mein age  hai or dosri dictionary
mein bhi age hai to woh usy override krdety haii  yeh same aesy hi kaam krta hai jesy jum dictionary ko update krty hain
"""
print("new example of diccct")
myschool:dict={
    "isbig":True,
    "haveground":"yes"
}
mycollege:dict={
    "isbig":"tooo much",
    "co_education":"yes",

}
myschool.update(mycollege)
print(myschool)
mycollege.update({
    "haveguards":"yes"
})
print(mycollege)
mycollege.clear()
print(mycollege)
"""Duplicate Not Allowed"""
carinfo:dict={
    "brand":"Civic",
    "model":2015,
    "year":2020,
    "year":2021   #yahan error nahin ayega bulky pichly year sy update hukr answer ayega aik hi year print huga or yeh length bhi 3 hi dega years ko alag alag count nahin krega
}
print(carinfo)

"""Iterating over Dict"""
for key in carinfo:
    print(key)
for key ,value in carinfo.items():
    print(key, ":" ,value)  
for value in carinfo.items():
    print(value) 
print(len(carinfo))  
"""Copying a dict"""
copied_dict=carinfo.copy()
print(copied_dict)
print("Nested Dictionary")
nested_dictionary:dict={
    "outerdict":{
        "name":"johny",
        "age":23
    },
    "innerdict":{
    "name":"BOb",
    "age":22
    }
}
print(nested_dictionary)
print(nested_dictionary["outerdict"])
print(nested_dictionary["innerdict"])
print(nested_dictionary["outerdict"]['age'])

"""Remaining topics list and dictionary comprehension 
soon i will complete"""






