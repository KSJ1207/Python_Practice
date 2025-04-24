## Membership (in / not in)
def membership():
    word = "banana"

    if "c" not in word:
        print("yes")

    else:
        print("no")


##membership()

## Identity (is / is not)
def identity():             ## string과 list는 iterable object 그러나 integer는 non-iterable object 
    list1 = [10, 20, 30]
    list2 = [10, 20, 30]

    print(list1 == list2)   ## True
    print(list1 is list2)   ## False

##identity()

## slicing
def slice():
    name = "Andrew"

    ##print(name[:4]) ##(:end) , 0~3번 index 까지 print

    ##print(name[2:]) ##(start:) 2번~마지막 index 까지 print

    ##print(name[1::2]) ##(start:end:step) 1번~마지막 indext까지 2칸씩 건너뛰어서 print

    ##print(name[6::-2]) ##reverse
##slice()


## split & join
def split():
    name ="Andrew Luxton-Reilly"
    ##print(name.split()) ## space가 있으면 space단위로 쪼개기

    ##print(name.split("n")) ## 괄호 안의 string은 사라짐

##split()

def join():
    list = ["a", "b", "c"]

    print(", ".join(list)) ## list안의 value를 join해줘라 사이사이에 ,를 넣어서서

##join()

## Removing values in a loop

def remove_loop():

    data = [4, 6, 1, 8, 7, 6]
    for index in range(len(data)-1, -1, -1): ## index = i
        if data[index] % 2 == 0:
            data.pop(index)

    print(data)

remove_loop()


## default value in parameter
def multiply(num = 5, to_add = 3): ## parameter
    new_num = num * num
    new_num += to_add
    return new_num
 
multiply(to_add = 3, num = 6) ## argument



## List Comprehension
new_list = [letter for letter in 'hello' if letter > 'i']

new_list = []
for letter in 'hello':
    if letter > 'i':
        new_list.append(letter)

new_list = [i.strip() for i in ['   hello ', '  hi   ', '  bye ']]


def square(a):
    return a * a

my_list = [(6,3), (5,6), (3,5)]
new_list = [square(y) for (x, y) in my_list if y > 4]


class Champion:
	def __init__(self, name, ability, role, xPosition, yPosition): ## init은 object 생성을 위한 method
		self.name = name
		self.ability = ability
		self.role = role
		self.xPosition = xPosition
		self.yPosition = yPosition
		
	def __str__(self):
		return "{}".format(self.name)
		
	def move(self, dx, dy):
		self.xPosition += dx
		self.yPosition += dy

	def __repr__(self):
		return "Champion({}, {}, {}, {}, {})".format(self.name, self.ability, self.role, self.xPosition, self.yPosition)



new_champion = Champion("Ezreal", "shot", "bottom", 100, 100)  ## 챔피언 object 생성
new_champion.move(5, -8)  ## move method 사용
print(new_champion)  ## "Ezreal"
print(repr(new_champion)) ## Champion("Ezreal", "shot", "bottom", 100, 100) 출력


## 04.24 Homework


class Cat:

    def __init__(self, name, gender, bodycolor):
         self.name = name
         self.gender = gender
         self.bodycolor = bodycolor

    def __str__(self):
         return "Cat Info (name: {}, gender: {}, bodycolor: {})".format(self.name, self.gender, self.bodycolor)
    
    def __repr__(self):
         return "Cat({},{},{})".format(self.name, self.gender, self.bodycolor)
    
cat_a = Cat("Leo", "Male", "Black")
print(cat_a)
print(repr(cat_a))



class Architecture:
     
     def __init__(self, established_year, name, size):
          self.established_year = established_year
          self.name = name
          self.size = size
          

     def __str__(self):
          return "This Building was established in {}, The name of the building is {}, and the size is {}".format(self.established_year, self.name, self.size)
     
     def __repr__(self):
          return "Architecture({},{},{})".format(self.established_year, self.name, self.size)
     

uoa = Architecture("1966", "OGGB", "74000m^2")
print(uoa)
print(repr(uoa))



## Default Argument values

def sum(x, y=7):
    return x + y

print(sum(5))      ## output : 15
print(sum(5, 3))   ## output : 8


## List Comprehension

even = [num for num in range(20) if num % 2 == 0]
print(even)  # output : 0, 2, 4, 6, 8, 10, 12, 14, 16, 18 // 20은 제외; 0~19

## List Comprension with filtering

not_even = [num for num in range(0, 21) if num % 2 != 0] ## 조건 추가가
print(not_even) ## output : 1, 3, 5, 7, 9, 11, 13, 15, 17, 19

## Dictionary Comprehension

words = ["apple", "banana", "lemon"]
lengths = {word:len(word) for word in words} ## {len(word) for word in words} 일때는 {5, 6}만 나옴, difference?
print(lengths) ## output : {"apple": 5, "banana"': 6, "lemon": 5}