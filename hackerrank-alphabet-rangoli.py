#You are given an integer, N . 
#Your task is to print an alphabet rangoli of size N. 
#(Rangoli is a form of Indian folk art based on creation of patterns.)

#Different sizes of alphabet rangoli are shown below:

#size 3

#----c----
#--c-b-c--
#c-b-a-b-c
#--c-b-c--
#----c----

#4(x-1) + 1

#size 5

#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------

#size 10

#------------------j------------------
#----------------j-i-j----------------
#--------------j-i-h-i-j--------------
#------------j-i-h-g-h-i-j------------
#----------j-i-h-g-f-g-h-i-j----------
#--------j-i-h-g-f-e-f-g-h-i-j--------
#------j-i-h-g-f-e-d-e-f-g-h-i-j------
#----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
#--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#------j-i-h-g-f-e-d-e-f-g-h-i-j------
#--------j-i-h-g-f-e-f-g-h-i-j--------
#----------j-i-h-g-f-g-h-i-j----------
#------------j-i-h-g-h-i-j------------
#--------------j-i-h-i-j--------------
#----------------j-i-j----------------
#------------------j------------------



#The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

#Function Description

#Complete the rangoli function in the editor below.

#rangoli has the following parameters:

#int size: the size of the rangoli
#Returns

#string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
#Input Format

#Only one line of input containing size , the size of the rangoli.

#Constraints
#0 < size < 27

#Sample Input

#5
#Sample Output

#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------


alphabet = ['a','b','c','d','e']

def rangoli(size): 
    #4(x-1) + 1 Längd
    ##2(x-1) + 1 bredd
    #print(size)
    result = ""
    numberOfLetters = 4*(size-1) +1
    numberOfRows = 2*(size-1) + 1
    print(numberOfRows)
    center = get_center_row(size)
    print(center)
    for x in range(1, size):
        temp = alphabet[x] 
        for y in range(x+1,size):
            temp = alphabet[y] + "-" + temp + "-" + alphabet[y]
        for y in range(1 ,x):
            temp = "--" + temp + "--" 
        temp = "--" + temp + "--"
        print(temp)
    


def get_center_row(size):
    center = alphabet[0]
    for y in range(1,size):
        center = alphabet[y] + "-" + center + "-" + alphabet[y]
    return center


rangoli(5)
