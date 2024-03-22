from random import uniform
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 

print("Seleccione el metodo para calcular Pi:")
print("1.- Agujas de buffon\n2.- Dardos\n")
if int(input())==1:
  sns.set_theme()
  mngr = plt.get_current_fig_manager()
  mngr.window.setGeometry = (2250, 100, 640, 800)

  NUM = int(input("Ingrese el numero de Agujas a lanzar:")) #Numero de Agujas
  d = 2
  l = d

  point_x = np.random.uniform(-3, 3, NUM)
  point_y = np.random.uniform(-3, 3, NUM)
  angle = np.random.uniform(-np.pi/2, np.pi/2, NUM)
  def is_in(n, start, end):
      if start < n < end or start > n > end :
          return True

  def intersect(p_x, p_y, theta, l):
      x1 = p_x + (l/2)*np.cos(theta)
      y1 = p_y + (l/2)*np.sin(theta)

      x2 = p_x - (l/2)*np.cos(theta)
      y2 = p_y - (l/2)*np.sin(theta)

      if is_in(0, y1, y2) or is_in(-2, y1, y2) or is_in(2, y1, y2) or is_in(4, y1, y2) or is_in(-4, y1, y2):
          return True, (x1, y1), (x2, y2)
      else:
          return False, (x1, y1), (x2, y2)

  fig = plt.figure(1, figsize=(6, 15))
  fig.suptitle("Simulación de las Agujas de Buffon")
  ax1 = fig.add_subplot(2, 1, 1)
  ax1.plot([-4, 4],[0,0], c='b')
  ax1.plot([-4, 4],[2, 2], c='b')
  ax1.plot([-4, 4],[4, 4], c='b')
  ax1.plot([-4, 4],[-2, -2], c='b')
  ax1.plot([-4, 4],[-4, -4], c='b')

  ax2 = fig.add_subplot(2, 1, 2)
  num_int = 0
  ratio = np.zeros(NUM)
  x = np.arange(NUM)
  for i in range(1, NUM):
      intersected, (x1, y1), (x2, y2) = intersect(point_x[i], point_y[i], angle[i], l)
      if intersected == True:
          color = 'red' #Las agujas que intersecten con las líneas se pintaran de rojo.
          num_int = num_int + 1.0
          ratio[i] = num_int/i
      else:
          color = 'blue' #Las agujas que NO intersecten con las líneas se pintaran de rojo.
          ratio[i] = num_int/i


      ax1.title.set_text("# de Iteración del Metodo de Monte Carlo: {}".format(i))
    
      ax1.plot([x1, x2], [y1, y2], c= color, linewidth=0.5, alpha=0.7)
    
      ax2.plot(x[:i], 2/ratio[:i], c= 'r', linewidth=0.1) 
    
      ax2.title.set_text("Valor estimado de PI = {}".format(2/ratio[i]))
      plt.pause(0.0000001)

  plt.show()
else:
   
  N = int(input("Digite la cantidad de dardos a tirar: "))
  i = 0
  a = 0
  listax = list()
  listay = list()
  listanx = list()
  listany = list()
  fig, ax = plt.subplots()
  ax.add_patch(plt.Circle((0,0),1,fill=False,color='black'))
  plt.gca().set_aspect('equal')

  while i<N:
    x = uniform(-1,1)
    y = uniform(-1,1)
    h = math.sqrt((x*x)+(y*y))
    if h<=1:
      listax.append(x)
      listay.append(y)
      a += 1
    else:
      listanx.append(x)
      listany.append(y)
    i += 1
  pi = round(((4*a)/N),5)
  print("Pi = ",pi)
  plt.xlabel("Eje X")
  plt.ylabel("Eje Y")
  plt.title("Grafica de dardos")
  plt.scatter(listay,listax,5,color="green",label="Acertado")
  plt.scatter(listany,listanx,5,color="red",label="No Acertado")
  plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
  imprimir = 'π = ' + str(pi)
  plt.text(1.25,0.5,imprimir,fontsize=15)
  plt.show()