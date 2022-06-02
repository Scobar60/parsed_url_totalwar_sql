import json
lines_set = set()
fin = open(r"articles_urls.txt", "r") #  здесь указываете реальные
fout = open(r"new_art.txt", "w")  # пути к файлам
for line in fin:
    if line not in lines_set:
        fout.write(line)
    lines_set.add(line)
fin.close()
fout.close()