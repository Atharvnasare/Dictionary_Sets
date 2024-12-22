students = {
    "name" : "Shradha" ,
    "Score" : {
        "Chemistry" : 98 ,
        "Physic" : 97 ,
        "Maths" :96 ,
    }
}

print(students.keys()) #return all keys

print(students.values()) # return all values

print(students.items())  #return all (keys , values) pairs as tuple

print(students.get("name")) #return thwe key according to value

new_dict ={"city" : "Delhi" , "age":16}
students.update(new_dict) #insert the specified items to dictionar

print(students)