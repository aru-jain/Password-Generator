import random
num = chr(random.randint(97,122))
num1 = chr(random.randint(97,122))
num2 = chr(random.randint(65,90))
num3 = chr(random.randint(65,90))
num4 = chr(random.randint(48,57))
num5 = chr(random.randint(48,57))
num6 = chr(random.randint(33,47))
num7 = chr(random.randint(33,47))
password = num + num1 + num2 + num3 + num4 + num5 + num6 + num7
pass_list = list(password)
random.shuffle(pass_list)
result = ''.join(pass_list)
print(result)
