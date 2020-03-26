from covid import Covid

covid = Covid(source="worldometers")
exist = False

while not exist:
    con = False
    x = input("Input your desired country name \n")
    if x.lower()  in covid.list_countries() :
        s = covid.get_status_by_country_name(x.lower())
        print("Country :" ,s["country"])
        print("Confirmed :" , s["confirmed"])
        print("New cases :",s["new_cases"])
        print("Deaths :",s["deaths"])
        print("Recovered :",s["recovered"])
        print("Active :",s["active"])
        while not con :
            z = input("Do you want to see more countries ? y/n \n")
            if z[0].lower() == "y":

                con = True

            elif z[0].lower()=="n":
                exist = True
                con = True
            else:
                print("Wrong answer please answer with a yes or no")



    else:
        print("invalid country try again \n")

input("Press any key to exit \n")