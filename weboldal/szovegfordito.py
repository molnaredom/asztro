def szotar(betuparos):
    # 2 betu
    parosvegbetu = ""
    if betuparos == "sz":  parosvegbetu = "☿"
    elif betuparos == "cs":  parosvegbetu = "♆"
    elif betuparos == "zs":  parosvegbetu = "♆"

    maradekbetu = betuparos[-1]
    if maradekbetu == "¤":
        maradekbetu = "" # utolso betu eseten tortenik

    betu = betuparos[0]
    vegbetu = ""
    # 1 betu
    if betu == "a": vegbetu = "□"
    elif betu == "á": vegbetu = "□"
    elif betu == "b": vegbetu = "♀"
    elif betu == "c": vegbetu = "☾"
    elif betu == "d":  vegbetu = "♃"
    elif betu == "e":  vegbetu = "☍"
    elif betu == "é":  vegbetu = "⚻"  # Quincunx
    elif betu == "f":  vegbetu = "☿"
    elif betu == "g":  vegbetu = "☿"
    elif betu == "h":  vegbetu = "☾"
    elif betu == "i":  vegbetu = "△"
    elif betu == "í":  vegbetu = "△"
    elif betu == "j":  vegbetu = "☉"
    elif betu == "k":  vegbetu = "☿"
    elif betu == "l":  vegbetu = "☉"
    elif betu == "m":  vegbetu = "☽"
    elif betu == "n":  vegbetu = "☽"
    elif betu == "o":  vegbetu = "☌"
    elif betu == "ó":  vegbetu = "⚺"  # Semisextile
    elif betu == "ö":  vegbetu = "☌"
    elif betu == "ő":  vegbetu = "⚺"  # Semisextile
    elif betu == "p":  vegbetu = "♇"
    elif betu == "r":  vegbetu = "♂"
    elif betu == "s":  vegbetu = "♂"
    elif betu == "t":  vegbetu = "♄"
    elif betu == "u":  vegbetu = "⚹"
    elif betu == "ú":  vegbetu = "⚺"  # Semisextile
    elif betu == "ü":  vegbetu = "⚹"
    elif betu == "ű":  vegbetu = "⚺"  # Semisextile
    elif betu == "v":  vegbetu = "♂"
    elif betu == "z":  vegbetu = "♂"
    elif betu == "q":  vegbetu = "?"
    elif betu == "x":  vegbetu = "☽"
    elif betu == "y":  vegbetu = "♀"
    elif betu == "w":  vegbetu = "♇"

    if parosvegbetu != "":
        return parosvegbetu
    elif vegbetu == "":
        return f"{betu}{maradekbetu}"
    else:
        return f"{vegbetu}{maradekbetu}"


szo = "sziasztok adam vagyok nem kell valakinek egy kis tejberízs"
print(szo)
vizsgalt_betu = 2
forditottszo = szotar(f"{szo[0]}{szo[1]}")
# merkur A
# print(forditottszo)
while True:
    forditottszo += szo[vizsgalt_betu]
    forditottszo = forditottszo[:-2] + szotar(f"{forditottszo[-2]}{forditottszo[-1]}")
    # print(forditottszo)
    vizsgalt_betu += 1

    if len(szo) == vizsgalt_betu:
        forditottszo = forditottszo[:-1] + szotar(f"{forditottszo[-1]}¤")
        break

print(forditottszo)

