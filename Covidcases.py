from covid.api import CovId19Data

api = CovId19Data(force=True)
exist = False

while not exist:
    con = False
    q = input("Do you want to see a list of all the countries and use the ID for the search (Or type in country name manually)? y/n \n")
    if q[0].lower() =="y":
        for x,i in enumerate(api.show_available_countries()):
            print(x,i)
        z = int(input("Select the corresponding country code to continue \n"))
        c = api.show_available_countries()[z]
        s = api.filter_by_country(c)
        print("Country :" ,s["label"])
        print("Confirmed :" , s["confirmed"])
        print("Deaths :",s["deaths"])
        print("Recovered :",s["recovered"])
    elif q[0].lower()=="n":
        w = input("Select the country name to display the statistics \n")
        try:
            api.filter_by_country(w.lower())
            e = api.filter_by_country(w.lower())
            print("Country :", e["label"])
            print("Confirmed :", e["confirmed"])
            print("Deaths :", e["deaths"])
            print("Recovered :", e["recovered"])
        except:
            print("Invalid country ,use the country list for reference \n")
    else:
        print("Wrong answer try again please")
    while not con:
        r = input("Do you want to see more countries ? y/n \n")
        if r[0].lower() == "y":

            con = True

        elif r[0].lower() == "n":
            exist = True
            con = True
        else:
            print("Wrong answer please answer with a yes or no \n")



