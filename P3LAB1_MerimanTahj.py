r = int(input())
g = int(input())
b = int(input())

rgb_color = [r, g, b]
gray = min(rgb_color)

if r == min(rgb_color):
    r = 0
else:
    r = r - gray
if g == min(rgb_color):
    g = 0
else:
    g = g - gray
if b == min(rgb_color):
    b = 0 
else:
    b = b - gray
    
print (r,g,b)
