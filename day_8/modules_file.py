# modules_file.py
# creating function

def modules():
    print("welcome")

# creating class
class employee:
    def __init__(self,id,name,age,gender):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender
    def PrintData(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.gender)