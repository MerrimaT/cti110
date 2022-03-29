user_text = input()
not_letters = ' .!,'

count = 0
for charc in user_text:   
    if charc not in not_letters:
        count += 1
print(count)

