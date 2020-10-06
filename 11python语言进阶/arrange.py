names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)
scores = [[None] * len(courses) for _ in range(len(names))]#创建出填写成绩的列表，通过迭代创建多个列表
for row, name in enumerate(names):#enumerate（）方法向可迭代对象添加计数器，然后将其返回（枚举对象）。

    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))#将每个人的各科成绩填入相应的位置
        print(scores)#打印成绩
