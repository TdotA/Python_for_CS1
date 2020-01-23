def disemvoweling (text) :
    vowels = ''
    txt = ''
    i = 0
    while i < len(text) :
        if  text[i] in 'aeiouAEIOU' :
            vowels = vowels + text[i]
            
        else:
            txt = txt + text[i]
        i = i + 1 
    return (txt + vowels)
#print (disemvoweling("Banana is good!"))

def first_vowel (word) :
    vow = ['a','e','i','o','u']
    for char in word : 
        if char in 'aeiouAEIOU' : 
            return char
#print (first_vowel('hamburger'))

def undo_disemvowel(text):
    vowels = ''
    non_vowels = ''
    final_answer= ''
    i= 0 
    c = 0
    while i<len(text):
        if  text[i] in 'aeiouAEIOU' :
            vowels = vowels + text[i]
            
        else:
            non_vowels = non_vowels + text[i]
        i = i + 1 
    while c <len(vowels):
        for char in non_vowels :
            if char == '*':
                final_answer = final_answer + list(vowels)[c]
                c = c +1
            else:
                final_answer = final_answer + char 
    return final_answer
print(undo_disemvowel('B*n*n* *s g**d!aaaioo'))






