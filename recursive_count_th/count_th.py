
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# UP

# if word = 'things'
# string = ''
# i = 0
# j = i + 1
# sub_string = 'th'
# base case:
# if length of string is 0: return 0

# initialize counter to 0: counter = 0

# look at each index of the string: if th are in the string call count_th on
# if sub_string not in string[0:1]:
# return count_th(string[i:j])
# elif sub_string in string[0:1]:: increment counter
# else: return 0

def count_th(word):

    sub_string = 'th'

    # base case, the word has to have at least two letters to be able to contain 'th'
    if len(word) < 2:
        return 0

    if sub_string == word[0:2]:
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])


print(count_th('things'))
