from abc import ABC, abstractmethod

class absclass(ABC):

    def print(self,x):

        @abstractmethod
        def task(self):
            print("we are inside absclass task")

class testclass(absclass):
    def task(self):
        print("we are inside testclass task")

testobj = testclass()
testobj.task()
testobj.print(100)