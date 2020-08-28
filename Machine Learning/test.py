#1.Read the three csv files which contains the score of same students in term1 for each Subject
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dfMaths = pd.read_csv('/Users/prateekb/Downloads/Dataset/MathScoreTerm1.csv')
dfDS = pd.read_csv('/Users/prateekb/Downloads/Dataset/DSScoreTerm1.csv')
dfPhysics = pd.read_csv('/Users/prateekb/Downloads/Dataset/PhysicsScoreTerm1.csv')
