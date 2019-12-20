# create a app for simple interest calculator

# Input data

principal = float(input('please input total principal amount:'))
roi = float(input('please input interest rate per annum:'))
tenure = float(input('please input no of years:'))


# process


simint = principal*roi*tenure/100

# output

print('your total interest is:%.2f' % simint)
