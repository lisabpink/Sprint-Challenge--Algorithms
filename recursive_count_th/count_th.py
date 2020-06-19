'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# base case
# if length of word < than 2
# return 0

# if 2 letters are "th"
# return 1 + count of words

# if ending of word  = "th"
# return 1


def count_th(word):
    if len(word) < 2:
        return 0
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])


print(count_th("th"))
print(count_th("thth"))
print(count_th("ththth"))
print(count_th("thththth"))
print(count_th("elevator"))
print(count_th("This"))
print(count_th("this"))
print(count_th("throw"))
print(count_th("moth"))
