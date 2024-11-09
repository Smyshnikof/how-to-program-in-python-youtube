# 1.
# text = open("word_count.txt", encoding="UTF-8")
# print(text.read())

# 2.
# try:
#     text = open("word_countd.txt", encoding="UTF-8")
#     print(text.read())
# except:
#     print("Такого файла нет.")
    
    
# 3
# text = open("word_count.txt", encoding="UTF-8")

# count_words = dict()

# for line in text:
#     # print(line.upper())
#     words = line.split()
#     # print(words)
#     # print(len(words))    
#     for word in words:
#         print(word)
#         if word not in count_words:
#             count_words[word] = 1
#         else:
#             count_words[word] += 1

# # print(count_words)

# for word, count in count_words.items():
#     print(f"{word} - {count}")
    

# 4. Pandas
# import pandas as pd

# text = open("word_count.txt", encoding="UTF-8")

# count_words = dict()

# for line in text:
#     words = line.split() 
#     for word in words:
#         print(word)
#         if word not in count_words:
#             count_words[word] = 1
#         else:
#             count_words[word] += 1

# for word, count in count_words.items():
#     print(f"{word} - {count}")
    
# df = pd.DataFrame(list(count_words.items()), columns=["Слово", "Количество"])
# df = df.sort_values(by="Количество", ascending=False)
# print(df.head(30))


# 5.
# import pandas as pd
# import matplotlib.pyplot as mpl

# text = open("word_count.txt", encoding="UTF-8")

# count_words = dict()

# for line in text:
#     words = line.split() 
#     for word in words:
#         print(word)
#         if word not in count_words:
#             count_words[word] = 1
#         else:
#             count_words[word] += 1

# for word, count in count_words.items():
#     print(f"{word} - {count}")
    
# df = pd.DataFrame(list(count_words.items()), columns=["Слово", "Количество"])
# df = df.sort_values(by="Количество", ascending=False)
# print(df.head(30))

# mpl.figure(figsize=(8, 8))
# mpl.bar(df["Слово"][:10], df["Количество"][:10], color="green")
# mpl.title("Топ 10 слов")
# mpl.xlabel("Слово")
# mpl.xticks(rotation=45)
# mpl.ylabel("Количество")
# mpl.show()


# 6. 
from pathlib import Path
import imageio
from wordcloud import WordCloud as WC

text = Path("word_count.txt").read_text(encoding="UTF-8")
print(text)

mask_image = imageio.imread("heart.png")

wordCloud = WC(colormap="terrain", mask=mask_image, background_color="black")
wordCloud = wordCloud.generate(text)
wordCloud = wordCloud.to_file("image.png")
