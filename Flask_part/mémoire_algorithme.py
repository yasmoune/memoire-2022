# Récupération des fichiers du drivea
# Manipulation des données
import glob
import os

import math
import pandas as pd
import numpy as np

from shapely.geometry import Point
from shapely.geometry import Polygon
import shapely.geometry

import matplotlib.pyplot as plt
import plotly.express as px
import folium

data = pd.read_csv("/content/drive/My Drive/Mémoire/polygon_radius_complete.csv")

"""Observer la similarité entre un vecteur donné et l'ensemble des vecteurs"""

def difference(origin_vector, vector_matrix): #On pénalise quand il y en a plus d'éléments ou qu'il y en a moins
  dif = sum(np.square(origin_vector - vector_matrix))**(1/2)
  return dif

def difference_neg(origin_vector, vector_matrix): # On ne pénalise pas quand il y a plus d'éléments
  data = origin_vector - vector_matrix
  index = data[data <= 0].index

  dif = difference(origin_vector.loc[index], vector_matrix.loc[index])
  return dif

def difference_neg_np(origin_vector, vector_matrix): # On ne pénalise pas quand il y en a plus // en format numpy (plus rapide)
  data = origin_vector - vector_matrix
  index = np.where(data <= 0)

  dif = difference(origin_vector[index], vector_matrix[index])
  return dif
