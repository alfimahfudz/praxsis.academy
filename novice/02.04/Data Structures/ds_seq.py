shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist[::1]
['apple', 'mango', 'carrot', 'banana']
print(['apple', 'mango', 'carrot', 'banana'])
shoplist[::2]
['apple', 'carrot']
print(['apple', 'carrot'])
shoplist[::3]
['apple', 'banana']
print(['apple', 'banana'])
shoplist[::-1]
['banana', 'carrot', 'mango', 'apple']
print(['banana', 'carrot', 'mango', 'apple'])

bri = set(['brazil', 'russia', 'india'])
'india' in bri
True
'usa' in bri
False
bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
True
bri.remove('russia')
bri & bric # OR bri.intersection(bric)
{'brazil', 'india'}

