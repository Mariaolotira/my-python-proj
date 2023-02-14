class Car():
    def __init__(self, type, owner):
        self.type=type
        self.owner=owner

owner_1=Car("Toyota","Ryan")
print(owner_1.type)
print(owner_1.owner)

print("<-----end of first owner----->")

owner_2=Car("Mercedes", "Harry")
print(owner_2.type)
print(owner_2.owner)


print("<------end of second owner------>")


owner_3=Car("Dodge","Tracy")
print(owner_3.type)
print(owner_3.owner)


print("<-------end of third owner-------->")