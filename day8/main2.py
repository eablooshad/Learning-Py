#Area calculator
import math

def paint_calc(height, width, cover):
    paint_cans = math.ceil((height*width)/cover)
    print(f'You\'ll need {paint_cans} paint cans')

test_h = int(input('Height of wall: '))
test_w = int(input('width of wall: '))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)