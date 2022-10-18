import pyperclip

while True:
    try:
        inputstring = input("Enter current price (N/n for exit):")
        if inputstring == 'N' or inputstring == 'n':
            break
        else:
            currentprice = float(inputstring)
        while True:
            inputstring = input("Enter target price (N/n for new current price):")
            if inputstring == 'N' or inputstring == 'n':
                break
            else:
                price = float(inputstring)
            try:
                outputstring = str(int((price - currentprice) / currentprice * 10000)/100) + '%'
                print(outputstring, '   (Copied to clipboard!)')
                pyperclip.copy(outputstring)
            except:
                pass
    except:
        pass
