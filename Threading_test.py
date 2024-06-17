import threading
import time


def sing(*song):
    for i in range(10):
        print("i am singing")
        print(f"the song is {song}")
        time.sleep(2)


def dance(msg):
    for j in range(10):
        print(f"dancedancedance,{msg}")
        time.sleep(1)


if __name__ == '__main__':
    thread1 = threading.Thread(target=sing,args=("只因你太美",'七里香','never gonna give you up'))
    thread2 = threading.Thread(target=dance,kwargs={"msg":"跳舞跳舞"})

    thread1.start()
    thread2.start()