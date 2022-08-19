feedback = (input("Поділіться будь ласка враженнями про ваш відпочинок на нашому курорті\n> ")).lower()
keywords = {"меню": 0, "спортзал": 0, "обслуговування": 0}
for word in keywords:
    start = 0
    while word in feedback[start:]:
        keywords[word] += 1
        slicer = feedback[start:].find(word) + len(word)
        start += slicer

print("У відгуку меню згадано", keywords["меню"], "разів, спортзал -", keywords["спортзал"], "разів, обслуговування -",
      keywords["обслуговування"], "разів.")

if len(feedback) > 60:
    print("Шановний клієнте, дякуємо за ґрунтовний відгук та даруємо Вам знижку 15% на наступний візит!")
