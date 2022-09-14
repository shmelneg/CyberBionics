import shortener_func as short


links = {"wikipedia": "https://uk.wikipedia.org",
         "google": "https://www.google.com",
         "netflix": "https://www.netflix.com"
         }

while True:
    print("===================================================================================================")
    menu = input("Choose menu option:\n\t1.Get the link\n\t2.Store your link\n\t0.Exit\n"
                 "Make your choice (input 1, 2, or 0): ")
    print("===================================================================================================")
    if menu == "1":
        short.get_link(links)
    elif menu == "2":
        short.add_link(links)
    elif menu == "0":
        break
    else:
        print("Invalid command. Input 1, 2, or 0")
