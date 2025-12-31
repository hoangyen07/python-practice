# Create a threading example using classes

class Test1():
    def run():
        for i in range(5):
            print("Thread 1 is running ", i)
            
class Test2():
    def run():
        for i in range(5):
            print("Thread 2 is running ", i)    
            
t1 = Test1
t2 = Test2
# Start the threads
t1.run()
t2.run()