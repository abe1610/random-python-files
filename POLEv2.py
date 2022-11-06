import random

list = ['Lewis Hamilton', 'George Russell',
 'Max Verstappen', 'Sergio Perez',
 'Charles Leclerc', 'Carlos Sainz',
 'Fernando Alonso', 'Esteban Ocon',
 'Lando Norris', 'Daniel Ricciardo',
 'Valtteri Bottas', 'Zhou Guanyu',
 'Sebastian Vettel', 'Lance Stroll',
 'Kevin Magnussen', 'Mick Schumacher',
 'Piere Gasly', 'Yuki Tsunoda',
 'Alexander Albon', 'Nicholas GOATifi']

driver = random.choice(list)

for x in range(22):
    driver = random.choice(list)
    print(driver + " gets pole position!")

c = driver.count()