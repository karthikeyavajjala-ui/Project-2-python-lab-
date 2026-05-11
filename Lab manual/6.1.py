with open("output.txt", "a") as file:
    while True:
        text = input("Enter text (type 'exit' to stop): ")
        if text.lower() == "exit":
            break
        file.write(text + "\n")
        print("Data saved")