##########################################################################
# Encryption 
#
# A substitution cipher is a simple method of encryption by which each letter
# of a given alphabet is replaced by another letter. Such a cipher is
# represented by a dictionary that maps letter to their corresponding
# encrypted letters.
# 
# For instance, dictionary `{'A': 'B', 'C': 'C', 'B': 'D', 'D': 'A'}`
# means that `'A'` is replaced by `'B'`, `'B'` by `'D'`, `'D'` by `'A'`
# and `'C'` remains `'C'`.
##########################################################################

# In all examples that follow the following substitution cipher will be used:
our_cipher = {
    'Y': 'K', 'A': 'O', 'C': 'Z', 'B': 'M',
    'E': 'V', 'D': 'C', 'G': 'P', 'F': 'E',
    'I': 'B', 'H': 'F', 'K': 'I', 'J': 'A',
    'M': 'U', 'L': 'H', 'O': 'R', 'N': 'X',
    'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
    'T': 'Y', 'V': 'N', 'Z': 'Q', 'X': 'S',
    'Q': 'D', 'W': 'W'
}


##########################################################################
# Write a function encrypt(cipher, word) that returns the encryption
# of `word` using `cipher`. Assume that each letter of the `word` is a
# key of the dictionary `cipher`. Example:
# 
#     >>> encrypt(our_cipher, 'PHYSICS')
#     'JFKTBZT'
##########################################################################



##########################################################################
# Write a function is_cipher(dictionary) that determines if `dictionary`
# represents a cipher, i.e., if it is a bijection on some alphabet.
# Example:
# 
#     >>> is_cipher(our_cipher)
#     True
##########################################################################



##########################################################################
# Write a function inverse(cipher) that returns the inverse of a given
# cipher. If the inverse does not exist then the function should return
# `None`. Example:
# 
#     >>> inverse({'A': 'D', 'B': 'A', 'D': 'J', 'J': 'B'})
#     {'A': 'B', 'B': 'J', 'J': 'D', 'D': 'A'}
##########################################################################



##########################################################################
# Write a function decrypt(cipher, word) that takes a cipher and an
# encrypted word and returns the decrypted word. If the dictionary is
# not a bijection (and it is therefore not possible to decrypt the word)
# then the function should return `None`. Example:
# 
#     >>> decrypt(our_cipher, 'JFKTBZT')
#     'PHYSICS'
##########################################################################


