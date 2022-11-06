import random
from collections import Counter
from colorama import Fore, Style

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

driver = [random.choice(list), random.choice(list),
 random.choice(list), random.choice(list), 
 random.choice(list), random.choice(list), 
 random.choice(list), random.choice(list), 
 random.choice(list), random.choice(list), 
 random.choice(list), random.choice(list), 
 random.choice(list), random.choice(list), 
 random.choice(list), random.choice(list), 
 random.choice(list), random.choice(list), 
 random.choice(list), random.choice(list),
 random.choice(list), random.choice(list),]

count = Counter(driver)
c = (repr(count).strip("Counter(){}"))
print(Fore.YELLOW + 'Pole Positions: ' + Fore.RED + c + Style.RESET_ALL)