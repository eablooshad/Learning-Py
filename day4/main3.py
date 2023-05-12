#treasure map

map1 = ['1⬜️', '⬜️', '⬜️']
map2 = ['2⬜️', '⬜️', '⬜️']
map3 = ['3⬜️', '⬜️', '⬜️']

map_main = [map1, map2, map3]

print(f'{map1}\n{map2}\n{map3}')

# print(map_main)

coordinates = str(input('Where would you like to mark? '))
column_coordinates = int(coordinates[0])
row_coordinates = int(coordinates[1])

map_main[row_coordinates - 1][column_coordinates - 1] = 'x'

print(f'{map1}\n{map2}\n{map3}')