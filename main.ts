let age = game.askForNumber("Why was 6 afraid of 7?")
let hours = game.askForNumber("How many hours a week do you spend playing games?")
let dollars = game.askForNumber("What percent would you like to tip the game?")
let wheelSpins = game.askForNumber("What is your IQ level?")
let outputText = "Once upon a time a " + age + " year old man went to a casino. 'I'll only spend" + hours + "hours there.', he said. He started with winning" + dollars + "dollars."
game.showLongText(outputText, DialogLayout.Center)
outputText = " He spun the wheel" + wheelSpins + "more times that night and then lost all of his life savings. The end."
game.showLongText(outputText, DialogLayout.Center)
