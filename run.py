while True:
    words = []
    for line in open('input.txt').readlines():
        word = line.strip().lower()
        if len(word) > 0 and word not in words:
            words.append(word)

    matches = [[word, 0, 0] for word in words]

    telescope = input('Введите телескопизм: ').lower()

    for word in matches:
        for i in range(len(word[0])):
            if telescope[i] == word[0][i]:
                word[1] += 1
            else:
                break
        for i in range(len(word[0])):
            if telescope[-i-1] == word[0][-i-1]:
                word[2] += 1
            else:
                break

    finded = []
    for word1 in matches:
        if word1[1] > 0:
            for word2 in matches:
                if word2[2] > 0:
                    if word1[1] + word2[2] >= len(telescope):
                        finded.append([word1[0], word2[0]])

    if len(finded) == 0:
        print('Телескопизм не найден')
    else:
        for pair in finded:
            print(pair[0]+' '+pair[1])