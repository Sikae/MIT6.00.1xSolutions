from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def get_computer_chosen_word(hand, word_list, n):
    """
    Given a hand and a word_list, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the word_list.

    If no words in the word_list can be made from the hand, return None.

    :param hand: dictionary (string -> int)
    :param word_list: list (string)
    :param n: integer (HAND_SIZE; i.e., hand size required for additional points)

    :returns: string or None
    """
    best_word = ""

    for word in word_list:
        if is_valid_word(word, hand, word_list) and get_word_score(word, n) > get_word_score(best_word, n):
            best_word = word

    return best_word if best_word else None


#
# Problem #7: Computer plays a hand
#
def play_computer_hand(hand, word_list, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    :param hand: dictionary (string -> int)
    :param word_list: list (string)
    :param n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0
    while calculate_hand_len(hand):
        print_current_hand(hand)

        if get_computer_chosen_word(hand, word_list, n) is None:
            break

        computer_word = get_computer_chosen_word(hand, word_list, n)
        score += update_and_print_score(score, computer_word, n)
        hand = update_hand(hand, computer_word)
        print()

    print_total_score(score)


def get_valid_player():
    while True:
        player = input(PLAYER_PROMPT)
        if player == "c" or player == "u":
            return player
        else:
            print(INVALID_COMMAND_MESSAGE)


def perform_play(player, hand, word_list, n):
    if player == "c":
        play_computer_hand(hand, word_list, n)
    else:
        play_hand(hand, word_list, n)


#
# Problem #8: Playing a game
#
#
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    :param word_list: list (string)
    """
    action = get_initial_valid_input()

    while action != "e":
        if action != "n" and action != "r":
            print(INVALID_COMMAND_MESSAGE)
        else:
            if action == "n":
                hand = deal_hand(HAND_SIZE)
            player = get_valid_player()
            perform_play(player, hand, word_list, HAND_SIZE)
            print()

        action = input(PLAY_GAME_PROMPT)


def main():
    word_list = load_words()
    play_game(word_list)

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    main()
