"""
https://stackoverflow.com/questions/13650293/understanding-pythons-is-operator

Her tester jeg forskjellen på (is og is not) vs ==
"""
playerOne = {
  'name': 'Jørund',
  'speciality': 'grit',
  'age': 38,
}
shadow = {
  'name': 'Jørund',
  'speciality': 'grit',
  'age': 38,
}
copyCat = playerOne
playerTwo = {
  'name': 'Lori',
  'speciality': 'thorough',
  'age': 36,
}

# print(playerOne == playerTwo)
# print(playerOne == shadow)
# print(playerOne != shadow)
# print(playerOne is not shadow)
# print(playerOne is shadow)
# print(id(playerOne))
# print(id(shadow))
# print (playerOne is copyCat)
print(playerOne['name'])

firstArr = [1,2,3,4]
secondArr = [1,2,3,4]

# print(firstArr is secondArr)

myName = 'Jørund'
yourName = 'Jørund'

# interessant! Strings med samme innhold har samme id
# print(myName == yourName)
# print(myName is yourName) #denne blir lik!
# print(id(myName))
# print(id(yourName))
