from time import *
import random as rd

def mistake_cal(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(s_time, e_time, userinput):
    time_delay = e_time - s_time
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
if __name__ == '__main__':
    while True:
        ck = input('ready to test yes/no : ').lower()
        if ck == 'yes':
            typing_test = ["Ali walked through the quiet forest before sunset. Suddenly, he heard a strange sound behind the trees. He turned around and saw a small injured bird.",
            "The next morning, Sara found an old wooden box under her grandmother's bed. Curious, she opened it slowly and discovered beautiful letters written many years ago.",
            "Tom was returning home when heavy rain started falling. Near the bridge, he noticed a lost puppy. He carried it home and promised to find its owner."]

            test1 = rd.choice(typing_test)
            print('       ******Typing Speed Test******')
            print(test1)
            print()
            print()
            s_time = time()
            test_input = input('  Enter the paragraph:  ')
            e_time = time()

            print('Speed: ',speed_time(s_time,e_time,test_input)," w/sec")
            print('Error: ',mistake_cal(test1,test_input),'word')
        elif ck == 'no':
            print('Thankyou for visiting.')
            break
        else:
            print('Wrong word typing.')
