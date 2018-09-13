# We download the cards folder online and put them into the same folder as this file.
import random
import tkinter as tk


# Function to load the cards into this program;
def load_card_images(card_images):
	# We will iterate through these names to get all the cards. Each .png file contains one of these words in its name;
	suits = ["heart", "club", "diamond", "spade"]
	face_cards = ["jack", "queen", "king"]

	# For each suit, retrieve the image for the cards;
	for suit in suits:
		# First the number cards 1 to 10;
		for card in range(1, 11):
			name = "./cards/{}_{}.{}".format(str(card), suit, "png")
			image = tk.PhotoImage(file=name)
			card_images.append((card, image))

		# Next the face cards;
		for card in face_cards:
			name = "./cards/{}_{}.{}".format(str(card), suit, "png")
			image = tk.PhotoImage(file=name)
			card_images.append((10, image))
			# The value of 10 is due to the value of all face cards equal to 10 in blackjack;


# Function to show display the next card of the list;
def deal_card(frame):
	# Pop the next card off the top of the deck
	next_card = deck.pop(0)
	# Add the image to a label and display the label
	tk.Label(frame, image=next_card[1], relief="raised").pack(side="left")
	# We use side="left" because we want the cards to appear from left to right as they are displayed;
	# Now return the card's face value;
	return next_card


def score_hand(hand):
	# Calculate the total score of all cards in the list;
	# Only one ace can have the value of 11, and this will reduce to 1 if the hand would bust;
	score = 0
	ace = False
	for next_card in hand:
		card_value = next_card[0]
		if card_value == 1 and not ace:
			ace = True
			card_value = 11
		score += card_value
		# If we would bust, check if there is an ace and subtract 10;
		if score > 21 and ace:
			score -= 10
			ace = False
	return score


# Creating the 2 functions (one for "dealer" and the other for "player") to be assigned for the buttons;
def deal_dealer():
	dealer_hand.append(deal_card(dealer_card_frame))
	dealer_score = score_hand(dealer_hand)
	dealer_score_label.set(dealer_score)
	player_score = score_hand(player_hand)
	if player_score > 21:
		result_text.set("Dealer wins!")
	elif dealer_score > 21 or dealer_score < player_score:
		result_text.set("Player wins!")
	elif dealer_score > player_score:
		result_text.set("Dealer wins!")
	else:
		result_text.set("Draw =(")
	remaining_cards()


def deal_player():
	player_hand.append(deal_card(player_card_frame))
	player_score = score_hand(player_hand)
	player_score_label.set(player_score)
	if player_score > 21:
		result_text.set("Dealer wins!")
	remaining_cards()


# Function to see how many cards are left in the deck;
def remaining_cards():
	print(len(deck))


# Creating the main window;
mainWindow = tk.Tk()
mainWindow.geometry("640x540-330-0")
mainWindow.title("Blackjack")
mainWindow.configure(background="green")

# # A way of checking the values of the "configure()" method.
# for row in mainWindow.configure().items():
# 	print(row)


# Result window; First we create the text, which will change according to the game, then we create the window;
result_text = tk.StringVar()
result_window = tk.Label(mainWindow, textvariable=result_text)
result_window.grid(row=0, column=0, columnspan=3)

# Frame for the game;
game_Frame = tk.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
game_Frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# Score counter and text for the dealer's information;
dealer_score_label = tk.IntVar()
tk.Label(game_Frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tk.Label(game_Frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the dealer's card images;
dealer_card_frame = tk.Frame(game_Frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

# Score counter and text for the player's information;
player_score_label = tk.IntVar()
tk.Label(game_Frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tk.Label(game_Frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the player's card images;
player_card_frame = tk.Frame(game_Frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Button frame;
button_frame = tk.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# Dealer's button;
dealer_button = tk.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

# Player's button;
player_button = tk.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)


def again():
	exec(open("./63-blackjackSetup.py").read())


# Button to start over;
restart_button = tk.Button(button_frame, text="Restart", command=again)
restart_button.grid(row=0, column=2)

# Calling the load_cards_images();
cards = []
load_card_images(cards)
print("The number of pictures loaded into your program is {}".format(len(cards)))

# Create a new deck of cards and shuffle them;
# It is important to create a new list of cards, otherwise the deck will have fewer cards as the other games happen;
deck = list(cards)
random.shuffle(deck)

# Create the list to store the dealer's and player's hands;
dealer_hand = []
player_hand = []


# # SCOPING
# # If your function uses a global variable at the beginning of its definition, but later changed
# # (i.e. global_variable += 1), then python will no longer recognize that new value as global but rather as a new
# # local variable.
# # The next lines of code give an example, but you need to change the code in order to use it.
#
# player_score = 0
# player_ace = False
#
#
# def deal_player():
# 	global player_score
# 	global player_ace
# 	card_value = deal_card(player_card_frame)[0]
# 	if card_value == 1 and not player_ace:
# 		card_value = 11
# 		player_ace = True
# 	player_score += card_value
# 	# If we would bust, check if there's an ace and subtract;
# 	if player_score > 21 and player_ace:
# 		player_score -= 10
# 		player_ace = False
# 	player_score_label.set(player_score)
# 	if player_score > 21:
# 		result_text.set("Dealer Wins!")
# 	remaining_cards()

mainWindow.mainloop()