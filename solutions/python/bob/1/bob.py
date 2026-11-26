def response(hey_bob):
    text = hey_bob.strip()
    if text.isupper() and text.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif text.endswith("?"):
        return "Sure."
    elif text.isupper(): 
        return "Whoa, chill out!"    
    elif text == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."