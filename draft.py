#from collections import deque
st = []
s = "(((()))"
br_open = ["(", "{", "["]
br_close = [")", "}", "]"]

l = ""
def isValid(s):
    for i in s:
        if i in br_open:
            st.append(i)
            print(st)
        if i in br_close:
            l = st.pop()
            print(f"st = {st}")
            print(f"l = {l}")
            print(f"i = {i}")
            if l == "(" and i == ")":
                continue
            elif l == "[" and i == "]":
                continue
            elif l == "{" and i == "}":
                continue
            else:
                return 0
    if len(st) == 0:
        return 1
    elif len(st) > 0:
        return 0

if isValid(s):
    print("Good")
else:
    print("No")

'''
([({})][]) - Yes
[][) - No

4*5+3*4
->

n
n - пар скобок
сколько существует вариантов правильных скобочных последовательностей?

1/(n+1)*C(2n)_(n)

3
((()))
(())()
()()()
()(())
()()()

5
4 3

[1, 1, 1 + 1, ...]

n, k
print(n^k)

k - 5
n^2 * n^2 * n
k - 4
n^2 * n^2

1) Старые задачи
2) обратная польская запись(нотация)
3) Возведение в степень через рекурсию. Строго после предыдущего пункта. Посмотреть алогритм бинарного возведения в степень.
4) def (n) :
     return () -- определяет явлется ли n степенью двойки
'''
