from ps4a import *


#
# Test code
# You don't need to understand how this test code works (but feel free to look it over!)

# To run these tests, simply run this file (open up in IDLE, then run the file as normal)

def test_get_word_score():
    """
    Unit test for getWordScore
    """
    failure = False
    # dictionary of words and scores
    words = {("", 7): 0, ("it", 7): 4, ("was", 7): 18, ("scored", 7): 54, ("waybill", 7): 155, ("outgnaw", 7): 127,
             ("fork", 7): 44, ("fork", 4): 94}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_getWordScore()")
            print("\tExpected", words[(word, n)],
                  "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n))
            failure = True
    if not failure:
        print("SUCCESS: test_get_word_score()")


# end of test_getWordScore


def test_update_hand():
    """
    Unit test for updateHand
    """
    # test 1
    original_hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
    copied_hand = original_hand.copy()
    word = "quail"

    hand2 = update_hand(copied_hand, word)
    expected_hand_1 = {'l': 1, 'm': 1}
    expected_hand_2 = {'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}

    if hand2 != expected_hand_1 and hand2 != expected_hand_2:
        print("FAILURE: test_updateHand('" + word + "', " + str(original_hand) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand_1, "or", expected_hand_2)

        return  # exit function

    if copied_hand != original_hand:
        print("FAILURE: test_updateHand('" + word + "', " + str(original_hand) + ")")
        print("\tOriginal hand was", original_hand)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", copied_hand)

        return  # exit function

    # test 2
    original_hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    copied_hand = original_hand.copy()
    word = "evil"

    hand2 = update_hand(copied_hand, word)
    expected_hand_1 = {'v': 1, 'n': 1, 'l': 1}
    expected_hand_2 = {'e': 0, 'v': 1, 'n': 1, 'i': 0, 'l': 1}
    if hand2 != expected_hand_1 and hand2 != expected_hand_2:
        print("FAILURE: test_updateHand('" + word + "', " + str(original_hand) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand_1, "or", expected_hand_2)

        return  # exit function

    if copied_hand != original_hand:
        print("FAILURE: test_updateHand('" + word + "', " + str(original_hand) + ")")
        print("\tOriginal hand was", original_hand)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", copied_hand)

        return  # exit function

    # test 3
    original_hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    copied_hand = original_hand.copy()
    word = "hello"

    hand2 = update_hand(copied_hand, word)
    expected_hand_1 = {}
    expected_hand_2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expected_hand_1 and hand2 != expected_hand_2:
        print("FAILURE: test_updateHand('" + word + "', " + str(original_hand) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand_1, "or", expected_hand_2)

        return  # exit function

    if copied_hand != original_hand:
        print("FAILURE: test_updateHand('" + word + "', " + str(original_hand) + ")")
        print("\tOriginal hand was", original_hand)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", copied_hand)

        return  # exit function

    print("SUCCESS: test_update_hand()")


# end of test_updateHand

def test_is_valid_word(word_list):
    """
    Unit test for isValidWord
    """
    failure = False
    # test 1
    word = "hello"
    original_hand = get_frequency_dict(word)
    copied_hand = original_hand.copy()

    if not is_valid_word(word, copied_hand, word_list):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", original_hand)

        failure = True

    # Test a second time to see if wordList or hand has been modified
    if not is_valid_word(word, copied_hand, word_list):
        print("FAILURE: test_isValidWord()")

        if copied_hand != original_hand:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", original_hand, "but it is", copied_hand)

        else:
            print("\tTesting word", word, "for a second time - have you modified wordList?")
            wordInWL = word in word_list
            print("The word", word, "should be in wordList - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", copied_hand)

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
    word = "rapture"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

        # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
    word = "honey"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

        # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 5
    hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    word = "evil"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 6
    word = "even"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)")

        failure = True

    if not failure:
        print("SUCCESS: test_is_valid_word()")


wordList = load_words()
print("----------------------------------------------------------------------")
print("Testing get_word_score...")
test_get_word_score()
print("----------------------------------------------------------------------")
print("Testing update_hand...")
test_update_hand()
print("----------------------------------------------------------------------")
print("Testing is_valid_word...")
word_list = load_words()
test_is_valid_word(word_list)
print("----------------------------------------------------------------------")
print("All done!")
