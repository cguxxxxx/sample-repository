x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x) # [1, 2, 4, 6, 7, 9]

#[:]分片方法
x =[4, 6, 2, 1, 7, 9]
y = x[ : ]
y.sort()
print(y) #[1, 2, 4, 6, 7, 9]
print(x) #[4, 6, 2, 1, 7, 9]

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
numbers.sort()
print(numbers)

x =[4, 6, 2, 1, 7, 9]
y = sorted(x)
print(y) #[1, 2, 4, 6, 7, 9]
print(x) #[4, 6, 2, 1, 7, 9] 

nums = [3, 2, 8 ,0 , 1]
nums.sort(reverse=True)
print(nums) # 降序排序[8, 3, 2, 1, 0]

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave','B', 10)]
sorted(students,key=lambda s: x[2]) #按照年龄来排序
print(students)

####
def sort_priority(values, group):
	def helper(x):
		if x in group: 
			return False
		return True
	values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

sort_priority(numbers, group)
print(numbers)
####

s = 'asdf234GDSdsf23'
print(sorted(s, key=lambda x: (x.isdigit())))
print("".join(sorted(s, key=lambda x: (x.isdigit()))))
#print("".join(sorted(s, key=lambda x: (x.isdigit(),x.isdigit() and int(x) % 2 == 0,x.isupper(),x))))
