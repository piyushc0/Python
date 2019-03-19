customer = {
    "name": "Piyush Choubey",
    "age": 18,
    "is_Verified": True
}
print(customer["name"])  # Case-sensitive

# Exercise
phone = input("Phone: ")
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for x in phone:
    output += numbers.get(x, "!") + " "
print(output)


# Emoji Converter

def emoji_convertor(msg):
    words = msg.split(" ")
    emojis = {
        ":)": "😄",
        ":(": "😡"
    }
    result = ""
    for word in words:
        result += emojis.get(word, word) + " "
    return result


message = input("> ")
print(emoji_convertor(message))
