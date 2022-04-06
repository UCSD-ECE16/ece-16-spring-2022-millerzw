
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



test_list = ['Quotient','Mustn\'t','Yellow', 'Honest', 'Thursday', 'Christmas',
             'Alliteration', 'Information', 'Education', 'Fish', 'Numbers!',
             'Toyota!', 'Mother-in-law', 'Laps', 'Slap', 'August', 'empty-handed',
             'Ice-cream', 'Years', 'Yankee', 'Yawn', 'Young', 'Yard', 'Quiet', 'Quack']

for i, word in enumerate(test_list):
    out1 = eng_to_pig(word)
    #out2 = pig_latin_to_english(out1)
    print(i+1, 'inputted word:', word)
    print(i+1, 'english -> p-latin:', out1)
   # print(i+1, 'p-latin -> english:', out2)
