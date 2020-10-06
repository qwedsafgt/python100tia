"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""
class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    max_weight, num_of_things = map(int, input().split())#map根据提供的函数对指定序列做映射。
                                                          #这个将查询用户输入，然后将其拆分为单词，将这些单词转换为整数，只有输入两个数字时能成功。

    all_things = []
    for _ in range(num_of_things):#循环六次
        all_things.append(Thing(*input_thing()))#将物品信息加入列表，
    all_things.sort(key=lambda x: x.value, reverse=True)#sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数，TRUE为降序
    total_weight = 0
    total_price = 0
    for thing in all_things:#按性价比从高到低的来循环
        if total_weight + thing.weight <= max_weight:#小于20
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')#知道重量达到，就结束循环


if __name__ == '__main__':
    main()
