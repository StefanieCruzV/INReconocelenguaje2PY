num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize float number 
boolean = True # variable declaration, initialize boolean
string = 'Hello World'# variable declaration, initialize string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list  declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#dictionary 
fruit = ('blueberry', 'strawberry', 'banana') #tuple 
print(type(fruit)) #   access value of fruit and print data type of it 
print(pizza_toppings[1]) # print value of pizza_toppings in the position 1
pizza_toppings.append('Mushrooms')# add value to the end
print(person['name']) # accest value name wich is in dictionary person 
person['name'] = 'George'# change the value 
person['eye_color'] = 'blue'# add value 
print(fruit[2])#acces value of fuit  tuple in teh position 2

if num1 > 45: #conditional  if the variable is greatter
    print("It's greater")  #print string
else: #else 
    print("It's lower") #print string

if len(string) < 5:# conditional if the length is less  than..
    print("It's a short word!") #print string
elif len(string) > 15: #else if  the length is larger than ..
    print("It's a long word!") #print string
else: #else 
    print("Just right!") #print string

for x in range(5): # foor loop 
    print(x)# print 0,1,2,3,4
for x in range(2,5):
    print(x)# print 2,3,4
for x in range(2,10,3):
    print(x)# print 2,5,8
x = 0 #  variable declaration, initialize
while(x < 5): # while loop
    print(x) # print 0,1,2,3,4
    x += 1 #increment

pizza_toppings.pop()#function to delete the laste value
pizza_toppings.pop(1) #function to delete the value in the position 1

print(person)# printe the dictionary
person.pop('eye_color')# function to delete the key and value "eye color "
print(person) # print {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings: # foor loop
    if topping == 'Pepperoni': # conditional
        continue #continue
    print('After 1st if statement') #print 
    if topping == 'Olives': # conditional 
        break # break 

def print_hello_ten_times():# function 
    for num in range(10): # foor loop
        print('Hello') # print 

print_hello_ten_times() # call the funtion

def print_hello_x_times(x): # function
    for num in range(x): # foor loop
        print('Hello') #print

print_hello_x_times(4) # call the function

def print_hello_x_or_ten_times(x = 10):#function
    for num in range(x):# foor loop
        print('Hello')#print 

print_hello_x_or_ten_times()  # call the funtion
print_hello_x_or_ten_times(4) # call the funtion


# """
# Bonus section
# """

# print(num3) # can not print num3 because its not defined 
# num3 = 72 # define and initialize num3
#fruit[0] = 'cranberry' #can not add because its a tuple
# print(person['favorite_team'])# can not exist 

# print(pizza_toppings[7]) # can not exist 
#print(boolean)# didnt know whats boleans means 
# fruit.append('raspberry')) # can not be modified 
# fruit.pop(1) # can not be modified 