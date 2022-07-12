import _thread

def new_thread():
    while True:
        print('A')

_thread.start_new_thread(new_thread, ()) 

while True:
    print('B')
