# lambda 함수


def blahblah(x):
    return x**2


for i in range(10):
    print('{0}:{1}'.format(i, (lambda x:x**2)(i)), end=' ')
else:
    print()


strings = ['foo', 'card', 'bar', 'abab', 'abab', 'ab', 'foo', 'foo']

strings.sort(key=lambda x: len(x))
print(strings)

print(strings.count('ab'))

strings.sort(key=lambda x: strings.count(x))
print(strings)

