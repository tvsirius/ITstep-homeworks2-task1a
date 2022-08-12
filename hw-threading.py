import threading

from countdown import countdown,show_info_infinitly

t1=threading.Thread(target=countdown, args=(2,True))
t2=threading.Thread(target=countdown, args=(5,True))
t3=threading.Thread(target=countdown, args=(10,True))
t4=threading.Thread(target=countdown, args=(7,True))
t5=threading.Thread(target=countdown, args=(4,True))
t99=threading.Thread(target=show_info_infinitly, args=(0.7,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t99.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()

# exit(0)
