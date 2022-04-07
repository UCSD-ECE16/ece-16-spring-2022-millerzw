import enchant as e
dictionary=e.Dict('en_US')

def eng_to_pig(phrase):

    words=phrase.split("-")
    new_phrase=""

    for i,word in enumerate(words):
        #Case Vowel
        vowels="aeiouAEIOU"
        punct="!.@#$%^&*"
        if (word[0] in vowels):
            words[i]+="yay"
        #Case Consonant or Y or Qu
        else:
            for j, letter in enumerate(word):
                #Case Qu
                if (word[0] in "qQ" and word[1] in "uU"):
                    words[i]=word[2:]+word[:2]+"ay"
                    break
                elif (letter in vowels):
                    #iterate up to first vowel and add that section to the end
                    words[i]=word[j:]+(word[:j])
                    if word[0] in "yY":
                        #if starts with y then add ey
                        words[i]+="ey"
                    else:
                        #if starts with consonant then add ay
                        words[i]+="ay"
                    break
        for k, letter in enumerate(words[i]):
            if (letter in punct):
                words[i]=words[i][:k]+words[i][(k+1):]+letter
                break
        if ("-" in phrase):
            new_phrase+=words[i]+"-"
        else:
            new_phrase += words[i] + " "
    new_phrase=new_phrase[:-1]
    return new_phrase

#dictionary.chedck('word')

def pig_to_eng(phrase):
    words=phrase.split("-")
    new_phrase=""
    for i, word in enumerate(words):
        vowels = "aeiouAEIOU"
        punct = "!.@#$%^&*"
        append_punct=""
        #Case where word starts with vowel
        y_word = word[-3] + word[:-3]
        if (dictionary.check(word[:-3])):
            words[i]=words[i][:-3]

        #Case where the first letter of the word is Y: note that when the first letter is y
        # the second letter will always be a vowel, so no need for iteration

        elif (dictionary.check(y_word)):
            words[i]=y_word

        if (word[-1] in punct):
            append_punct=word[-1]
            word_to_check=word[:-3]
        else:
            append_punct=""
            word_to_check=word[:-2]
        #Case where it started with a consonant: note we should never have a case where
        # there are greater than 5 consonants in a row at the start of a word
        # this just shifts the end letter to the front and checks if a word is then created
        for k in range(5):
            word_to_check=word_to_check[-1]+word_to_check[:-1]
            if (dictionary.check(word_to_check)):
                words[i]=word_to_check+append_punct
                break
        if ("-" in phrase):
            new_phrase += words[i] + "-"
        else:
            new_phrase += words[i] + " "
    new_phrase=new_phrase[:-1]
    return new_phrase




test_list = ['Quotient','Mustn\'t','Yellow', 'Honest', 'Thursday', 'Christmas',
             'Alliteration', 'Information', 'Education', 'Fish', 'Numbers!',
             'Toyota!', 'Mother-in-law', 'Laps', 'Slap', 'August', 'empty-handed',
             'Ice-cream', 'Years', 'Yankee', 'Yawn', 'Young', 'Yard', 'Quiet', 'Quack']

for i, word in enumerate(test_list):
    out1 = eng_to_pig(word)
    out2 = pig_to_eng(out1)
    print(i+1, 'inputted word:', word)
    print(i+1, 'english -> p-latin:', out1)
    print(i+1, 'p-latin -> english:', out2)

myCaseAE=eng_to_pig("yell")
myCaseAP=pig_to_eng(eng_to_pig("yell"))
print(myCaseAE)
print(myCaseAP)
myCaseBE=eng_to_pig("fight")
myCaseBP=pig_to_eng(eng_to_pig("fight"))
print(myCaseBE)
print(myCaseBP)

