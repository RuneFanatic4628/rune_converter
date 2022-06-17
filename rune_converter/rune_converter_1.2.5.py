#Preset Variables
a=0
b=-1
x=None
data=None
EorD=None
rune_req='types'

#Anglo-Saxon - ᚪᛒᚳᛞᛖᚠᚷᚻᛁᛄᚳᛚᛘᚾᚩᛈᚳᚱᛋᛏᚢᚠᚹ ᚳᛋ ᛁᛋ
def Anglo_Encode():
    data=input('What would you like to', EorD, '? ')
    data=data.lower
    for x in list(range(len(data)-1)):
        if data[x]=='a':
            data=data.replace('a', 'ᛅ'[x])
        if data[x]=='b':
            data=data.replace('b', 'ᛒ'[x])
        if data[x]=='c':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
#Elder Futhark Runes - ᚨᛒᚲᛞᛖᚠᚷᚺᛁᛃᚲᛚᛗᚾᛟᛈᚲᚱᛊᛏᚢᚢᚹ ᚲᛊ ᛁᛉ
def Elder_Encode():
    data=input('What would you like to', EorD, '? ')
    data=data.lower
    for x in list(range(len(data)-1)):
        if data[x]=='a':
            data=data.replace('a', 'ᛅ'[x])
        if data[x]=='b':
            data=data.replace('b', 'ᛒ'[x])
        if data[x]=='c':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
        if data[x]=='':
            data=data.replace('', ''[x])
#Younger Futhark Runes - ᛅᛒᚴᛏᛁᚠᚴᚼᛁᛁᚴᛚᛘᚾᚬᛒᚴᚱᛋᛏᚢᚢᚢ ᚴᛋ ᛁᛋ
def Younger_Encode():
    data=input('What would you like to', EorD, '?  ')
    data=data.lower
    for x in list(range(len(data))):
        if data[x]=='a':
            data=data.replace('a', 'ᛅ'[x])
        if data[x]=='b' or data[x]=='p':
            data=data.replace('b', 'ᛒ'[x])
            data=data.replace('p', 'ᛒ'[x])
        if data[x]=='c' or data[x]=='k' or data[x]=='q' or data[x]=='g':
            data=data.replace('c', 'ᚴ'[x])
            data=data.replace('k', 'ᚴ'[x])
            data=data.replace('q', 'ᚴ'[x])
            data=data.replace('g', 'ᚴ'[x])
        if data[x]=='d' or data[x]=='t':
            data=data.replace('d', 'ᛏ'[x])
            data=data.replace('t', 'ᛏ'[x])
        if data[x]=='e' or data[x]=='i' or data[x]=='j' or data[x]=='y':
            data=data.replace('y', 'ᛁ'[x])
            data=data.replace('j', 'ᛁ'[x])
            data=data.replace('i', 'ᛁ'[x])
            data=data.replace('e', 'ᛁ'[x])
        if data[x]=='f':
            data=data.replace('f', 'ᚠ'[x])
        if data[x]=='h':
            data=data.replace('h', 'ᚼ'[x])
        if data[x]=='l':
            data=data.replace('l', 'ᛚ'[x])
        if data[x]=='m':
            data=data.replace('m', 'ᛘ'[x])
        if data[x]=='n':
            data=data.replace('n', 'ᚾ'[x])
        if data[x]=='o':
            data=data.replace('o', 'ᚬ'[x])
        if data[x]=='r':
            data=data.replace('r', 'ᚱ'[x])
        if data[x]=='s' or data[x]=='z':
            data=data.replace('s', 'ᛋ'[x])
            data=data.replace('z', 'ᛋ'[x])
        if data[x]=='u' or data[x]=='v' or data[x]=='w':
            data=data.replace('u', 'ᚢ'[x])
            data=data.replace('v', 'ᚢ'[x])
            data=data.replace('w', 'ᚢ'[x])
        if data[x]=='x':
            data=data.replace('x', 'ᚴᛋ')

def Rune_Nav_En():
    if rune_req=='Anglo-Saxon Runes':
        Anglo_Encode()
    if rune_req=='Elder Futhark Runes':
        Elder_Encode()
    if rune_req=='Younger Futhark Runes':
        Younger_Encode()

while rune_req=='types':
    EorD=input('Decode or Encode? ')
    if EorD=='Encode':               #Encoding runes
        while rune_req=='types' :
            rune_req=input('Which rune type are you converting? Enter "types" to view available rune types. ')
            if rune_req=='types':
                print('+-----------------------+')
                print('|     Rune   Types      |')
                print('+-----------------------+')
                print('|   Anglo-Saxon Runes   |')
                print('|  Elder Futhark Runes  |')
                print('| Younger Futhark Runes |')
                print('+-----------------------+')
            if rune_req!='Anglo-Saxon Runes' and rune_req!='Elder Futhark Runes' and rune_req!='Younger Futhark Runes' and rune_req!='types':
                print('That is not an available rune type. Please enter "types" to see a list of available rune types.')
        Rune_Nav_En()
    if EorD=='Decode':               #Decoding runes
        while rune_req=='types' :

            rune_req=input('Which rune tpye are you converting? Enter "types" to view available rune types. ')
            if rune_req=='types':
                print('+-----------------------+')
                print('|     Rune   Types      |')
                print('+-----------------------+')
                print('|   Anglo-Saxon Runes   |')
                print('|  Elder Futhark Runes  |')
                print('| Younger Futhark Runes |')
                print('+-----------------------+')
            if rune_req!='Anglo-Saxon Runes' and rune_req!='Elder Futhark Runes' and rune_req!='Younger Futhark Runes' and rune_req!='types':
                print('That is not an available rune type. Please enter "types" to see a list of available rune types.')
        print('This feature is still under development.')
        break
    if EorD!='Encode' or EorD!='Decode':
        print('You must input "Decode" or "Encode"!')
print('All Done!')
