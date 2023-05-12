# Love Calculator

first_name = input('Input first name - ').lower()
second_name = input('Input Second name - ').lower()

t_count = first_name.count('t') + second_name.count('t')
r_count = first_name.count('r') + second_name.count('r')
u_count = first_name.count('u') + second_name.count('u')
e_count = first_name.count('e') + second_name.count('e')

l_count = first_name.count('l') + second_name.count('l')
o_count = first_name.count('o') + second_name.count('o')
v_count = first_name.count('v') + second_name.count('v')
e_count = first_name.count('e') + second_name.count('e')

print(f'T-{t_count}  L-{l_count}')
print(f'R-{r_count}  O-{o_count}')
print(f'U-{u_count}  V-{v_count}')
print(f'E-{e_count}  E-{e_count}')
print('-------')
true_sum = t_count + r_count + u_count + e_count
love_sum = l_count + o_count + v_count + e_count
print(f'  {true_sum}   {love_sum}')

str_true_sum = str(true_sum)
str_love_sum = str(love_sum)

true_love_rate = str_true_sum + str_love_sum
int_true_love_rate = int(true_love_rate)

comment = '-text goes here-'

if int_true_love_rate < 10:
    comment = 'Y\'all dont fit, you guys go like coke & mentos'
elif int_true_love_rate < 25:
    comment = 'Awnn, '
elif int_true_love_rate < 50:
    comment = 'Awnn, Love in Paradise !!'
elif int_true_love_rate < 75:
    comment = 'Woww, Cherish what you have!!'
else:
    comment = 'Woww, now this is love!!'

print(f'You got {int_true_love_rate}%, {comment}')