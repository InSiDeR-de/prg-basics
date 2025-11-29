def hide(card_number):
    i=0
    result=''
    for x in card_number:    
        i+=1
        if i in [1,2,16,15,14,13]:
            result+=x
            continue
        else:
            result+="*"
            continue
    return result

if __name__ == "__main__":
    print(hide("1234567890098765"))
    print(hide("4565367890098987"))
    print(hide("6756667890534645"))