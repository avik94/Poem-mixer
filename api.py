def funct():
    string_input=input("enter a saying or poem: ")
    listt= string_input.split()
    listt_length= len(listt)
    for x in range(listt_length):
        if len(listt[x])<=3:
            lower_word=listt[x].lower()
            listt[x]=lower_word
        elif len(listt[x])>=7:
            upper_word=listt[x].upper()
            listt[x]=upper_word
    result=word_mixer(listt)
    print(" \n")
    print(result)


def word_mixer(listt):
    listt.sort()
    newList= []
    x=len(listt)
    while x > 5:
        firstPOp= listt.pop(-5)
        newList.append(firstPOp)
        secondPop= listt.pop(0)
        newList.append(secondPop)
        thirdPop= listt.pop(-1)
        newList.append(thirdPop)

        if len(listt)==5:
            break
    newWord=" ".join(newList)
    return newWord


if __name__ == '__main__':
    funct()
