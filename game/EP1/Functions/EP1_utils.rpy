label EP1_bitch(amount, place=False):
    $ global bitchmeter_places
    if place != False:
        if bitchmeter_places.has_key(place):
            return
        $ bitchmeter_places[place] = amount


    if bitchmeterValue > maxBitchness / 2 and amount < 0:
        $ amount *= 3
    if bitchmeterValue <= maxBitchness / 2 and amount > 0:
        $ amount *= 3

    $ bitchmeterValue += amount

    if bitchmeterValue >= maxBitchness:
        $ steam_achievement("ach14")
    if bitchmeterValue <= 153:
        $ steam_achievement("ach15")

    if amount > 0:
        show screen notify ("Bitchness increased!")
    else:
        show screen notify ("Bitchness decreased!")
    return
