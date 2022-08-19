from collections import namedtuple

Marks = namedtuple('Marks', 'Algebra Geometry History Computer_Science Geography')

marks1 = Marks(10, 9, 7, 12, 9)
marks2 = Marks(6, 7, 11, 9, 11)

print("У Івана наступний табель:", marks1)
print("У Дарії наступний табель:", marks2)