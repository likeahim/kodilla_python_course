print("Greetings from file")

def shopping(items, payment='card', shop='local'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupuję następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić używam %s." % payment
    return result

items = ["cola", "ser", "wykałaczki"]
text = shopping(items, 'card', 'small local shop')
print(text)

print("Pokażę wszystko, co wpiszesz!")
text = input("wpisz wypociny:\n")
print("Oto Twój tekst: ***%s***" % text)