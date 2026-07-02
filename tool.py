import webbrowser

while True:
    command = input("You: ")

    if command == "exit":
        break

    if command.startswith("open "):
        site = command.replace("open ", "")

        if not site.startswith("http"):
            site = "https://" + site + ".com"

        webbrowser.open(site)
        print("Opening", site)