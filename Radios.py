file='RadioStream.txt'

with open(file,encoding='utf-8-sig')as radio_data:
    radio_stream=radio_data.read()
    

last4=[]
position=0

for letter in radio_stream:
    position+=1
    while letter in last4:
        del last4[0]
    last4.append(letter)
    if len(last4)==14: #equals 4 for first part -- otherwise code is the same
        
        print(f'The sequence of {last4} is the marker, with the message starting after character {position}')
        break
    
        
    