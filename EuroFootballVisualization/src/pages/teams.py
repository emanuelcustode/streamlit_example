import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_teams = pd.read_csv('EuroFootballVisualization/dataset/archive/euro_summary.csv')

winner = df_teams['winner'].value_counts()

plt.figure(figsize = (10,10))
plt.bar(winner.index, winner.values)
plt.xticks(rotation = 45)
plt.yticks(np.arange(0, max(winner.values) + 1, 1))
plt.xlabel('Teams')
plt.ylabel('Number of Wins')
plt.title('Welche Nation holt die meisten EM-Titel? ')
plt.tight_layout()

st.pyplot(plt.gcf())