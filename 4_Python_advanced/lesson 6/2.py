import threading
import time
import os


def checker():
    print('Looking for the file!')
    while True:
        try:
            with open('somefile.txt', 'r') as file:
                print('Checking the file!')
                if 'WOW!' in file.read():
                    print('Found WOW!')
                    break
                else:
                    time.sleep(5)
        except:
            print("Can't see the file")
            time.sleep(5)

    print('We are going to delete the file!')
    wow_annigilator.set()
    wow_annigilator.clear()


def deleter():
    print('WAITING FOR DELETE COMMAND...')
    wow_annigilator.wait()
    print('DELETE COMMAND RECEIVED')
    os.remove("somefile.txt")
    print('THE FILE HAS BEEN DELETED!')


wow_annigilator = threading.Event()

task1 = threading.Thread(target=checker)
task2 = threading.Thread(target=deleter)

task2.start()
task1.start()

task2.join()
task1.join()
