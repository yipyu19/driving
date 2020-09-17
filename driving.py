country = input('請問你是哪個國家人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == 'taiwan':
    if age >= 18:
    	print('你可以考駕駛照')
    else:
    	print('你不能考駕駛照')
 