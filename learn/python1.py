# coding='UTF-8'


print('\n\n-----------------------------------------------------------------------------------------------\n\n')


class A(object):
    name = 'Lia'

    def out(self):
        print(8888888)


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.__mro__)

print('\n\n-----------------------------------------------------------------------------------------------\n\n')


class People:
    name = "小明同学"
    _sex = "男"
    __address = "heihei之地"

    def __init__(self, age):
        self.__age = age

    @property
    def walk(self):
        print("I can walk")

    @classmethod
    def _jump(self):
        print("I can jump")

    def __heihei(self):
        print("I can heihei")


people = People(12)
print(dir(people))
print(people._People__age)

# people.walk() 在walk方法被标记为@property时，
# 再用walk()调用时会出现错误，只能当做属性用walk调用
people.walk
# People._jump()方法的属性
print(People._jump)
People._jump()
print(people._People__heihei)
people._People__heihei()

print('\n\n-----------------------------------------------------------------------------------------------\n\n')


class Student(People):
    stu_number = 0

    def __init__(self, name, sex, address, age, stu_number):
        self.name = name
        self._sex = sex
        self._People__adress = address
        super(Student, self).__init__(age)
        self.stu_number = stu_number


student = Student('张ng', '男', '的是非地方', 26, 100010)
print(dir(student))
print(student.name)
print(student._sex)
print(student._People__adress)
print(student._People__age)
print(student.stu_number)
student.walk
student._People__heihei()
print('student 是否是 People的实例：', isinstance(student, People))
print('student 是否是 Student的实例', isinstance(student, Student))
print('Student 是否是 People的子类', issubclass(Student, People))
print(student.__str__())
print(student.__repr__())

print('\n\n-----------------------------------------------------------------------------------------------\n\n')


class OldClass:
    def __init__(self, name):
        self.name = name


class NewClass(object):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    old = OldClass('oldName')
    print(old)
    print(type(old))
    print(dir(old))
    new = NewClass('newName')
    print(new)
    print(type(new))
    print(dir(new))

print('\n\n-----------------------------------------------------------------------------------------------\n\n')

formatter = "%r %c %r %r"
print(formatter % ("one", "c", "three", "four"))
print(formatter % (1, "c", "three", "four"))
print(formatter % (
    "I had this thing.",

    3,
    "But it didn't sing.",
    "So I said goodnight."
))

print('\n\n-----------------------------------------------------------------------------------------------\n\n')

# python中map(func,value)函数的用法
L1 = range(20, 90)
L2 = range(9, 100)
for i in map(lambda x, y: x ** y, L1, L2):
    print(i)

print('\n\n-----------------------------------------------------------------------------------------------\n\n')

# filter(func,value)函数的用法
L1 = ['sdf', 'sdfs', 'eee', 'wqqw', 'qed', 'yiyuoj']
for i in filter(lambda x: x.find('sdf') == -1, L1):
    print(i)

print('\n\n-----------------------------------------------------------------------------------------------\n\n')

# filter(func,value)函数的用法
L1 = ['sdf', 'sdfs', 'eee', 'wqqw', 'qed', 'yiyuoj']
for i in sorted(L1, key=lambda x: 1 / (x.find('e') + 1) if x.find('e') != -1 else -1, reverse=True):
    print(i)

print('\n\n-----------------------------------------------------------------------------------------------\n\n')

# python中True==1 为真 False==0为真
x = 'special'
print(x if x != 'special' else 'common')

val = float(78)
print('You should be', ('working', 'retired')[val > 65])

print('\n\n-----------------------------------------------------------------------------------------------\n\n')

# 文件操作

file = open("../learn")
files = file.dir()
for filesa in files:
    fileList = filesa.readlines()
    for str in fileList:
        if str.startswith("#"):
            print(str)
    filesa.close()
