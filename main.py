from game_data import getdata
from random import randint

data = getdata()
for x in range(len(data)):
    print(data[x].get('name'), )

A = data[randint(0, len(data))]
B = data[randint(0, len(data))]
count = 1
reserverd_instagram = ''
# for random_instagram in range(0, len(data)):



print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
print('___VS___')
print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

while count > 0:
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a' and A['follower_count'] >= B['follower_count']:
        count += 1
    elif choice == 'b' and A['follower_count'] <= B['follower_count']:
        count += 1
    else:
        count = 0
        print('Вы проиграли')
    print(f'Ваш счет {count}')

