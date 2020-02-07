def main():
    room_list = []
    room = ['You are in a dark room.\nThere is a passage to the north and a door to the east.',3,1,None,None]
    room_list.append(room)
    
    room = ['You are in a torchlit hallway.\nThere are rooms to the east and west.',None,2,None,0]
    room_list.append(room)
    
    room = ['You are in the dining hall surrounded by empty plates.\nThere is a door to the west.',None,None,None,1]
    room_list.append(room)
    
    room = ['You are in the armory.  Weapons are everywhere.\nThere is a hallway to the east and a door to the south.',None,4,0,None]
    room_list.append(room)
    
    room = ['You are in a large, well lit hallway.\nThere are rooms to the east and west and a balcony to the north.\nA pleasant smell is coming out of the room to the east.',6,5,None,3]
    room_list.append(room)
    
    room = ['You are in the kitchen.  A fresh baked apple pie is on the counter.\nThere is a hallway to the west.',None,None,None,4]
    room_list.append(room)
    
    room = ['You are on the balcony.  There is a 100 ft drop in front of you\nand a hallway to the south.',None,None,4,None]
    room_list.append(room)
    
    current_room = 0
    
    while True:
        print()
        print(room_list[current_room][0])
        direction = input('What direction? ')
        north = ['n','north']
        south = ['s','south']
        east = ['e', 'east']
        west = ['w', 'west']
        quit = ['q', 'quit', 'wake', 'exit']
        
        if direction.lower() in north:
            next_room = room_list[current_room][1]
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room
        
        elif direction.lower() in east:
            next_room = room_list[current_room][2]
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room
                
        elif direction.lower() in south:
            next_room = room_list[current_room][3]
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room
                
        elif direction.lower() in west:
            next_room = room_list[current_room][4]
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room
        
        elif direction.lower() in quit:
            print("You awake feeling well rested.")
            return
            
        else:
            print("Sorry, I didn't understand you.")
            
    

if __name__ == "__main__":
    main()