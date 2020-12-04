#ca = float(input('Valor do cateto adjacente'))
#co = float(input('Valor do cateto oposto'))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('O valor da Hipotenusa é {:.2f}'.format(hi))

#import math
#ca = float(input('Valor do cateto adjacente'))
#co = float(input('Valor do cateto oposto'))
#hi = math.hypot(ca , co)
#print('O valor da Hipotenusa é {:.2f}'.format(hi))

from math import hypot
ca = float(input('Valor do cateto adjacente'))
co = float(input('Valor do cateto oposto'))
hi = hypot(ca, co)
print('O valor da Hipotenusa é {:.2f}'.format(hi))
