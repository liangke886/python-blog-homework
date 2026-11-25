print("=====任务1 del切片删除 + for循环remove对比=====")
# del切片删除
ls1 = [0,1,2,3,4,5,6,7,8,9]
print("del切片删除前：", ls1)
del ls1[::3]
print("del ls1[::3] 删除后：", ls1)

# for循环remove 错误写法
ls_err = [2,2,4,6]
print("\nfor循环remove【错误版本】原始列表：", ls_err)
for i in ls_err:
    if i % 2 == 0:
        ls_err.remove(i)
print("错误写法运行结果：", ls_err)

# for循环remove 正确写法（遍历副本）
ls_right = [2,2,4,6]
print("\nfor循环remove【正确版本】原始列表：", ls_right)
for i in ls_right.copy():
    if i % 2 == 0:
        ls_right.remove(i)
print("正确写法运行结果：", ls_right)


print("\n=====任务2 哈希测试=====")
s = set()
# s.add( (1,2,3) )       # ✅成功
# s.add( (1,[2,3]) )     # ❌报错
# s.add( [1,2] )         # ❌报错
# s.add( frozenset({1,2}) ) # ✅成功
# s.add( {1,2} )         # ❌报错
print(s)


print("\n=====任务3 集合运算、集合推导式=====")
A={2,4,6,8,10,12}
B={3,6,9,12,15}
print("A =",A)
print("B =",B)
print("交集 A & B：", A & B)
print("并集 A | B：", A | B)
print("差集 A - B（A有B没有）：", A - B)
print("差集 B - A（B有A没有）：", B - A)
print("对称差集 A ^ B（只在其中一个里面）：", A ^ B)

# 集合推导式：1~30能被4整除
set_comp = {x for x in range(1,31) if x % 4 == 0}
print("1~30能被4整除的集合：", set_comp)


print("\n=====任务4 三种列表去重对比=====")
data = [5,2,7,2,5,7,3,9,1]
# 方案1 set去重（无序）
res1 = list(set(data))
print("方案1 set去重（无序）：", res1)

# 方案2 手写循环保序去重
res2 = []
for num in data:
    if num not in res2:
        res2.append(num)
print("方案2 手写循环保序去重：", res2)

# 方案3 dict.fromkeys 一行保序去重
res3 = list(dict.fromkeys(data))
print("方案3 dict.fromkeys保序去重：", res3)


print("\n=====任务5 选课统计综合任务=====")
class1 = [101,103,105,107,109,103,101]
class2 = [102,104,106,108,109,107,102]
print("原始一班选课列表：", class1)
print("原始二班选课列表：", class2)

# ① 分别获取两个班不重复、保序的学生编号
s1_unique = list(dict.fromkeys(class1))
s2_unique = list(dict.fromkeys(class2))
print("①一班去重保序：", s1_unique)
print("①二班去重保序：", s2_unique)

# 转集合做运算
set1 = set(class1)
set2 = set(class2)

# ② 同时选两门课（交集）
both = set1 & set2
print("②同时选两门课学生：", both)

# ③ 只选其中一门（对称差）
only_one = set1 ^ set2
print("③只选一门课学生：", only_one)

# ④选了1班，没选2班
only_c1 = set1 - set2
print("④选一班、没选二班：", only_c1)

# ⑤交集转元组
both_tuple = tuple(both)
print("⑤交集转元组：", both_tuple)

# 拓展：嵌套列表去重
nest = [[1,2],[3,4],[1,2],[5,6]]
temp = {tuple(i) for i in nest}
nest_res = [list(i) for i in temp]
print("拓展嵌套列表去重结果：", nest_res)
