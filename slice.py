#闭包和装饰器
from functools import wraps

def add_infor(func1):
	@wraps(func1)
	def wrapper():

		print("Below is my name:")
		func1()
	return wrapper

@add_infor
def get_name():
	print("wenjian")

#get_name()
#print(get_name.__name__)


class Student(object):
	#__slots__=("name","world")
	def __init__(self, name):
		self.name = name

stu = Student("lilei")
print(stu.name)
stu.test = 1

# print(stu.name)
# print(stu.__name)
#print(stu._Student__name)


