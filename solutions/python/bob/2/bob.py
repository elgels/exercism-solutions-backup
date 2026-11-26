"""Bob, the lackadaisical teenager."""
def response(hey_bob):
    """Return Bob's reply to what someone says to him."""
    text = hey_bob.strip()
    if text.isupper() and text.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if text.endswith("?"):
        return "Sure."
    if text.isupper(): 
        return "Whoa, chill out!"    
    if text == "":
        return "Fine. Be that way!"
    return "Whatever."