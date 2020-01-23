##########################################################################
# Encryption
# 
# In the extended ASCII character encoding, each character is associated
# with a number between 0 and 255. For instance, the code of character
# 'A' is 65, the code of character '#' is 35, the code of character '2'
# is 50 etc.
# 
# The function ord in Python returns the code of the character. The
# function chr is the inverse to ord. For example:
# 
#     >>> ord('A')
#     65
#     >>> ord('a')
#     97
#     >>> chr(73)
#     'I'
# 
# It is not a coincidence that the codes of lower-case letters of the
# English alphabet are consecutive numbers:
# 
#     >>> [ord(c) for c in 'abcdefgh']
#     [97, 98, 99, 100, 101, 102, 103, 104]
# 
# The same is true in the case of the upper-case letters:
# 
#     >>> [ord(c) for c in 'ABCDEFGH']
#     [65, 66, 67, 68, 69, 70, 71, 72]
# 
# The English alphabet (in upper-case): 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
# 
# Students of mathematics like to discuss mathematical problems on on-line
# forums such as http://artofproblemsolving.com/community. A student may
# accidentally read a hint on a problem before she attempts to solve it
# herself. Such a spoiler can be very annoying.
#
# Therefore, a moderator on some forum has decided to encrypt all posts
# which contain a hint by using some letter substitution cipher such as
# ROT-13. Because ROT-13 is well-known and widely used, he decided to use
# another cipher which he calls INV-13. By this method, the $i$-th
# character of the alphabet is replaced with the $i$-th character from the
# end of the alphabet while non-alphabetic characters remain untouched. In
# this way the message
#
#     'Use the Pythagorean theorem!'
#
# becomes
#
#     'Fhv gsv Kbgsztlivzm gsvlivn!'
##########################################################################



##########################################################################
# Write a function single_inv13(c) that takes a string c (which will always
# be of length 1, i.e., it will contain a single character). The function
# should encrypt that character using the INV-13 cipher. The case of the
# letters should be preserved (upper-case letters must remain in upper-case).
# 
# Example:
# 
#     >>> single_inv13('A')
#     'Z'
#     >>> single_inv13('b')
#     'y'
#     >>> single_inv13('C')
#     'X'
##########################################################################



##########################################################################
# Write a function inv13(text) which takes a string text. This function
# should return a new string which is obtained from string text by
# encrypting it with the INV-13 cipher.
#
# Example:
# 
#     >>> inv13('Use the Pythagorean theorem!')
#     'Fhv gsv Kbgsztlivzm gsvlivn!'
##########################################################################



##########################################################################
# Write a function inv13_file(input_name, output_name) that takes two
# arguments: the name of the input file and the name of the output file.
# The function should read the text from the input file, encrypt it using
# the INV-13 cipher and write it to the output file.
# 
# If the input file contains the following text:
# 
#     Chuck Norris can create a rock so heavy that
#     even he can't lift it. And then he lifts it anyways,
#     just to show you who the fuck Chuck Norris is.
# 
# then the output file should contain:
# 
#     Xsfxp Mliirh xzm xivzgv z ilxp hl svzeb gszg
#     vevm sv xzm'g orug rg. Zmw gsvm sv orugh rg zmbdzbh,
#     qfhg gl hsld blf dsl gsv ufxp Xsfxp Mliirh rh.
##########################################################################



##########################################################################
# Sometimes the reader of the forum can not solve the problem and needs
# to read a hint. Write a function decrypt_inv13(text) that takes a string
# text which contains the encrypted text (with the INV-13 cipher). The
# function should return the string which contains the decrypted text.
#
# Example:
# 
#     >>> decrypt_inv13('Fhv gsv Kbgsztlivzm gsvlivn!')
#     'Use the Pythagorean theorem!'
##########################################################################


