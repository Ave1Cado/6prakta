import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Users\\Кырылюк Артём\\Desktop\\gk\\dataset.csv')

# Линейные графики
plt.figure(figsize=(10, 6))
plt.plot(df['danceability'], label='Танцевальность')
plt.plot(df['energy'], label='Энергия')
plt.title('Танцевальность и Энергия Треков')
plt.xlabel('Индекс трека')
plt.ylabel('Значение')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['valence'], label='Валентность')
plt.plot(df['loudness'], label='Громкость')
plt.title('Валентность и громкость треков')
plt.xlabel('Индекс трека')
plt.ylabel('Значение')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['speechiness'], label='Речитативность')
plt.plot(df['acousticness'], label='Акустичность')
plt.title('Речетативность и акустичность треков')
plt.xlabel('Индекс трека')
plt.ylabel('Значение')
plt.legend()
plt.show()

# Столбчатые диаграммы
plt.figure(figsize=(10, 6))
sns.barplot(x=df['playlist_genre'], y=df['danceability'], color='blue')
plt.title('Танцевальность по жанрам')
plt.xlabel('Жанр')
plt.ylabel('Танцевальность')
plt.legend()
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=df['playlist_genre'], y=df['energy'], color='orange')
plt.title('Энергия по жанрам')
plt.xlabel('Жанр')
plt.ylabel('Энергия')
plt.legend()
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=df['playlist_genre'], y=df['valence'], color='green')
plt.title('Валентность по жанрам')
plt.xlabel('Жанр')
plt.ylabel('Валентность')
plt.legend()
plt.xticks(rotation=45)
plt.show()


# Круговые диаграммы
one= df['playlist_genre'].value_counts()
plt.figure(figsize=(10, 6))
plt.pie(one, labels=one.index, autopct='%1.1f%%')
plt.title('Доля жанров в плейлисте')
plt.show()

two= df['playlist_subgenre'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.pie(two, labels=two.index, autopct='%1.1f%%')
plt.title('Топ 10 поджанров в плейлисте')
plt.show()

# Диаграммы рассеяния
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['danceability'], y=df['energy'], data=df)

plt.title('Взаимосвязь между танцевальностью и энергией')
plt.xlabel('Танцевальность')
plt.ylabel('Энергия')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['valence'], y=df['loudness'], data=df)
plt.title('Взаимосвязь между валентностью и громкостью')
plt.xlabel('Валентность')
plt.ylabel('Громкость')
plt.legend()
plt.show()

# Гистограммы
plt.figure(figsize=(10, 6))
sns.histplot(df['danceability'], bins=20, kde=True, color='blue')

plt.title('Гистограмма танцевальности')
plt.xlabel('Танцевальность')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['energy'], bins=20, kde=True, color='orange')
plt.title('Гистограмма энергии')
plt.xlabel('Энергия')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['valence'], bins=20, kde=True, color='green')
plt.title('Гистограмма валентности')
plt.xlabel('Валентность')
plt.legend()
plt.show()