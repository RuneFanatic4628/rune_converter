#Preset Variables
a=None
b=0
x=None
#Rune Alphabets
#English - ABCDEFGHIJKLMNOPQRSTUVWXYZ
#Anglo-Saxon - ᚪᛒᚳᛞᛖᚠᚷᚻᛁᛄᚳᛚᛘᚾᚩᛈᚳᚱᛋᛏᚢᚠᚹ ᚳᛋ ᛁᛋ
#Elder Futhark Runes - ᚨᛒᚲᛞᛖᚠᚷᚺᛁᛃᚲᛚᛗᚾᛟᛈᚲᚱᛊᛏᚢᚢᚹ ᚲᛊ ᛁᛉ
#Younger Futhark Runes - ᛅᛒᚴᛏᛁᚠᚴᚼᛁᛁᚴᛚᛘᚾᚬᛒᚴᚱᛋᛏᚢᚢᚢ ᚴᛋ ᛁᛋ

def runetype():
        a=input('Which rune tpye are you converting? Enter "types" to view possible rune types. ')
        b=a
        if a=='types':
            print('+-----------------------+')
            print('|   Anglo-Saxon Runes   |')
            print('|  Elder Futhark Runes  |')
            print('| Younger Futhark Runes |')
            print('+-----------------------+')
            b=0
def runeconvert():
    data=Input('What would you like to', x, '? ')


while a is None:
    x=input('Decode or Encode? ')
    if x=='Encode':
        while b==0 :
            runetype()     #Encoding runes
    if x=='Decode':
        while b==0 :
            runetype()     #Decoding runes
    if x!='Encode' or x!='Decode':
        print('You must input "Decode" or "Encode"!')
print('All Done!')
