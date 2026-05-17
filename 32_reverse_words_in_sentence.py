sentence = input("Enter a sentence: ")

words = sentence.split()
reversed_sentence = " ".join(reversed(words))

print("Reversed word order:", reversed_sentence)