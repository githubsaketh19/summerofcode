
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0] = 'Giant'

print(bicycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycle = []
print(motorcycle)

favBici = input("What is your favourite motorcycle")
motorcycle.append(favBici)
print(motorcycle)

del motorcycles[2]
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
