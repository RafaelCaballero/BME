# -*- coding: utf-8 -*-
import numpy as np

# rendimiento a 'dias' días
def rendimiento(precios,dias=1):
  r = precios[dias:]/precios[:-dias] -1
  return r

# rendimiento total a partir de rendimientos individuales
def rendimiento_total(rendimientos):
  r = np.prod(1+rendimientos)-1
  return r