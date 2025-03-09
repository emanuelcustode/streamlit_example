import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


df_coaches = pd.read_csv('EuroFootballVisualization/dataset/archive/euro_coaches.csv')

coach_participation = df_coaches.groupby('name')['year'].nunique().sort_values(ascending=False)

top_coaches = coach_participation.head(20)

plt.figure(figsize=(10, 6))
plt.bar(top_coaches.index, top_coaches.values, color='b')
plt.xticks(rotation=90, ha='right')
plt.yticks(np.arange(0, max(top_coaches.values) + 1, 1))
plt.ylabel('Teilnahmen')
plt.title('Top 15 Trainer mit den meisten EM-Teilnahmen')
plt.tight_layout()

st.pyplot(plt.gcf())

coach_games = df_coaches['name'].value_counts().sort_values(ascending=False)

# Top 15 Trainer mit den meisten Spielen anzeigen
top_coaches_games = coach_games.head(15)

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.bar(top_coaches_games.index, top_coaches_games.values, color='b')
plt.xticks(rotation=90, ha='right')
plt.yticks(np.arange(0, max(top_coaches_games.values) + 1, 2))
plt.ylabel('Anzahl der Spiele')
plt.title('Top 15 Trainer mit den meisten EM-Spielen')
plt.tight_layout()
st.pyplot(plt.gcf())