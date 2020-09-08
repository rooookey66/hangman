import random

def word_select():
    word = input("出題者は、単語を入力してください：")
    return word

def word_select_rand():
    word_list = ["apple","pen","pine","orange"]
    return word_list[random.randint(0,3)]

def hangman(word):

    wrong = 0
    stages = ["",
    "________        ",
    "|       |       ",
    "|       o       ",
    "|      /|\      ",
    "|      / \      ",
    "|               "
    ]
    rletters = list(word) # "w" "o" "r" "d"のように１文字ずつリストになる
    board = ["_"] * len(word)
    win = False
    
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        char = input("1文字を予想してください：")
        
        if char in rletters:
            c_index = rletters.index(char)
            board[c_index] = char
            rletters[c_index] = "$"
        else:
            wrong += 1

        print(" ".join(board))

        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("回答者の勝ちです！")
            print(" ".join(board))
            win = True
            break
    
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("回答者の負けです！正解は{}でした！".format(word))

word = word_select_rand()
hangman(word)

