
# 파이썬의 변수: 값이 담긴 객체를 가리킨다.

# 변수 생성, 변경
a = 1       # int
b = 1.0     # float
c = True    # bool
d = [1,2,3] # list
e = (1,2,3) # tuple
f = 'abc'   # str
a = 2

# 변수 타입, 값 출력
print(type(a), id(a), a, id(2))
print(type(b), id(b), b, id(float))
print(type(c), id(c), c, id(True))
print(type(d), id(d), d, id([1,2,3]))
print(type(e), id(e), e, id((1,2,3)))
print(type(f), id(f), f, id('abc'))

a = str(a)      # int -> str
b = int(b)      # float -> int
d = tuple(d)    # list -> tuple
f = list(f)     # str -> list
print(a, b, d, f)
print(type(a), type(b))
