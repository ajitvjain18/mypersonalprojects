for i in range(0,100):
    print(" ")
    from covid import Covid
    print("COVID TRACKER")
    cv= Covid()
    active=cv.get_total_active_cases()
    recovery=cv.get_total_recovered()
    death=cv.get_total_deaths()
    confirmed=cv.get_total_confirmed_cases()
    print("1.Global Count")
    print("2.Active Cases")
    print("3.Confirmed Cases")
    print("4.Recovered Cases")
    print("5.Deceased")
    print("6.Get Covid Updates By Country Name")
    choice=input("ENTER A NUMBER OF YOUR CHOICE: ")
    if choice == '1':
        print("Active Cases: ",active,"\nConfirmed Cases: ",confirmed,"\nRecovered Cases: ",recovery,"\nDeceased Cases: ",death)
    elif choice == '2':
        print("Active Cases: ",active)
    elif choice == '3':
        print("Confirmed Cases: ",confirmed)
    elif choice == '4':
        print("Recovered Cases: ",recovery)
    elif choice == '5':
        print("Deceased Cases: ",death)
    elif choice == '6':
        str=i=input("ENTER COUNTRY NAME: ")
        cname=cv.get_status_by_country_name(i)
        print(cname)
    else:
        print("Invalid Option")

