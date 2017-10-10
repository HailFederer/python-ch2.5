# 기본 인수 값


def incr(a, step=1):
    return a + step
# def incr(step=1, a):
#     return a + step


print(incr(10, 10))
print(incr(10))

# 키워드 인수 + 기본 인수
def area(width=0, height=0):
    return width*height


print(area(height=10))

# 가변 인수
def varg(a, *arg):
    print(a, arg)


varg(1)
varg(1, 2)
varg(1, 2, 3, 4, 5)


# c의 printf
# printf("%s, %d", "hello", 10)
print('%s, %d' % ('hello', 10))


def printf(f, *arg):
    print(f % arg)


printf("%s, %d", "hello", 10)


# 정의되지 않은 파라미터 받기
def f(width, height, **arg):
    print(width, height)
    print(arg)


f(10, 20, depth=10, dimension=3)


def g(a, b, *args, **kw):
    print(a, b)
    print(args)
    print(kw)


g(10, 20, 3, 4, depth=10, dimension=3)

# 튜플/사전 파라미터
def h(name, age, height):
    print(name, age, height)


t = ('둘리', 10, 145)

h(*t)

d = {'name':'마이콜', 'age':25, 'height':182}

h(**d)