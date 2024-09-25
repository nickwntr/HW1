def single_root_words(root_word,*other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    print(same_words)

single_root_words("Торт","Малина","Торты")
single_root_words("Сорт", "Сортировка","Сорить")