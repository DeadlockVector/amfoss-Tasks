(number_words, m) = map(int, input().split())   #input

final_spell = ''   #string for final spell
dict_translator = {}         #dictionary which acts like a translator

for i in range(m):
    (magic, normal) = map(str, input().split())
    dict_translator[magic] = normal        #adding the key-value pairs to the dictionary

init_spell = input()        #input of spell

l1 = init_spell.split()     #list of the input spell, split into words

#print(dict_translator)
#print(l1)

for i in l1:                                          #checking length of words and replacing whenever needed
    if len(dict_translator[i]) < len(i):
        final_spell += dict_translator[i] + ' '
    elif len(dict_translator[i]) >= len(i):
        final_spell += i + ' '

print(final_spell)
