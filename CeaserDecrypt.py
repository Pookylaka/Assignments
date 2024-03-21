def ceaserencrypt(text,Step):
  result = ""

  for letter in text:

      if letter.isalpha():

          alphabet = ord(letter) + Step

          if alphabet > ord('z'): # Section referenced from github
              alphabet -= 26      #

          final = chr(alphabet)

      result += final

  return result


text = "tqjzfxfdemcplvespwlhozteezdptkpazhpctylwwzespcnldpdzmdpcgptetnlxptdlhtnzybfpcpotetdmpeepcezncplepeslyezwplcyncpletyrtdesppddpynpzqwtqpldlcfwpxpyhzccjxzcplmzfehsleespjnlyedppeslylmzfehsleespjnlytetdpldtpcezqtyoxpyhszhtwwgzwfyeppcezotpeslyezqtyoeszdphszlcphtwwtyrezpyofcpaltyhtesaletpynp"
Step = 15
print ("Original Text : " + text )
print ("\nShift : " + str(Step))
print ("\nCipher Decrypted : " + ceaserencrypt(text,Step))
