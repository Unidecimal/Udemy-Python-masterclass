text = """Education is not the learning of facts
but the training of the mind to think

 - Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

splited_quote = set(text.split())
preps_used = splited_quote & prepositions
print(preps_used)