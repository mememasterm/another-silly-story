age = game.ask_for_number("Why was 6 afraid of 7?")
hours = game.ask_for_number("How many hours a week do you spend playing games?")
dollars = game.ask_for_number("What percent would you like to tip the game?")
wheelSpins = game.ask_for_number("What is your IQ level?")
outputText = "Once upon a time a " + age + " year old man went to a casino. \'I\'ll only spend" + hours + "hours there.\', he said. He started with winning" + dollars + "dollars."
game.show_long_text(outputText, DialogLayout.Center)
outputText = " He spun the wheel" + wheelSpins + "more times that night and then lost all of his life savings. The end."
game.show_long_text(outputText, DialogLayout.Center)