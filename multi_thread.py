from threading import Thread
from time import sleep
# Create a threading example using classes  
class Test1(Thread):
    def run(self):
        for i in range(5):
            print("Thread 1 is running ", i)
            sleep(0.1)
            
class Test2(Thread):
    def run(self):
        for i in range(5):
            print("Thread 2 is running ", i)
            sleep(0.1)  
            

t1 = Test1()
t2 = Test2()
# Start the threads
t1.start()
t2.start()
# Wait for both threads to complete
t1.join()
t2.join()
#  Final message
print("Both threads have finished execution.")