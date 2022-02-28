# Bank Robbery
positions = input()
positions = positions.split()
positions.sort()
oleg_position = positions[1]
bank_notes = int(input())
notes_position = input()
notes_position = notes_position.split()
notes_position.sort()
notes_collected = 0

if positions.count(oleg_position)<2:
    notes_collected = notes_collected + notes_position.count(oleg_position)

    while True:
        if str(int(oleg_position)+1) not in positions:
            notes_collected = notes_collected + notes_position.count(str(int(oleg_position)+1))
            oleg_position = str(int(oleg_position)+1)
        else:
            break
    oleg_position = positions[1]

    while True:        
        if str(int(oleg_position)-1) not in positions:
            notes_collected = notes_collected + notes_position.count(str(int(oleg_position)-1))
            oleg_position = str(int(oleg_position)-1)
        else:
            break    
    oleg_position = positions[1]
    print(notes_collected)
else:
    print("")