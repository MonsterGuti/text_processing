key = list(map(int, input().split()))

while True:
    message = input()
    if message == "find":
        break

    decrypted = ""
    key_length = len(key)

    for i in range(len(message)):
        decrypted += chr(ord(message[i]) - key[i % key_length])

    start_treasure = decrypted.index("&") + 1
    end_treasure = decrypted.index("&", start_treasure)
    treasure = decrypted[start_treasure:end_treasure]

    start_coordinates = decrypted.index("<") + 1
    end_coordinates = decrypted.index(">")
    coordinates = decrypted[start_coordinates:end_coordinates]

    print(f"Found {treasure} at {coordinates}")
