# 자동화하고 로그파일(guess.txt)을 남기도록,
# 로그 시간을 갖도록.
import random

def guess_number():
    low = 1
    high = 100
    answer = random.randint(low, high)
    chance = 7
    mid = (low + high) //2 #50
    with open('guess.txt','w') as file:
        file.write("start guess number")


        while chance != 0:

            if mid == answer:
                print(f'You win. Answer is {answer}')
                file.write(f'You win. Answer is {answer}\n')
                break
            elif mid > answer:
                chance = chance - 1
                print(f'{mid} is bigger. Chance left : {chance}')
                file.write(f'{mid} is bigger. Chance left : {chance}\n')
                high = mid - 1
            else:
                chance = chance - 1
                print(f'{mid} is lower. Chance left : {chance}')
                file.write(f'{mid} is lower. Chance left : {chance}\n')
                low = mid + 1
            mid = (low + high) // 2
        else:
            print(f'You lost. Answer is {answer}')
            file.write(f'You lost. Answer is {answer}\n')


guess_number()
