import pyperclip

while True:
    try:
        stoplossinput = input("Enter stop loss price (N/n for exit): ")
        if stoplossinput == 'N' or stoplossinput == 'n':
            break
        stoploss = float(stoplossinput)
        while True:
            try:
                entryinput = input("Enter entry price (N/n for new stop loss): ")
                if entryinput == 'N' or entryinput == 'n':
                    break
                entry = float(entryinput)
                #targetinput = input("Enter target price (N/n for new stop loss): ")
                #if targetinput == 'N' or targetinput == 'n':
                #    break
                #target = float(targetinput)
                riskpercentageinput = input("Enter desired risk percentage (e.g. '0.5') (N/n for new stop loss): ")
                if riskpercentageinput == 'N' or riskpercentageinput == 'n':
                    break
                riskpercentage = float(riskpercentageinput)
                slpercentage = abs(((entry - stoploss) / stoploss) * 100)
                positionsizeusd = 100000 * riskpercentage / slpercentage
                positionsizesymbol = positionsizeusd / entry
                outputstring = str(int(positionsizesymbol*100)/100)
                pyperclip.copy(outputstring)
                print(outputstring, '   (Copied to clipboard!)')
            except:
                pass
    except:
        pass