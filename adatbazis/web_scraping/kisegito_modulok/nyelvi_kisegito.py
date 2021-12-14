def ekezetnelkul(szo: str):
    szo =szo.replace("á", "a")
    szo =szo.replace("ű", "u")
    szo =szo.replace("ú", "u")
    szo =szo.replace("ó", "o")
    szo =szo.replace("ö", "o")
    szo =szo.replace("ő", "o")
    szo =szo.replace("é", "e")

    return szo.replace("á", "a")