from boltiot import Bolt
import time
import conf
import signal

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)


def handler(signum, frame):
    response = mybolt.analogWrite('4', 0)
    response = mybolt.digitalWrite('1', "LOW")
    msg = "\n!!! Program terminated !!!\n"
    print(msg)
    # print(response, end='\n')
    exit(1)


signal.signal(signal.SIGINT, handler)


def showTime():
    t = time.localtime()
    result = time.strftime("%H:%M:%S", t)
    print(result)


def morse_buzzer(morse):
    timeVal = 2
    high = 16
    low = 2
    hashVal = 32
    for code in morse:
        showTime()
        if code == '-':
            print(code)
            response = mybolt.analogWrite('4', high)
            print(response)
            time.sleep(timeVal)
            showTime()
        elif code == '.':
            print(code)
            response = mybolt.analogWrite('4', low)
            print(response)
            time.sleep(timeVal)
            showTime()
        elif code == '#':
            print(code)
            response = mybolt.analogWrite('4', hashVal)
            print(response)
            time.sleep(timeVal)
            showTime()
        response = mybolt.analogWrite('4', 0)
        print("--------BUFFER-------", response)
        time.sleep(4)


def morse_led(morse):
    for code in morse:
        showTime()
        if code == '-':
            timeVal = 4
            print(code)
            response = mybolt.digitalWrite('1', 'HIGH')
            print(response)
            time.sleep(timeVal)
            showTime()
        elif code == '.':
            timeVal = 2
            print(code)
            response = mybolt.digitalWrite('1', 'HIGH')
            print(response)
            time.sleep(timeVal)
            showTime()
        elif code == '#':
            timeVal = 2
            print(code)
            response = mybolt.digitalWrite('1', 'LOW')
            print(response)
            time.sleep(timeVal)
            showTime()
        response = mybolt.digitalWrite('1', 'LOW')
        print("--------BUFFER-------", response)
        time.sleep(2)


morseDict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}


inp = input("Enter your message: ")

# contains each character
inpList = list(inp)

# contains morse for each character
morseStrList = []

# contains each morse symbol -> dot/dash, # used for seperation of alphabets
morseList = []

for i in range(len(inpList)):
    ele = inpList[i].upper()
    if ele in morseDict.keys():
        morseStrList.append(morseDict[ele])

for ele in morseStrList:
    for m in ele:
        morseList.append(m)
    morseList.append('#')

# print(morseList)

try:
    ind = morseList.index('/')
except:
    ind = len(morseList)
ind -= 1
firstFilter = morseList[:ind]
print(firstFilter)

if firstFilter == []:
    print("No message to deliver..... Terminating program")
else:
    choice = input("Enter 1 for using LED and 2 for using Buzzer: ")
    if choice == '1':
        morse_led(firstFilter)
    elif choice == '2':
        morse_buzzer(firstFilter)
    else:
        print("Invalid Input..... Terminating program")

print("Program finished")
