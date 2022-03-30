from nis import match
math=0
a=0
b=0
def colisio(self,a,b):
    distancia = math.sqrt(math.pow((a.position_x - b.position_x),2) + math.pow((a.position_y - b.position_y),2))
   #print(distancia)
    if distancia <= (a.radius):
       return True
    else:
       return False