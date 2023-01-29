import random



def handle_response(message) -> str:
    user_message = message.lower()
    
    # greetings array ---------
    greetings = ["uwu -o- I live to serve you master oWo", "Haiiii senpai you look cute today ^.^", "v( '.') > ohh master, you make me blush >.<", "Hello Handsome 6.6","Hey there Senapi", "O.O senpai finally noticed me", "wassup :3", ]
    greeting = random.choice(greetings)
    
    if user_message == '#hi':
        return str(greeting)
    # end greetings -------------
    
    # rolling dice --------
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_phrase = ["uwu senpai rolled a: ", "WOW senpai -.-: ", "Look senpai a: ", "Master you rolled a: ", "Master has rolled: "]
    dice_phrases = random.choice(dice_phrase)
    
    
    if user_message == "#roll the dice":
        if dice1 == 1 and dice2 == 1:
            return str(f"SSSENPAII!!!... {dice1} and {dice2} .... Thats SNAKE EYES @.@ owo.")
        return str(f"{dice_phrases} {dice1} and a {dice2}.")
    
    # end rolling dice ----------
    
    if user_message == "!help":
        return "`There is no saving you senpai... youre mine now >;3.`"