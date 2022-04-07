
# class "NAME":
class Cat:
    name = ""
    age = 0
    breed = ""
    color = ""
    #method
    def voice(self):
        print(self.name + ", Meow")

def main():
    print("Start")
    d1 = Cat()
    d1.name = "Marsel"
    d1.age = 8
    d1.breed = "Scottish Fold"
    d1.color = "Chocolate purple"
    print(f"Cat:\nName: {d1.name}\nAge: {d1.age}\nBreed: {d1.breed}\nColor: {d1.color}\n")

    d1.voice()


if __name__ == '__main__':
    main()

