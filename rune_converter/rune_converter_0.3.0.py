#Preset Variables
a=None
b=0
x=None
z=None
EN_Alph='abcdefghijklmnopqrstuvwxyz'
data=None
#Rune Alphabets
#English - ABCDEFGHIJKLMNOPQRSTUVWXYZ
#Anglo-Saxon - ᚪᛒᚳᛞᛖᚠᚷᚻᛁᛄᚳᛚᛘᚾᚩᛈᚳᚱᛋᛏᚢᚠᚹ ᚳᛋ ᛁᛋ
#Elder Futhark Runes - ᚨᛒᚲᛞᛖᚠᚷᚺᛁᛃᚲᛚᛗᚾᛟᛈᚲᚱᛊᛏᚢᚢᚹ ᚲᛊ ᛁᛉ
#Younger Futhark Runes - ᛅᛒᚴᛏᛁᚠᚴᚼᛁᛁᚴᛚᛘᚾᚬᛒᚴᚱᛋᛏᚢᚢᚢ ᚴᛋ ᛁᛋ

def runetype():
        a=input('Which rune tpye are you converting? Enter "types" to view possible rune types. ')
        b=1
        if a=='types':
            print('+-----------------------+')
            print('|     Rune   Types      |')
            print('+-----------------------+')
            print('|   Anglo-Saxon Runes   |')
            print('|  Elder Futhark Runes  |')
            print('| Younger Futhark Runes |')
            print('+-----------------------+')
            b=0

def Anglo_Encode():
    data=input('What would you like to', x, '? ')

def Elder_Encode():
    data=input('What would you like to', x, '? ')

def Younger_Encode():
    data=input('What would you like to', x, '?  ')
    
    for z in


def Rune_Nav():
    if a=='Anglo-Saxon Runes':
        Anglo_Encode()
    if a=='Elder Futhark Runes':
        Elder_Encode()
    if a=='Younger Futhark Runes':
        Younger_Encode()

while a is None:
    x=input('Decode or Encode? ')
    if x=='Encode':               #Encoding runes
        while b==0 :
            runetype()
        Rune_Nav()
    if x=='Decode':               #Decoding runes
        while b==0 :
            runetype()
        Rune_Nav()
    if x!='Encode' or x!='Decode':
        print('You must input "Decode" or "Encode"!')
print('All Done!')
