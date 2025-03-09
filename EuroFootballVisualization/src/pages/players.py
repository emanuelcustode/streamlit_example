import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

df_players = pd.read_csv('EuroFootballVisualization/dataset/archive/euro_lineups.csv')


player_games = df_players['name'].value_counts().sort_values(ascending=False)

# Top 15 Trainer mit den meisten Spielen anzeigen
top_players = player_games.head(15)

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.bar(top_players.index, top_players.values, color='b')
plt.xticks(rotation=90, ha='right')
plt.yticks(np.arange(0, max(top_players.values) + 1, 2))
plt.ylabel('Anzahl der Spiele')
plt.title('Top 15 Spieler mit den meisten EM-Spielen')
plt.tight_layout()
st.pyplot(plt.gcf())