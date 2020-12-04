#import math
#an = float(input('Digite o ângulo que você deseja: '))
#seno = math.sin(math.radians(an))
#print('O ângulo de {} tem o SENO de {:.2f}'.format(an , seno))
#cosseno = math.cos(math.radians(an))
#print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an ,cosseno))
#tan = math.tan(math.radians(an))
#print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an ,tan))

from math import sin, cos, tan, cos, radians
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tan = tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))
