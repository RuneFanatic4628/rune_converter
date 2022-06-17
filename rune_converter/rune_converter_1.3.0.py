#Preset Variables
a=0
b=-1
c=None
d=None
e=-1
x=None
data=None
EorD=None
rune_req=None

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
    data=input('What would you like to encode?  ')
    data=data.lower
    for x in list(range(len(str(data)))):
        data=data.replace('a', 'ᛅ')
        data=data.replace('b', 'ᛒ')
        data=data.replace('p', 'ᛒ')
        data=data.replace('c', 'ᚴ')
        data=data.replace('k', 'ᚴ')
        data=data.replace('q', 'ᚴ')
        data=data.replace('g', 'ᚴ')
        data=data.replace('d', 'ᛏ')
        data=data.replace('t', 'ᛏ')
        data=data.replace('y', 'ᛁ')
        data=data.replace('j', 'ᛁ')
        data=data.replace('i', 'ᛁ')
        data=data.replace('e', 'ᛁ')
        data=data.replace('f', 'ᚠ')
        data=data.replace('h', 'ᚼ')
        data=data.replace('l', 'ᛚ')
        data=data.replace('m', 'ᛘ')
        data=data.replace('n', 'ᚾ')
        data=data.replace('o', 'ᚬ')
        data=data.replace('r', 'ᚱ')
        data=data.replace('s', 'ᛋ')
        data=data.replace('z', 'ᛋ')
        data=data.replace('u', 'ᚢ')
        data=data.replace('v', 'ᚢ')
        data=data.replace('w', 'ᚢ')
        data=data.replace('x', 'ᚴᛋ')
def Rune_Nav_En():
    if rune_req=='Anglo-Saxon Runes':
        Anglo_Encode()
    if rune_req=='Elder Futhark Runes':
        Elder_Encode()
    if rune_req=='Younger Futhark Runes':
        Younger_Encode()
while rune_req is None:
    EorD=input('Decode or Encode? ')
    if EorD=='Encode':               #Encoding runes
        while rune_req=='types' or rune_req is None :
            rune_req=input('Which rune type are you converting? Enter "types" to view available rune types. ')
            if rune_req=='types':
                print('                             +-----------------------+')
                print('                             |     Rune   Types      |')
                print('                             +-----------------------+')
                print('                             |   Anglo-Saxon Runes   |')
                print('                             |  Elder Futhark Runes  |')
                print('                             | Younger Futhark Runes |')
                print('                             +-----------------------+')
            if rune_req!='Anglo-Saxon Runes' and rune_req!='Elder Futhark Runes' and rune_req!='Younger Futhark Runes' and rune_req!='types':
                print('That is not an available rune type. Please enter "types" to see a list of available rune types.')
        Rune_Nav_En()
    if EorD=='Decode':               #Decoding runes
        while rune_req=='types' or rune_req is None:
            rune_req=input('Which rune type are you converting? Enter "types" to view available rune types. ')
            if rune_req=='types':
                print('                             +-----------------------+')
                print('                             |     Rune   Types      |')
                print('                             +-----------------------+')
                print('                             |   Anglo-Saxon Runes   |')
                print('                             |  Elder Futhark Runes  |')
                print('                             | Younger Futhark Runes |')
                print('                             +-----------------------+')
            if rune_req!='Anglo-Saxon Runes' and rune_req!='Elder Futhark Runes' and rune_req!='Younger Futhark Runes' and rune_req!='types':
                print('That is not an available rune type. Please enter "types" to see a list of available rune types.')
        print('This feature is still under development.')
        break
    if EorD!='Encode' and EorD!='Decode':
        print('You must input "Decode" or "Encode"!')
print('All Done!')
