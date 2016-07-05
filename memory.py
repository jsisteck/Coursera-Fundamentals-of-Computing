# implementation of card game - Memory

import simplegui
import random
exposed = []


# helper function to initialize globals
def new_game():
    global full_deck, exposed, state
    
    #create decks for pairing
    deck1 = range(8)
    deck2 = range(8)
    full_deck = deck1 + deck2
    
    #shuffle full deck
    random.shuffle(full_deck)
    
    #hide all cards
    for i in range(len(full_deck)):
        exposed.append('False')
    
    state = 0
    #print full_deck
        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state
    card_select = pos[0]//50
    if exposed[card_select] == 'False':
        exposed[card_select] = 'True'
        if state == 0:
            state = 1
        elif state == 1:
            state = 2
        else:
            state = 1
    print state
    #print card_select
       
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
   
    for card_idx in range(len(full_deck)):
        card_pos = 50 * card_idx
        num_pos = [((card_pos) + 15), 60]
        #for i in range(0,len(full_deck),3):
        #    exposed[i] = 'True'
        if exposed[card_idx] == 'True':
            canvas.draw_text(str(full_deck[card_idx]), num_pos, 36, 'White')
        else:
            canvas.draw_polygon([[card_pos, 0], [(card_pos + 50), 0], [(card_pos + 50), 100], [card_pos, 100]], 1, 'Red', 'Green')
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric