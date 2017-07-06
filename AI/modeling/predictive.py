__author__ = 'Edisnel C.C.'

from matplotlib.pyplot import axis
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier as KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn import model_selection, metrics
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder # One Hot Enconding
from sklearn import preprocessing
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from sklearn.preprocessing import Imputer
from sklearn import neighbors
from sklearn.neural_network import MLPClassifier

# Predictive analytics (Classification and regression)



