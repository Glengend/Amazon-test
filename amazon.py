print('amazon task')
from math import *

print('This will give 3 different outcomes from predetermined variables ')

out_file = open ( 'outputt.txt' , 'w' )

in_file = open("inputt.txt","r")

# Find the minimum
text = in_file.readline()

num_list= text[4:]
num_array=num_list[:-1].split(',')
min_num=num_array[0]
for  num in num_array:
    if (int(num) < int(min_num)):
        min_num=num

min_output='The min output of  ' + ', '.join(num_array) + ' is ' + min_num
print(min_output)
    
# Find the maximum
text = in_file.readline()

num_list= text[4:]
num_array=num_list[:-1].split(',')
max_num=num_array[0]
for  num1 in num_array:
    if (int(num1) > int(max_num)):
        max_num=num1

max_output='The max output of  ' + ', '.join(num_array) + ' is ' + max_num
print(max_output)

# Find the average
text = in_file.readline()

num_list= text[4:]
num_array=num_list.split(',')
avg_num=num_array[0]

num_total=0
for  num2 in num_array:
    num_total=int(num_total)+int(num2)

avg_output='The avg output of  ' + ', '.join(num_array) + ' is ' + str(num_total/len(num_array))
print(avg_output)    
out_file.write(min_output + '\r\n') 
out_file.write(max_output + '\r\n')
out_file.write(avg_output)
out_file.close()

in_file.close()





#block showing the how results are calc.

def sum1 (numbers):
    return sum(map(int, numbers))

def avg (numbers):
    average=str(sum(map(int, numbers)) / len(numbers))
    return average
    
def p90 (numbers):
    return percentile97(numbers,90)

def p70 (numbers):    
    return percentile97(numbers,70)

def percentile97 (numbers,p):
    percentile=p/100*len(numbers)
    return str(numbers[floor(percentile)])


#print output
print('')
print('The solutions are as follows...')


sum=sum1
file = open(r"inputt.txt","r")
lines = file.readlines()

for line in lines:
    stuff = line.split(":")
    func = stuff[0]
    numbers = stuff[1].replace('\n','').split(",")
    
  #  print(("Funtion is " + func + ", numbers are " + str(numbers) + ", answer is ") + (str(eval(func + '(' + str(numbers) + ')'))))

print(("Funtion is " + func + ", numbers are " + str(numbers) + ", answer is ") + (str(eval(func + "(" + str(numbers) + ")")) if func != 'avg' else str(sum(map(int, numbers)) / len(numbers))))

