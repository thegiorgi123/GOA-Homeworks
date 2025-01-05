score_tuple = (2.45, 5.123, 5.1, 6.45, 8.4)
score_list = [2.45, 4.53, 6.46, 8.77]
print(score_tuple)
# არ შეიძლება ცვლილების შეტანა, რადგან ის არის immutable მონაცემთა ტიპი /data type



scores = (1, 2, 3, 4, 1, 1, 2, 3)
print(scores.count(1))
print(scores, len(scores))
print(scores, min(scores))
print(scores, max(scores))

bday_date = (12, "december", "1993", [1, 2, 3, 4, 5, "giorgi"], 5, 6, 12, 13241234, 2)
day, month, year, *rest = bday_date
print(day)
print(month)
print(year)
print(rest)


fav_movies = ("wv", "tvd", "got", "lotr", "hp", "to")
first, *rest = fav_movies
print(first)
print(rest)

print(fav_movies[0])
print(fav_movies[-1])

while True:
    print("ლომი")