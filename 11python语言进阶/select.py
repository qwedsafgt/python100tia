def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]#等于列表中的所有元素
    for i in range(len(items) - 1):#通过
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):#判断是否小于
                min_index = j#选出这两个值中较小的，重新赋值，继续循环
        items[i], items[min_index] = items[min_index], items[i]#把这一轮中最小的排在前面
    return items
