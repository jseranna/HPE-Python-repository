# tax calculation app

# input data

name = input('What is your name: ')
age = int(input('age please: '))
sal = int(input('what is your total CTC: '))
sec = int(input('money invested under section 80C(if any): '))


# process

x= int(250000)

if(sal <=250000):
    y=0
elif(sal >=250001 and sal <=500000):
    y=(sal-sec-x)*5/100
elif(sal >=500001 and sal <=1000000):
    y=(sal-sec-x-x)*20/100+12500
elif(sal >=1000001):
    y=(sal-sec-x-x-x-x)*30/100+112500
else:
    y=0


# Output

print('Hi',name , 'your total tax payable amount is: ', y)


          
