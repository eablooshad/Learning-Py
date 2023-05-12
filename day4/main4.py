#Understanding the nested lists & matrix

map1 = ['⬜️', '⬜️', '⬜️','⬜️', '⬜️', '⬜️']
map2 = ['⬜️', '⬜️', '⬜️','⬜️', '⬜️', '⬜️']
map3 = ['⬜️', '⬜️', '⬜️','⬜️', '⬜️', '⬜️']
map4 = ['⬜️', '⬜️', '⬜️','⬜️', '⬜️', '⬜️']
map5 = ['⬜️', '⬜️', '⬜️','⬜️', '⬜️', '⬜️']
map6 = ['⬜️', '⬜️', '⬜️','⬜️', '⬜️', '⬜️']

map_main = [map1, map2, map3, map4, map5, map6]

print(f'{map1}\n{map2}\n{map3}\n{map4}\n{map5}\n{map6}')

co_ord = str(input('input co_ordinates > '))

row = int(co_ord[0])
col = int(co_ord[1])

map_main[row - 1][col - 1] = 'X'

print(f'{map1}\n{map2}\n{map3}\n{map4}\n{map5}\n{map6}')