from covid.api import CovId19Data

api = CovId19Data(force=True)

exist = False

while not exist:
    con = False
    x = input("Input your desired country name \n")
    if  api.filter_by_country(x.lower())  :
        s = api.filter_by_country(x.lower())
        print("Country :" ,s["label"])
        print("Confirmed :" , s["confirmed"])
        print("Deaths :",s["deaths"])
        print("Recovered :",s["recovered"])
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
