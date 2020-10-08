class Kea:
    def __init__(self, id):
        self.id = id

keaID = Kea("1")
id = Kea("2")


print(keaID.id)
print(id.id)


scanner = input("Please select your id")

if scanner == keaID.id:
    print("Welcome to the Kea Coffee Machine")
elif scanner == id.id:
    print("Please scan your Kea Card")
else:
    print("Try again")
