def sentence_filter():
    filtered_words = []
    
    word_counter = 0
    
    #only stores 5 different words
    while word_counter<5:
        word_list = input("Enter filtered words:\n")
        filtered_words.append(word_list)
        word_counter = word_counter + 1
    
    sentence = input("Enter a sentence:\n")
    
    sentence = sentence.split(" ")

    censored_sentence = []

    for word in sentence:
        if word in filtered_words:
            censored_sentence.append("*" * len(word))
        else:
            censored_sentence.append(word)

    print(" ".join(censored_sentence))
    
sentence_filter()