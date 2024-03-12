def main_menu():
    ussd_code = input("Enter your USSD code: ")
    if ussd_code == "*301#":
        print(" ")
        select_transaction()
    else:
        print("Invalid USSD code. Try again")
        main_menu()


def exit_menu():
    print("Exiting, thank you")


def invalid():
    print("Invalid Selection. Try again")


def airtime_value():
    airtime = input("Enter your airtime value: ")
    if airtime.isdigit() and float(airtime) >= 0:
        return float(airtime)
    else:
        print("Invalid input. Please enter a positive number.")
        return airtime_value()


def insufficient_balance():
    print(
        "SORRY! Insufficient credit balance for the plan you want to buy.Please"
        "recharge"
        "your"
        "line or you can simply Borrow Data. To Borrow Data now, just dial "
        "*303#")


def print_subscription(plan):
    print(f"You have subscribed for {plan['data']} of data at N{plan['amount']}.")
    print(f"Validity: {plan['validity']}. Night data: {plan['nite_data']}")


def buy_data_options():
    renew = input(
        "1. Proceed (Auto-Renew)\n"
        "2. Proceed (One-off)\n"
        "99. Back\n"
        "0. Exit\n"
    )
    if renew == "1" or renew == "2":
        auto_buy_data()
    elif renew == "99":
        select_transaction()
    elif renew == "0":
        exit_menu()
    else:
        invalid()
        buy_data_options()


def mini_plans():
    mini_plans1 = {
        "1": {"data": "150MB", "amount": 100, "validity": "1 Day", "nite_data": "35MB"},
        "2": {"data": "350MB", "amount": 200, "validity": "2 Days", "nite_data": "110MB"},
        "3": {"data": "1.8GB", "amount": 500, "validity": "14 Days", "nite_data": "1GB"},
        "4": {"data": "50MB", "amount": 50, "validity": "1 Day", "nite_data": "5MB"}
    }

    mini_plan_selection = input("1. N100 = 150MB 1 Day incl 35MB nite\n"
                                "2. N200 = 350MB 2 Days incl 110MB nite\n"
                                "3. N500 = 1.8GB 14 Days incl 1 GB nite\n"
                                "4. N50 = 50MB 1 Day incl 5MB nite\n"
                                "5. More Plans\n"
                                "99. Back\n"
                                "0. Exit\n")

    if mini_plan_selection in mini_plans1:
        airtime = airtime_value()
        if airtime >= mini_plans1[mini_plan_selection]["amount"]:
            print_subscription(mini_plans1[mini_plan_selection])
        else:
            insufficient_balance()
            mini_plans()
    elif mini_plan_selection == "5":
        more_plans()
    elif mini_plan_selection == "99":
        # Go back
        return
    elif mini_plan_selection == "0":
        exit()
    else:
        invalid()
        mini_plans()


def more_plans():
    more_plans1 = {
        "1": {"data": "3900MB", "amount": 1000, "validity": "30 Day", "nite_data": "2000MB"},
        "2": {"data": "7500MB", "amount": 1500, "validity": "30 Days", "nite_data": "4000MB"},
        "3": {"data": "9200GB", "amount": 2000, "validity": "30 Days", "nite_data": "4000MB"},
        "4": {"data": "10800MB", "amount": 2550, "validity": "30 Day", "nite_data": "4000MB"}
    }
    more_plans_selection1 = input("1. N1000 = 3.9GB 30 Days incl 2GB nite\n"
                                  "2. N1500 = 7.5GB 30 Days incl 4GB nite\n"
                                  "3. N2000 = 9.2GB 30 Days incl 4GB nite\n"
                                  "4. N2500 = 10.8GB 30 Days incl 4GB nite\n"
                                  "5. More Plans\n"
                                  "99. Back\n"
                                  "0. Exit\n"
                                  )
    if more_plans_selection1 in more_plans1:
        airtime = airtime_value()
        if airtime >= more_plans1[more_plans_selection1]["amount"]:
            print_subscription(more_plans1[more_plans_selection1])
        else:
            insufficient_balance()
            mini_plans()
    elif more_plans_selection1 == "5":
        more_plans2()
    elif more_plans_selection1 == "99":
        # Go back
        more_plans()
    elif more_plans_selection1 == "0":
        exit()
    else:
        invalid()
        mini_plans()


def more_plans2():
    more_plans2 = {
        "1": {"data": "14000MB", "amount": 3000, "validity": "30 Day", "nite_data": "4000MB"},
        "2": {"data": "18000MB", "amount": 4000, "validity": "30 Days", "nite_data": "4000MB"},
        "3": {"data": "24000GB", "amount": 5000, "validity": "30 Days", "nite_data": "4000MB"},
        "4": {"data": "29500MB", "amount": 8000, "validity": "30 Day", "nite_data": "4000MB"}
    }
    more_plans_selection2 = input("1. N3000 = 14GB 30 Days incl 4GB nite\n"
                                  "2. N4000 = 18GB 30 Days incl 4GB nite\n"
                                  "3. N5000 = 24GB 30 Days incl 4GB nite\n"
                                  "4. N8000 = 29.5GB 30 Days incl 4GB nite\n"
                                  "5. More Plans\n"
                                  "99. Back\n"
                                  "0.Exit\n"
                                  )
    if more_plans_selection2 in more_plans2:
        airtime = airtime_value()
        if airtime >= more_plans2[more_plans_selection2]["amount"]:
            print_subscription(more_plans2[more_plans_selection2])
        else:
            insufficient_balance()
            mini_plans()
    elif more_plans_selection2 == "5":
        more_plans3()
    elif more_plans_selection2 == "99":
        # Go back
        more_plans()
    elif more_plans_selection2 == "0":
        exit()
    else:
        invalid()
        mini_plans()


def more_plans3():
    more_plans3 = {
        "1": {"data": "50000MB", "amount": 10000, "validity": "30 Day", "nite_data": "4000MB"},
        "2": {"data": "95000MB", "amount": 15000, "validity": "30 Days", "nite_data": "7000MB"},
        "3": {"data": "119000GB", "amount": 18000, "validity": "30 Days", "nite_data": "10000MB"},
        "4": {"data": "138000MB", "amount": 20000, "validity": "30 Day", "nite_data": "12000MB"}
    }
    more_plans_selection3 = input("1. N10000 = 50GB 30 Days incl 4GB nite\n"
                                  "2. N15000 = 93GB 30 Days incl 7GB nite\n"
                                  "3. N18000 = 119GB 30 Days incl 10GB nite\n"
                                  "4. N20000 = 138GB 30 Days incl 12GB nite\n"
                                  "5. More Plans\n"
                                  "99. Back\n"
                                  "0. Exit\n")
    if more_plans_selection3 in more_plans3:
        airtime = airtime_value()
        if airtime >= more_plans3[more_plans_selection3]["amount"]:
            print_subscription(more_plans3[more_plans_selection3])
        else:
            insufficient_balance()
            mini_plans()
    elif more_plans_selection3 == "5":
        more_plans4()
    elif more_plans_selection3 == "99":
        # Go back
        more_plans()
    elif more_plans_selection3 == "0":
        exit()
    else:
        invalid()
        mini_plans()


def more_plans4():
    more_plans4 = {
        "1": {"data": "225000MB", "amount": 30000, "validity": "30 Days", "nite_data": "4000MB"},
        "2": {"data": "300000MB", "amount": 36000, "validity": "30 Days", "nite_data": "4000MB"},
        "3": {"data": "4250000GB", "amount": 50000, "validity": "90 Days", "nite_data": "4000MB"},
        "4": {"data": "5250000MB", "amount": 60000, "validity": "120 Days", "nite_data": "4000MB"},
        "5": {"data": "6750000MB", "amount": 75000, "validity": "120 Days", "nite_data": "4000MB"}
    }
    more_plans_selection4 = input("1. N30000=225GB for 30 Days\n"
                                  "2. N36000=300GB for 30 Days\n"
                                  "3. N50000=425GB for 90 Days\n"
                                  "4. N60000=525GB for 120 Days\n"
                                  "5. N75000=675GB for 120 Days\n"
                                  "99. Back\n"
                                  "O. Exit\n"
                                  "88. Next\n")
    if more_plans_selection4 in more_plans4:
        airtime = airtime_value()
        if airtime >= more_plans4[more_plans_selection4]["amount"]:
            print_subscription(more_plans4[more_plans_selection4])
        else:
            insufficient_balance()
            mini_plans()
    elif more_plans_selection4 == "99":
        # Go back
        more_plans()
    elif more_plans_selection4 == "0":
        exit()
    else:
        invalid()
        more_plans()


def monthly_plans():
    monthly_plans1 = {
        "1": {"data": "3900MB", "amount": 1000, "validity": "30 Day", "nite_data": "2000MB"},
        "2": {"data": "7500MB", "amount": 1500, "validity": "30 Days", "nite_data": "4000MB"},
        "3": {"data": "9200GB", "amount": 2000, "validity": "30 Days", "nite_data": "4000MB"},
        "4": {"data": "10800MB", "amount": 2550, "validity": "30 Day", "nite_data": "4000MB"}
    }
    monthly_plans_selection1 = input("1. N1000 = 3.9GB 30 Days incl 2GB nite\n"
                                     "2. N1500 = 7.5GB 30 Days incl 4GB nite\n"
                                     "3. N2000 = 9.2GB 30 Days incl 4GB nite\n"
                                     "4. N2500 = 10.8GB 30 Days incl 4GB nite\n"
                                     "5. More Plans\n"
                                     "99. Back\n"
                                     "0. Exit\n"
                                     )
    if monthly_plans_selection1 in monthly_plans1:
        airtime = airtime_value()
        if airtime >= monthly_plans1[monthly_plans_selection1]["amount"]:
            print_subscription(monthly_plans1[monthly_plans_selection1])
        else:
            insufficient_balance()
            monthly_plans()
    elif monthly_plans_selection1 == "5":
        monthly_plans2()
    elif monthly_plans_selection1 == "99":
        # Go back
        monthly_plans()
    elif monthly_plans_selection1 == "0":
        exit()
    else:
        invalid()
        monthly_plans()


def monthly_plans2():
    monthly_plans2 = {
        "1": {"data": "14000MB", "amount": 3000, "validity": "30 Day", "nite_data": "4000MB"},
        "2": {"data": "18000MB", "amount": 4000, "validity": "30 Days", "nite_data": "4000MB"},
        "3": {"data": "24000GB", "amount": 5000, "validity": "30 Days", "nite_data": "4000MB"},
        "4": {"data": "29500MB", "amount": 8000, "validity": "30 Day", "nite_data": "4000MB"}
    }
    monthly_plans_selection2 = input("1. N3000 = 14GB 30 Days incl 4GB nite\n"
                                     "2. N4000 = 18GB 30 Days incl 4GB nite\n"
                                     "3. N5000 = 24GB 30 Days incl 4GB nite\n"
                                     "4. N8000 = 29.5GB 30 Days incl 4GB nite\n"
                                     "5. More Plans\n"
                                     "99. Back\n"
                                     "0.Exit\n"
                                     )
    if monthly_plans_selection2 in monthly_plans2:
        airtime = airtime_value()
        if airtime >= monthly_plans2[monthly_plans_selection2]["amount"]:
            print_subscription(monthly_plans2[monthly_plans_selection2])
        else:
            insufficient_balance()
            mini_plans()
    elif monthly_plans_selection2 == "5":
        monthly_plans3()
    elif monthly_plans_selection2 == "99":
        # Go back
        monthly_plans()
    elif monthly_plans_selection2 == "0":
        exit()
    else:
        invalid()
        monthly_plans()


def monthly_plans3():
    monthly_plans3 = {
        "1": {"data": "50000MB", "amount": 10000, "validity": "30 Day", "nite_data": "4000MB"},
        "2": {"data": "95000MB", "amount": 15000, "validity": "30 Days", "nite_data": "7000MB"},
        "3": {"data": "119000GB", "amount": 18000, "validity": "30 Days", "nite_data": "10000MB"},
        "4": {"data": "138000MB", "amount": 20000, "validity": "30 Day", "nite_data": "12000MB"}
    }
    monthly_plans_selection3 = input("1. N10000 = 50GB 30 Days incl 4GB nite\n"
                                     "2. N15000 = 93GB 30 Days incl 7GB nite\n"
                                     "3. N18000 = 119GB 30 Days incl 10GB nite\n"
                                     "4. N20000 = 138GB 30 Days incl 12GB nite\n"
                                     "5. More Plans\n"
                                     "99. Back\n"
                                     "0. Exit\n")
    if monthly_plans_selection3 in monthly_plans3:
        airtime = airtime_value()
        if airtime >= monthly_plans3[monthly_plans_selection3]["amount"]:
            print_subscription(monthly_plans3[monthly_plans_selection3])
        else:
            insufficient_balance()
            monthly_plans()
    elif monthly_plans_selection3 == "5":
        monthly_plans4()
    elif monthly_plans_selection3 == "99":
        # Go back
        monthly_plans()
    elif monthly_plans_selection3 == "0":
        exit()
    else:
        invalid()
        monthly_plans()


def monthly_plans4():
    monthly_plans4 = {
        "1": {"data": "225000MB", "amount": 30000, "validity": "30 Days", "nite_data": "4000MB"},
        "2": {"data": "300000MB", "amount": 36000, "validity": "30 Days", "nite_data": "4000MB"},
        "3": {"data": "4250000GB", "amount": 50000, "validity": "90 Days", "nite_data": "4000MB"},
        "4": {"data": "5250000MB", "amount": 60000, "validity": "120 Days", "nite_data": "4000MB"},
        "5": {"data": "6750000MB", "amount": 75000, "validity": "120 Days", "nite_data": "4000MB"}
    }
    monthly_plans_selection4 = input("1. N30000=225GB for 30 Days\n"
                                     "2. N36000=300GB for 30 Days\n"
                                     "3. N50000=425GB for 90 Days\n"
                                     "4. N60000=525GB for 120 Days\n"
                                     "5. N75000=675GB for 120 Days\n"
                                     "99. Back\n"
                                     "O. Exit\n"
                                     "88. Next\n")
    if monthly_plans_selection4 in monthly_plans4:
        airtime = airtime_value()
        if airtime >= monthly_plans4[monthly_plans_selection4]["amount"]:
            print_subscription(monthly_plans4[monthly_plans_selection4])
        else:
            insufficient_balance()
            monthly_plans()

    elif monthly_plans_selection4 == "99":
        # Go back
        monthly_plans()
    elif monthly_plans_selection4 == "0":
        exit()
    else:
        invalid()
        monthly_plans()


def mega_plans():
    mega_plans1 = {
        "1": {"data": "225000MB", "amount": 30000, "validity": "30 Days", "nite_data": "4000MB"},
        "2": {"data": "300000MB", "amount": 36000, "validity": "30 Days", "nite_data": "4000MB"},
        "3": {"data": "4250000GB", "amount": 50000, "validity": "90 Days", "nite_data": "4000MB"},
        "4": {"data": "5250000MB", "amount": 60000, "validity": "120 Days", "nite_data": "4000MB"},
        "5": {"data": "6750000MB", "amount": 75000, "validity": "120 Days", "nite_data": "4000MB"}
    }
    mega_plans_selection = input("1. N10000=50GB 30 Days incl 4GB nite\n"
                                 "2. N15000=93GB 30 Days incl 7GB nite\n"
                                 "3. N18000=119GB 30 Days incl 10GB nite\n"
                                 "4. N20000=138GB 30 Days incl 12GB nite\n"
                                 "5. More Plans\n"
                                 "99.Back\n"
                                 "0. Exit\n")

    if mega_plans_selection in mega_plans1:
        airtime = airtime_value()
        if airtime >= mega_plans1[mega_plans_selection]["amount"]:
            print_subscription(mega_plans1[mega_plans_selection])
        else:
            insufficient_balance()
            mega_plans()
    elif mega_plans_selection == "5":
        mega_plan1()
    elif mega_plans_selection == "99":
        # Go back
        mega_plans()
    elif mega_plans_selection == "0":
        exit()
    else:
        invalid()
        mega_plans()


def mega_plan1():
    mega_plans2 = {
        "1": {"data": "50000MB", "amount": 10000, "validity": "30 Days", "nite_data": "4000MB"},
        "2": {"data": "930000MB", "amount": 15000, "validity": "30 Days", "nite_data": "7000MB"},
        "3": {"data": "119000GB", "amount": 18000, "validity": "90 Days", "nite_data": "10000MB"},
        "4": {"data": "138000MB", "amount": 20000, "validity": "120 Days", "nite_data": "12000MB"},

    }
    mega_plans_selection2 = input("1. N10000=50GB 30 Days incl 4GB nite\n"
                                  "2. N15000=93GB 30 Days incl 7GB nite\n"
                                  "3. N18000=119GB 30 Days incl 10GB nite\n"
                                  "4. N20000=138GB 30 Days incl 12GB nite\n"
                                  "5. More Plans\n"
                                  "99.Back\n"
                                  "0. Exit\n")

    if mega_plans_selection2 in mega_plans2:
        airtime = airtime_value()
        if airtime >= mega_plans2[mega_plans_selection2]["amount"]:
            print_subscription(mega_plans2[mega_plans_selection2])
        else:
            insufficient_balance()
            mega_plans()
    elif mega_plans_selection2 == "5":
        mega_plan2()
    elif mega_plans_selection2 == "99":
        # Go back
        mega_plans()
    elif mega_plans_selection2 == "0":
        exit()
    else:
        invalid()
        mega_plans()


def mega_plan2():
    mega_plans3 = {
        "1": {"data": "225000MB", "amount": 30000, "validity": "30 Days", "nite_data": "4000MB"},
        "2": {"data": "300000MB", "amount": 36000, "validity": "30 Days", "nite_data": "7000MB"},
        "3": {"data": "425000GB", "amount": 50000, "validity": "90 Days", "nite_data": "10000MB"},
        "4": {"data": "525000MB", "amount": 60000, "validity": "120 Days", "nite_data": "12000MB"},
        "5": {"data": "675000MB", "amount": 750000, "validity": "120 Days", "nite_data": "12000MB"},

    }
    mega_plans_selection3 = input("1.N30000=225GB for 30 Days\n"
                                  "  2.N36000=300GB for 30 Days\n"
                                  " 3.N50000=425GB for 90 Days\n"
                                  " 4.N60000=525GB for 120 Days\n"
                                  " 5.N75000=675GB for 120 Days\n"
                                  " 99.Back\n"
                                  " O.Exit\n"
                                  " 88.Next\n")

    if mega_plans_selection3 in mega_plans3:
        airtime = airtime_value()
        if airtime >= mega_plans3[mega_plans_selection3]["amount"]:
            print_subscription(mega_plans3[mega_plans_selection3])
        else:
            insufficient_balance()
            mega_plans()
    elif mega_plans_selection3 == "88":
        pass
        # next_mega_plan()
    elif mega_plans_selection3 == "99":
        # Go back
        mega_plans()
    elif mega_plans_selection3 == "0":
        exit()
    else:
        invalid()
        mega_plans()


def super_mega_plan():
    super_mega_plans = {
        "1": {"data": "225000MB", "amount": 30000, "validity": "30 Days", "nite_data": "4000MB"},
        "2": {"data": "300000MB", "amount": 36000, "validity": "30 Days", "nite_data": "7000MB"},
        "3": {"data": "425000GB", "amount": 50000, "validity": "90 Days", "nite_data": "10000MB"},
        "4": {"data": "525000MB", "amount": 60000, "validity": "120 Days", "nite_data": "12000MB"},
        "5": {"data": "675000MB", "amount": 750000, "validity": "120 Days", "nite_data": "12000MB"},

    }
    super_plan_selection = input(" 1.N30000=225GB for 30 Days\n"
                                 " 2.N36000=300GB for 30 Days\n"
                                 " 3.N50000=425GB for 90 Days\n"
                                 " 4.N60000=525GB for 120 Days\n"
                                 " 5.N75000=675GB for 120 Days\n"
                                 " 99.Back\n"
                                 " O.Exit\n"
                                 " 88.Next\n")

    if super_plan_selection in super_mega_plans:
        airtime = airtime_value()
        if airtime >= super_mega_plans[super_plan_selection]["amount"]:
            print_subscription(super_mega_plans[super_plan_selection])
        else:
            insufficient_balance()
            super_mega_plan()
    elif super_plan_selection == "88":
        pass
        # next_mega_plan()
    elif super_plan_selection == "99":
        # Go back
        super_mega_plan()
    elif super_plan_selection == "0":
        exit()
    else:
        invalid()
        super_mega_plan()


def special_data_offer():
    special_data = input("1.Special Plans\n"
                         " 2. Campus Booster\n"
                         "3. Badagry Plans\n"
                         "   4. Data Booster\n"
                         "   5. Betting Agent Plan\n"
                         "  99.Back\n"
                         "  0. Exit\n")
    if special_data == "1":
        pass
    elif special_data == "2":
        pass
    elif special_data == "3":
        pass
    elif special_data == "4":
        pass
    elif special_data == "5":
        pass
    elif special_data == "99":
        special_data_offer()
    elif special_data == "0":
        exit_menu()
    else:
        invalid()
        special_data_offer()


def social_bundle():
    social_bundles = input("1.WTF (WhatsApp, Twitter and Facebook) Bundles\n"
                           "2. YouTube Bundles\n"
                           "3. Opera Bundles\n"
                           "4. Single Bundles\n"
                           "99. Back\n"
                           "0. Exit\n")
    if social_bundles == "1":
        pass
    elif social_bundles == "2":
        pass
    elif social_bundles == "3":
        pass
    elif social_bundles == "4":
        pass
    elif social_bundles == "99":
        social_bundle()
    elif social_bundles == "0":
        exit_menu()
    else:
        invalid()
        social_bundle()


def print_night(plan):
    print(f"You have subscribed for {plan['data']} of data at N{plan['amount']}.")
    print(f"Validity: {plan['validity']}. Duration: {plan['duration']}")


def night_plan():
    night_plans = input("1. N25= 250MB 1Day (12am-05am)\n"
                        "2. N50= 500MB 1Day (12am-05am)\n"
                        "3. N100= 1GB 5Days (12am-05am)\n"
                        "4. N200= 1.25GB 1Day SUN\n"
                        "5. N500= 3GB 2Days SAT-SUN\n"
                        "99. Back\n"
                        "0. Exit\n"
                        )
    night_plan_selection = {
        "1": {"amount": 25, "data": "250MB", "validity": "1Day", "duration": "12am-05am"},
        "2": {"amount": 50, "data": "500MB", "validity": "1Day", "duration": "12am-05am"},
        "3": {"amount": 100, "data": "1GB", "validity": "5Days", "duration": "12am-05am"},
        "4": {"amount": 200, "data": "1.25GB", "validity": "1Day", "duration": "SUN"},
        "5": {"amount": 500, "data": "3GB", "validity": "2Days", "duration": "SAT-SUN"}
    }

    if night_plans in night_plan_selection:
        airtime = airtime_value()
        if airtime >= night_plan_selection[night_plans]["amount"]:
            print_night(night_plan_selection[night_plans])
        else:
            insufficient_balance()
            night_plan()
    elif night_plans == "99":
        night_plan()
    elif night_plans == "0":
        exit_menu()
    else:
        invalid()
        night_plan()


def print_glotv(plan):
    print(f"You have subscribed for {plan['data']} of data at N{plan['amount']}.")
    print(f"Validity: {plan['validity']}.")


def glotv_plans():
    glo_tv = input("1.N150=VOD 500 MB 3 Days\n"
                   "2. N150=VOD 2GB 7 Days\n"
                   "3.N1,400= VOD 6GB 30 Days\n"
                   "4. N900= VOD + TV 2GB 7 Days\n"
                   "5. N3,200= VOD + TV 6GB 30 Days\n"
                   "99. Back\n"
                   "0. Exit\n")
    glo_tv_selection = {
        "1": {"data": "VOD 500MB", "amount": 150, "validity": "3 Days"},
        "2": {"data": "VOD 2GB", "amount": 150, "validity": "7 Days"},
        "3": {"data": "VOD 6GB", "amount": 1400, "validity": "30 Days"},
        "4": {"data": "VOD + TV 2GB", "amount": 900, "validity": "7 Days"},
        "5": {"data": "VOD + TV 6GB", "amount": 3200, "validity": "30 Days"}

    }
    if glo_tv in glo_tv_selection:
        airtime = airtime_value()
        if airtime >= glo_tv_selection[glo_tv]["amount"]:
            print_glotv(glo_tv_selection[glo_tv])
        else:
            insufficient_balance()
            glotv_plans()
    elif glo_tv == "99":
        glotv_plans()
    else:
        invalid()
        glotv_plans()


def auto_buy_data():
    auto_buy_data1 = input("1. Mini Plans\n" +
                           "2. Monthly Plans\n" +
                           "3. Mega Plans\n" +
                           "4. Super Mega Plans\n" +
                           "5. Special Data Offer\n" +
                           "6. Social Bundles\n" +
                           "7. Night and weekend plans\n" +
                           "8. GLOTV Plans\n" +
                           "99. Back\n" +
                           "0. Exit\n"
                           )

    if auto_buy_data1 == "1":
        mini_plans()
    elif auto_buy_data1 == "2":
        monthly_plans()
    elif auto_buy_data1 == "3":
        mega_plans()
    elif auto_buy_data1 == "4":
        super_mega_plan()
    elif auto_buy_data1 == "5":
        special_data_offer()
    elif auto_buy_data1 == "6":

        social_bundle()
    elif auto_buy_data1 == "7":
        night_plan()
    elif auto_buy_data1 == "8":
        glotv_plans()
    elif auto_buy_data1 == "99":
        buy_data_options()
    elif auto_buy_data1 == "0":
        exit_menu()
    else:
        invalid()
        auto_buy_data()


def data_plans():
    data_plans1 = input("1. Buy Data\n" +
                        "2. Gift Data\n" +
                        "3. Share Data\n" +
                        "4. Check Data Bal\n" +
                        "5. Voice/ Data Roaming Offers\n" +
                        "6. Glo Rewards - Cash token\n"
                        "0. Exit\n"
                        )
    if data_plans1 == "1":
        buy_data_options()
    elif data_plans1 == "2":
        pass
        # gift_data_options()
    elif data_plans1 == "3":
        pass
        # share_data_options()
    elif data_plans1 == "4":
        pass
        # check_data_options()
    elif data_plans1 == "5":
        pass
        # voice_roaming_options()
    elif data_plans1 == "6":
        pass
        # glo_reward_options()
    elif data_plans1 == "0":
        exit_menu()
    else:
        invalid()
        data_plans()


def cash_tokens():
    cash_token = input("Recharge and win assured cashback, exciting prizes and chance to win up to N100M "
                       "every week:\n" +
                       "1. Opt-in\n" +
                       "2. Opt-out\n" +
                       "99. Back\n" +
                       "0. Exit \n"
                       )

    if cash_token == "1":
        print("Dear Customer, You have successfully opted-in for Promo. Keep Recharging, win assured cashback, "
              "exciting prizes up to N100MnEvery week.")
    elif cash_token == "2":
        print("Dear Customer, Thank you for your patronage. You can opt-in again by  dialing *301*8# anytime "
              "during promo period and start inning gain.")
    elif cash_token == "99":
        cash_tokens()
    elif cash_token == "0":
        exit_menu()
    else:
        invalid()
        cash_tokens()


def data_balance_options():
    data_value = float(input("What is your data balance: "))
    if data_value >= 0:
        print(f"You are on Berekete, expires 05/03/2024 00:02, Your data balance is {data_value} MB and browsed "
              f"for 0 min")
    else:
        print(
            "Dear Customer, your plan has expired, and you do not have a data plan. To buy a data plan and continue"
            "browsing visit https://hsi.glo.com or dial *312#")


def check_balance_options():
    check_balance = input("1. Main A/C Balance\n" +
                          "2. Bonus A/C Balance\n" +
                          "3. Post Paid A/C Balance: Dial *310#\n" +
                          "99. Back\n" +
                          "0. Exit\n"
                          )
    airtime = airtime_value()
    if check_balance == "1":
        print(f"Main bal is {airtime}.")
    elif check_balance == "2":
        print("This service is not available. Please try again later")
    elif check_balance == "3":
        print("This service is not available. Please try again later")
    elif check_balance == "99":
        check_balance_options()
    elif check_balance == "0":
        exit_menu()

    else:
        invalid()
        check_balance_options()


def recharge_options():
    recharge = input("Dear Customer, as per NCC directive, the airtime recharge code is now 311.\n" +
                     "To recharge dial *311*RechargePin#.\n" +
                     "Thanks\n" +
                     "99. Back\n" +
                     "0. Exit\n"
                     )
    if recharge == "99":
        recharge_options()
    elif recharge == "0":
        exit_menu()
    else:
        invalid()
        recharge_options()


data_share_no = []


def data_share_options():
    while True:
        data_share = input("1. Share Data\n" +
                           "2. Unshare Data\n" +
                           "3. List of Shared Numbers\n" +
                           "4. Get Data Settings\n" +
                           "5. Manual Configuration Details\n" +
                           "6. Easy Share (Credit Share)\n"
                           "0. Exit"
                           )

        if data_share == "1":

            tel_number_share = input("Please enter Glo subscriber number, you want to share data with: ")
            if tel_number_share.isnumeric() and len(tel_number_share) == 11:

                # print(tel_number_share, "has been added")
                data_share_no.append(tel_number_share)
                # print(data_share_no, "added to the list")
                print(f"You have successfully shared your plan with"
                      f" {tel_number_share}.You can also GIFT a data"
                      "plan. To gift a data plan, visit hsi.glo.com or"
                      "simply dial *312#")
            else:
                print("Sorry, you are adding/removing an invalid Globacom user.")
            data_share_options()
        elif data_share == "2":

            tel_unshare = input("Please enter Glo subscriber number, you want to unshare data with: ")
            if tel_unshare in data_share_no:

                data_share_no.remove(tel_unshare)

                print(f"You have successfully removed"

                      f" {tel_unshare} from sharing your plan subscription")

            else:
                print("Number not on the list. Try again with a valid number")
        elif data_share == "3":
            print("NOTE: The following numbers are sharing your subscription plan\n")
            for i, number in enumerate( data_share_no, start=1):
                print(f"{i}. {number}")
        elif data_share == "4":
            data_setting = input("Please send the keyword <flat> to 1234\n"

                                 "99. Back\n"

                                 "0. Exit\n"

                                 )

            if data_setting == "99":

                data_share_options()

            elif data_setting == "0":

                exit_menu()

            else:

                invalid()

                data_share_options()


        elif data_share == "5":

            manual_config = input("Please save the APN details under"

                                  "setting option in your handset.\n"

                                  "APN Name: glo flat\n"

                                  "User Name: flat\n"

                                  "Password: flat\n"

                                  "99. Back\n"

                                  "0. Exit\n")

            if manual_config == "99":

                data_share_options()

            elif manual_config == "0":

                exit_menu()

            else:

                invalid()

                data_share_options()

        elif data_share == "6":

            easy_share = input("To share airtime with other Glo"

                               "Number, Pls dial 131*Glo Number"

                               "Amount*PIN#Default PIN: 00000 Note:"

                               "Easy Share is not available For Berekete"

                               "Customers\n"

                               "99. Back\n"

                               "0. Exit\n")

            if easy_share == "99":

                data_share_options()

            elif easy_share == "0":

                exit_menu()

            else:

                invalid()

                data_share_options()

        elif data_share == "0":

            exit_menu()


        else:

            invalid()

            data_share_options()


def borrow_options():
    borrow_services = input("Dear Customer, Welcome, you are eligible for N1500\n" +
                            "Reply with: \n" +
                            "1. My BMC Account\n" +
                            "2. Borrow Credit\n" +
                            "3. Borrow Data\n" +
                            "4. Borrow Credit for Others\n" +
                            "5. Borrow Data for Others \n"
                            )
    if borrow_services == "1":
        print("Dear Customer, your request stopped unexpectedly at this time. Please try again later")
    elif borrow_services == "2":
        borrow_credit = input("You are eligible for N1500\n"
                              " Reply with\n"
                              "1. N25\n"
                              "2. N50\n"
                              "3. N100\n"
                              "4. N200\n"
                              "5. N300\n"
                              "6. N400\n"
                              "7. N500\n"
                              "8. N800\n"
                              "9. N1000\n"
                              "10. N1200\n"
                              "11. N1500\n"
                              "0. Back\n"
                              )
        if borrow_credit == "1":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N22 airtime at N3 service charge.")
        elif borrow_credit == "2":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N47 airtime at N3 service charge.")
        elif borrow_credit == "3":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N97 airtime at N3 service charge.")
        elif borrow_credit == "4":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N197 airtime at N3 service charge.")
        elif borrow_credit == "5":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N297 airtime at N3 service charge.")
        elif borrow_credit == "6":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N397 airtime at N3 service charge.")
        elif borrow_credit == "7":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N497 airtime at N3 service charge.")
        elif borrow_credit == "8":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N797 airtime at N3 service charge.")
        elif borrow_credit == "9":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N997 airtime at N3 service charge.")
        elif borrow_credit == "10":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N1197 airtime at N3 service charge.")
        elif borrow_credit == "11":
            print("Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                  "with N1497 airtime at N3 service charge.")
        elif borrow_credit == "0":
            pass
        else:
            print("invalid")
    elif borrow_services == "3":
        borrow_data = input("Eligible N1500\n"
                            "Reply with\n"
                            "1. N50 = 35MB + 5MB\n"
                            "2. N100 = 95MB + 130MB\n"
                            "3. N200 = 200MB + 310MB\n"
                            "4. N500 = 650MB + 1.65GB\n"
                            "5. N1000 = 1.6GB + 2GB\n"
                            "6. N1500 = 3GB + 4GB\n"
                            "0. Back\n")
        if borrow_data == "1":
            print("Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 35MB "
                  "data Bundle")
        elif borrow_data == "2":
            print("Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 95MB "
                  "data Bundle")
        elif borrow_data == "3":
            print("Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 200MB "
                  "data Bundle")
        elif borrow_data == "4":
            print("Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 650MB "
                  "data Bundle")
        elif borrow_data == "5":
            print("Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 1.6GB "
                  "data Bundle")
        elif borrow_data == "6":
            print("Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 3GB "
                  "data Bundle")
        elif borrow_data == "0":
            pass
        else:
            print("invalid")
    elif borrow_services == "4":
        credit_others = input("You are eligible for N1500\n"
                              " Reply with\n"
                              "1. N25\n"
                              "2. N50\n"
                              "3. N100\n"
                              "4. N200\n"
                              "5. N300\n"
                              "6. N400\n"
                              "7. N500\n"
                              "8. N800\n"
                              "9. N1000\n"
                              "10. N1200\n"
                              "11. N1500\n"
                              "0. Back\n"
                              )
        if credit_others == "1":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N22 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")

        elif credit_others == "2":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N47 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "3":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N97 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "4":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N197 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "5":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N297 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "6":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N397 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "7":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N497 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "8":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N797 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "9":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N997 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "10":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N1197 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "11":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent N1497 at"
                      f"N3 service charge to {recipient_no} ")
            else:
                print("Invalid Globacom user")
        elif credit_others == "0":
            pass
        else:
            print("invalid")
    # recipient_no = input("Reply with the phone number of the recipient: ")
    elif borrow_services == "5":
        data_others = input("Eligible N1500\n"
                            "Reply with\n"
                            "1. N50 = 35MB + 5MB\n"
                            "2. N100 = 95MB + 130MB\n"
                            "3. N200 = 200MB + 310MB\n"
                            "4. N500 = 650MB + 1.65GB\n"
                            "5. N1000 = 1.6GB + 2GB\n"
                            "6. N1500 = 3GB + 4GB\n"
                            "0. Back\n")
        if data_others == "1":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent 35MB data bundle to {recipient_no} ")
        elif data_others == "2":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code.You have sent 95MB data bundle to {recipient_no}  ")
        elif data_others == "3":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent 200MB data bundle to {recipient_no}  ")
        elif data_others == "4":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent 650MB data bundle to {recipient_no}  ")
        elif data_others == "5":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent 1.6GB data bundle to {recipient_no} ")
        elif data_others == "6":
            recipient_no = input("Reply with the phone number of the recipient: ")
            if recipient_no.isnumeric() and len(recipient_no) == 11:
                print(f"Dear customer, please note *303# is our New"
                      f"Borrow-Me Credit code. You have sent 3GB data bundle to {recipient_no}  ")
        elif data_others == "0":
            pass
        else:
            print("invalid")
    else:
        print("invalid")


def vas_options():
    vas = input("Welcome. Please select.\n" +
                "1. Gaming Service\n" +
                "2. Educational Service\n" +
                "3. Lottery\n" +
                "4. Entertainment\n" +
                "5. Sport Service\n" +
                "6. Caller Tunes\n" +
                "7. BMC\n" +
                "8. Glo Cloud\n" +
                "9. Unsubscribe\n" +
                "0. Exit\n"
                )
    if vas == "1":
        gaming_services = input("Please press\n" +
                                "1. Gaming portal\n" +
                                "2. Gaming Tournament\n" +
                                "3. Edu Games\n" +
                                "4. GamesBox\n" +
                                "5. Games Play\n" +
                                "6. Glo Games Club\n" +
                                "7. Glo Kidjo TV\n" +
                                "8. Wazoo Play\n" +
                                "99. Back\n" +
                                "0. Exit\n"
                                )
        # Done
        if gaming_services == "1":
            gaming_portal_service = input("Welcome to Gaming Portal Service.\n" +
                                          "Choose Pack\n" +
                                          "1. Daily Auto Pack @N30\n" +
                                          "2. Daily one time pack @30\n" +
                                          "99. Back\n" +
                                          "0. Exit"
                                          )
            if gaming_portal_service == "1":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif gaming_portal_service == 2:
                print("MMI complete\n" +
                      "-----------\n" +
                      "Connection problem or invalid MMI code.\n"
                      )
            elif gaming_portal_service == 99:
                pass
            else:
                print("Invalid MMI")
                # Done
        elif gaming_services == "2":
            gaming_tournament = input("Welcome to Gaming Tournament. Press\n" +
                                      "1. Daily Auto @20\n" +
                                      "2. Weekly Auto @50\n" +
                                      "3. Monthly pack @200\n" +
                                      "4. Daily one time @20\n" +
                                      "5. Weekly One time @50\n" +
                                      "6. Monthly Onetime @200\n" +
                                      "99. Back\n" +
                                      "0. Exit\n"
                                      )
            if gaming_tournament == "1":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif gaming_tournament == "2":
                print("This service is not available, please try again later!")
            elif gaming_tournament == "3":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif gaming_tournament == "4":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif gaming_tournament == "5":
                print("This service is not available, please try again later!")
            elif gaming_tournament == "6":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif gaming_tournament == "99":
                pass
            elif gaming_tournament == "0":
                print("Exiting, thank you")
            else:
                print("This service is not available, please try again later!")
        elif gaming_services == "3":
            edu_games = input("Welcome to Edu. Games Service. Press\n" +
                              "1. Daily Auto @20\n" +
                              "2. Weekly Auto @50\n" +
                              "3. Monthly pack @200\n" +
                              "4. Daily one time @20\n" +
                              "5. Weekly One time @50\n" +
                              "6. Monthly Onetime @200\n" +
                              "99. Back\n" +
                              "0. Exit\n"
                              )
            if edu_games == "1":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif edu_games == "2":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif edu_games == "3":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif edu_games == "4":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif edu_games == "5":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif edu_games == "6":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif edu_games == "99":
                pass
            elif edu_games == "0":
                print("Exiting, thank you")
            else:
                print("This service is not available, please try again later!")
        elif gaming_services == "4":
            games_box = input("Welcome to Gamebox Service. Press\n" +
                              "1. Daily Auto @N15\n" +
                              "2. Weekly Auto @N55\n" +
                              "3. Monthly Auto @N155\n" +
                              "4. Daily one time @N15\n" +
                              "5. Weekly One time @55\n" +
                              "6. Monthly Onetime @N155\n" +
                              "99. Back\n" +
                              "0. Exit\n"
                              )
            if games_box == "1":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_box == "2":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_box == "3":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_box == "4":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_box == "5":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_box == "6":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_box == "99":
                pass
            elif games_box == "0":
                print("Exiting, thank you")
            else:
                print("Connection problem or invalid MMI Code")
        elif gaming_services == "5":
            games_play = input("Welcome to Games Play Service. Press\n" +
                               "1. Daily Auto @N20\n" +
                               "2. Weekly Auto @N60\n" +
                               "3. Monthly Auto @N150\n" +
                               "4. Daily one time @N20\n" +
                               "5. Weekly One time @60\n" +
                               "6. Monthly Onetime @N150\n" +
                               "99. Back\n" +
                               "0. Exit\n")
            if games_play == "1":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_play == "2":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_play == "3":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_play == "4":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_play == "5":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_play == "6":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif games_play == "99":
                pass
            elif games_play == "0":
                print("Exiting, thank you")
            else:
                print("Connection problem or invalid MMI Code")

        elif gaming_services == "6":
            glo_games_club = input("Welcome to Glo Games  Service. To Subscribe, Press\n" +
                                   "1. Daily Pack - @N10\n" +
                                   "2. Weekly - @N50\n" +
                                   "3. Monthly Pack - @N100\n" +
                                   "4. Unsubscribe\n" +
                                   "0. Exit\n"
                                   )
            if glo_games_club == "1":
                glo_games_daily = input("For Daily Pack, Please choose\n" +
                                        "1. Auto Renewal\n" +
                                        "2. One-Time\n" +
                                        "99. Back\n" +
                                        "0. Exit\n"

                                        )
                if glo_games_daily == "1":
                    print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                          "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
                elif glo_games_daily == "2":
                    print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                          "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
                elif glo_games_daily == "99":
                    pass
                elif glo_games_daily == "0":
                    print("Exiting, thankyou")
                else:
                    print("invalid")
            elif glo_games_club == "2":
                glo_games_weekly = input("For Weekly Pack, Please choose\n" +
                                         "1. Auto Renewal\n" +
                                         "2. One-Time\n" +
                                         "99. Back\n" +
                                         "0. Exit\n"
                                         )
                if glo_games_weekly == "1":
                    print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                          "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
                elif glo_games_weekly == "2":
                    print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                          "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
                elif glo_games_weekly == "99":
                    pass
                elif glo_games_weekly == "0":
                    print("Exiting,thankyou")
                else:
                    print("invalid")

            elif glo_games_club == "3":
                glo_games_monthly = input("For Monthly Pack, Please choose\n" +
                                          "1. Auto Renewal\n" +
                                          "2. One-Time\n" +
                                          "99. Back\n" +
                                          "0. Exit\n"
                                          )
                if glo_games_monthly == "1":
                    print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                          "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
                elif glo_games_monthly == "2":
                    print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                          "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
                elif glo_games_monthly == "99":
                    pass
                elif glo_games_monthly == "0":
                    print("Exiting,thankyou")
                else:
                    print("invalid")

            elif glo_games_club == "4":
                glo_games_unsubscribe = input("Please select\n" +
                                              "1. Daily Pack\n" +
                                              "2. Weekly\n" +
                                              "3. Monthly Pack\n" +
                                              "99. Back\n" +
                                              "0. Exit\n"
                                              )
                if glo_games_unsubscribe == "1":
                    games_unsubscribe_daily = input("Pleas choose and press\n" +
                                                    "1. Auto Renewal\n" +
                                                    "2. One-Time\n" +
                                                    "99. Back\n" +
                                                    "0. Exit\n"
                                                    )
                    if games_unsubscribe_daily == "1":
                        print("This service is not available, please try again later!")
                    elif games_unsubscribe_daily == "2":
                        print("This service is not available, please try again later!")
                    elif games_unsubscribe_daily == "99":
                        print("This service is not available, please try again later!")
                    elif games_unsubscribe_daily == "0":
                        print("This service is not available, please try again later!")
                    else:
                        print("This service is not available, please try again later!")

                elif glo_games_unsubscribe == "2":
                    games_unsubscribe_weekly = input("Pleas choose and press\n" +
                                                     "1. Auto Renewal\n" +
                                                     "2. One-Time\n" +
                                                     "99. Back\n" +
                                                     "0. Exit\n"
                                                     )
                    if games_unsubscribe_weekly == "1":
                        print("This service is not available, please try again later!")
                    elif games_unsubscribe_weekly == "2":
                        print("This service is not available, please try again later!")
                    elif games_unsubscribe_weekly == "99":
                        print("This service is not available, please try again later!")
                    elif games_unsubscribe_weekly == "0":
                        print("This service is not available, please try again later!")
                    else:
                        print("This service is not available, please try again later!")

                elif glo_games_unsubscribe == "3":
                    games_unsubscribe_monthly = input("Pleas choose and press\n" +
                                                      "1. Auto Renewal\n" +
                                                      "2. One-Time\n" +
                                                      "99. Back\n" +
                                                      "0. Exit\n"
                                                      )
                    if games_unsubscribe_monthly == "1":
                        print("This service is not available, please try again later!")
                    elif games_unsubscribe_monthly == "2":
                        print("This service is not available, please try again later!")
                    elif games_unsubscribe_monthly == "99":
                        print("This service is not available, please try again later!")
                    elif games_unsubscribe_monthly == "0":
                        print("Exiting, thankyou")
                    else:
                        print("This service is not available, please try again later!")

                elif glo_games_unsubscribe == "99":
                    pass
                elif glo_games_unsubscribe == "0":
                    print("Exiting, thankyou")
                else:
                    print("invalid")
            elif glo_games_club == "0":
                print("Exiting, thankyou")

            else:
                print("invalid")
        elif gaming_services == "7":
            glo_kidjo_tv = input("Welcome to Glo Kidjo. Pls Select:\n" +
                                 "1. Daily Auto @N20\n" +
                                 "2. Weekly Auto @N60\n" +
                                 "3. Monthly Auto @N150\n" +
                                 "4. Daily one time @N20\n" +
                                 "5. Weekly One time @60\n" +
                                 "6. Monthly Onetime @N150\n" +
                                 "0. Exit\n")
            if glo_kidjo_tv == "1":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif glo_kidjo_tv == "2":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif glo_kidjo_tv == "3":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif glo_kidjo_tv == "4":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif glo_kidjo_tv == "5":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif glo_kidjo_tv == "6":
                print("Dear Customer, your number has been blacklisted for VAS service activation. Please send "
                      "CANCEL to 2442 and then try again after 24 Hours to activate a service. Thank you")
            elif glo_kidjo_tv == "0":
                print("Send USSD failed\n" +
                      "__________\n" +
                      "MMI complete\n" +
                      "____________\n" +
                      "Connection problem or invalid MMI code\n"
                      )
            else:
                print("invalid")

        elif gaming_services == "8":
            wazoo_play = input("WAZOO PLAY: Subscribe to PLAY:\n"
                               "1. Daily Auto @N20/day\n"
                               "2. Weekly Auto @N100/wk\n"
                               "3. Daily Onetim @N20/day\n"
                               "4. Weekly Onetime @N100/wk\n"
                               "5. Unsubscribe\n"
                               "0. Exit"

                               )
            if wazoo_play == "1":
                print("Failed to subscribe to the product. Try again later.")
            elif wazoo_play == "2":
                print("Failed to subscribe to the product. Try again later.")
            elif wazoo_play == "3":
                print("Failed to subscribe to the product. Try again later.")
            elif wazoo_play == "4":
                print("Failed to subscribe to the product. Try again later.")
            elif wazoo_play == "5":
                unsubscribe_wazooplay = input("To unsubscibe from Wazoplay:\n"
                                              "1. Daily Auto @N20/day\n"
                                              "2. Weekly Auto @N100/wk\n"
                                              "3. Daily Onetim @N20/day\n"
                                              "4. Weekly Onetime @N100/wk\n"
                                              "99. Back\n"
                                              "0. Exit"
                                              )

                if unsubscribe_wazooplay == "1":
                    print("Dear Customer, your subscription of product WAZOPLAY  DAILY AUTO does not exist.")
                elif unsubscribe_wazooplay == "2":
                    print("Dear Customer, your subscription of product WAZOPLAY WEEKLY AUTO does not exist.")
                elif unsubscribe_wazooplay == "3":
                    print("Dear Customer, your subscription of product WAZOPLAY DAILY ONETIME does not exist.")
                elif unsubscribe_wazooplay == "4":
                    print("Dear Customer, your subscription of product WAZOPLAY WEEKLY ONETIME does not exist.")
                elif unsubscribe_wazooplay == "99":
                    print("Failed to subscribe to the product. Try again later.")
                elif unsubscribe_wazooplay == "0":
                    print("Exiting, thank you.")
                else:
                    print("invalid")
            elif wazoo_play == "0":
                print("Exiting, thank you.")
            else:
                print("invalid")
        elif gaming_services == "99":
            pass
        elif gaming_services == "0":
            print("Exiting, thank you.")
        else:
            print("Invalid MMI code")
    elif vas == "2":
        educational_service = input("Please Press\n"
                                    "1. Language Learning- Busuu\n"
                                    "2. Edu Video\n"
                                    "99. Back\n"
                                    "0. Exit\n"
                                    )
        if educational_service == "1":
            busuu_language = input("Welcome to Buss Language Learning Service\n"
                                   "Choose Pack"
                                   "1. Daily Auto Pack @N20\n"
                                   "2. Weekly Auto Pack@N100\n"
                                   "3. Daily Onetime Pack @N20\n"
                                   "4. Weekly Onetime Pack @N100\n"
                                   "99. Back\n"
                                   "0. Exit"
                                   )
            if busuu_language == "1":
                print("Failed to subscribe to the product. Try again later.")
            elif busuu_language == "2":
                print("Failed to subscribe to the product. Try again later.")
            elif busuu_language == "3":
                print("Failed to subscribe to the product. Try again later.")
            elif busuu_language == "4":
                print("Failed to subscribe to the product. Try again later.")
            elif busuu_language == "99":
                pass
            else:
                print("invalid")
        elif educational_service == "2":
            edu_video = input("Welcome to Edu. Video Service. Press\n" +
                              "1. Daily Auto @N20\n" +
                              "2. Weekly Auto @N50\n" +
                              "3. Monthly Auto @N200\n" +
                              "4. Daily one time @N20\n" +
                              "5. Weekly One time @50\n" +
                              "6. Monthly Onetime @N200\n" +
                              "0. Exit\n")
            if edu_video == "1":
                print("Failed to subscribe to the product. Try again later.")
            elif edu_video == "2":
                print("Failed to subscribe to the product. Try again later.")
            elif edu_video == "3":
                print("Failed to subscribe to the product. Try again later.")
            elif edu_video == "4":
                print("Failed to subscribe to the product. Try again later.")
            elif edu_video == "5":
                print("Failed to subscribe to the product. Try again later.")
            elif edu_video == "6":
                print("Failed to subscribe to the product. Try again later.")
            elif edu_video == "0":
                print("Exiting, thank you")
            else:
                print("invalid")
        elif educational_service == "99":
            pass
        elif educational_service == "0":
            print("Exiting, thank you")
        else:
            print("invalid")
    elif vas == "3":
        lottery = input("Press\n"
                        "1. Lucky Number\n"
                        "2. Green Lotto\n"
                        "3. Perfect 10\n"
                        "4. Jolly Suite\n"
                        "5. Africa Winner\n"
                        "6. Zoom Lottery\n"
                        "99. Back\n"
                        "0. Exit\n"
                        )
        if lottery == "1":
            lucky_numbers = input("Welcome to Lucky Number service\n"
                                  "Please choose\n"
                                  "1. Lucky Number Economy: N50\n"
                                  "2. Lucky Number Max: N200\n"
                                  "3. Lucky Number Premium: N500\n"
                                  "4. Unsubscribe\n"
                                  "5. Draw Result\n"
                                  "0. Exit\n"
                                  )
            if lucky_numbers == "1":
                lucky_numbers_eco = input("Thanks for choosing Lucky Number Economy pack @50 daily. Please "
                                          "confirm.\n"
                                          "1. Auto-renewal\n"
                                          "2. One-time or one off\n"
                                          "99. Back\n"
                                          "0. Exit"
                                          )
                if lucky_numbers_eco == "1":
                    print("Failed to subscribe to the product. Try again later.")
                elif lucky_numbers_eco == "2":
                    print("Failed to subscribe to the product. Try again later.")
                elif lucky_numbers_eco == "99":
                    pass
                elif lucky_numbers_eco == "0":
                    print("Exiting, thank you")
                else:
                    print("invalid")
            elif lucky_numbers == "2":
                lucky_numbers_max = input("Thanks for choosing Lucky Number Max pack @200 daily. Please "
                                          "confirm.\n"
                                          "1. Auto-renewal\n"
                                          "2. One-time or one off\n"
                                          "99. Back\n"
                                          "0. Exit"
                                          )
                if lucky_numbers_max == "1":
                    print("Failed to subscribe to the product. Try again later.")
                elif lucky_numbers_max == "2":
                    print("Failed to subscribe to the product. Try again later.")
                elif lucky_numbers_max == "99":
                    pass
                elif lucky_numbers_max == "0":
                    print("Exiting, thank you")
                else:
                    print("invalid")
            elif lucky_numbers == "3":
                lucky_numbers_premium = input("Thanks for choosing Lucky Number Premium pack @500 daily. Please "
                                              "confirm.\n"
                                              "1. Auto-renewal\n"
                                              "2. One-time or one off\n"
                                              "99. Back\n"
                                              "0. Exit"
                                              )
                if lucky_numbers_premium == "1":
                    print("Failed to subscribe to the product. Try again later.")
                elif lucky_numbers_premium == "2":
                    print("Failed to subscribe to the product. Try again later.")
                elif lucky_numbers_premium == "99":
                    pass
                elif lucky_numbers_premium == "0":
                    print("Exiting, thank you")
                else:
                    print("invalid")
            elif lucky_numbers == "4":
                unsubscribe_lucky_numbers = input("Select Package:\n"

                                                  "1. Lucky Number Economy: \n"
                                                  "2. Lucky Number Max: \n"
                                                  "3. Lucky Number Premium: \n"
                                                  "99. Back\n"
                                                  "0. Exit\n"
                                                  )
                if unsubscribe_lucky_numbers == "1":
                    unsubscribe_eco = input("1. Lucky Number Economy Auto\n"
                                            "2. Lucky Number Economy one-time\n"
                                            "99. Back"
                                            "0. Exit"
                                            )
                    if unsubscribe_eco == "1":
                        print("Failed to subscribe to the product. Try again later.")
                    elif unsubscribe_eco == "2":
                        print("Failed to subscribe to the product. Try again later.")
                    elif unsubscribe_eco == "99":
                        pass
                    elif unsubscribe_eco == "0":
                        print("Exiting, thank you")
                    else:
                        print("invalid selection")
                elif unsubscribe_lucky_numbers == "2":
                    unsubscribe_max = input("1. Lucky Number Max Auto\n"
                                            "2. Lucky Number Max one-time\n"
                                            "99. Back\n"
                                            "0.Exit"
                                            )
                    if unsubscribe_max == "1":
                        print("Failed to subscribe to the product. Try again later.")
                    elif unsubscribe_max == "2":
                        print("Failed to subscribe to the product. Try again later.")
                    elif unsubscribe_max == "99":
                        pass
                    elif unsubscribe_max == "0":
                        print("Exiting Thank you")
                    else:
                        print("invalid selection")
                elif unsubscribe_lucky_numbers == "3":
                    unsubscribe_premium = input("1. Lucky Number Premium Auto\n"
                                                "2. Lucky Number Premium one-time\n"
                                                "99. Back\n"
                                                "0.Exit"
                                                )
                    if unsubscribe_premium == "1":
                        print("Failed to subscribe to the product. Try again later.")
                    elif unsubscribe_premium == "2":
                        print("Failed to subscribe to the product. Try again later.")
                    elif unsubscribe_premium == "99":
                        pass
                    elif unsubscribe_premium == "0":
                        print("Exiting Thank you")
                    else:
                        print("invalid selection")
                elif unsubscribe_lucky_numbers == "99":
                    pass
                elif unsubscribe_lucky_numbers == "0":
                    print("Exiting, thank you")
                else:
                    print("Invalid")
            elif lucky_numbers == "5":
                print("This service is not available. Please try again later.")
            elif lucky_numbers == "0":
                print("Exiting, thank you")
            else:
                print("Invalid")
        elif lottery == "2":
            green_lotto = input("Green Lotto. I accept T&C by Playing/Subscribing\n"
                                "1. Economy N50\n"
                                "2. Premium @N100\n"
                                "3. Daily Draw Menu\n"
                                "4. Instant Draw Menu\n"
                                "5. Play5/90\n"
                                "6. Scratch Game\n"
                                "7. Winning\n"
                                "8. Add Bank\n"
                                "0. Exit\n"
                                "        \n"
                                "88. Next\n"

                                )
            if green_lotto == "1":
                green_lotto_economy = input("For Economy pack, Please choose\n"
                                            "1. Auto Renewal Daily @50\n"
                                            "2. One-Time @50\n"
                                            "99. Back\n"
                                            "0. Exit\n"
                                            )
                if green_lotto_economy == "1":
                    print("This service is not available. Please try again later.")
                elif green_lotto_economy == "2":
                    print("This service is not available. Please try again later.")
                elif green_lotto_economy == "99":
                    pass
                elif green_lotto_economy == "0":
                    print("Exiting, thank you")
                else:
                    print("invalid")

            elif green_lotto == "2":
                green_lotto_premium = input("For Premium pack, Please choose\n"
                                            "1. Auto Renewal @100\n"
                                            "2. One-Time @100\n"
                                            "99. Back\n"
                                            "0. Exit\n"
                                            )
                if green_lotto_premium == "1":
                    print("This service is not available. Please try again later.")
                elif green_lotto_premium == "2":
                    print("This service is not available. Please try again later.")
                elif green_lotto_premium == "99":
                    pass
                elif green_lotto_premium == "0":
                    print("Exiting, thank you")
                else:
                    print("invalid")
            elif green_lotto == "3":
                green_lotto_draw = input("Please Confirm\n"
                                         "1. N50\n"
                                         "2. N100\n")
                if green_lotto_draw == "1":
                    print("Error in deducting Airtime.Try again")
                elif green_lotto_draw == "1":
                    print("Error in deducting Airtime.Try again")
                else:
                    print("invalid")
            elif green_lotto == "4":
                green_lotto_instant = input("Please Confirm\n"
                                            "1. N50\n"
                                            "         "
                                            "2. N100\n"
                                            )
                if green_lotto_instant == "1":
                    print("Error in deducting Airtime.Try again")
                elif green_lotto_instant == "1":
                    print("Error in deducting Airtime.Try again")
                else:
                    print("invalid")
            elif green_lotto == "5":
                green_lotto_play = input("Today's Game\n"
                                         "1. DESTINY 5/99 06:30PM\n"
                                         "2. CHAMPION 5/90 09:00PM\n"
                                         "3. WIN BIG 5/90 10:00PM\n"
                                         "                         "
                                         "0. Exit"
                                         )
                if green_lotto_play == "1":
                    green_lotto_destiny = input("An error occurred. Please try again later.\n"
                                                "Error Code: (SL - 17086419522804)\n"
                                                "0. Exit"
                                                )
                    if green_lotto_destiny == "0":
                        print("Exiting")
                    else:
                        print("Exiting")
                elif green_lotto_play == "2":
                    green_lotto_champion = input("An error occurred. Please try again later.\n"
                                                 "Error Code: (SL - 17086421367654)\n"
                                                 "0. Exit"
                                                 )
                    if green_lotto_champion == "0":
                        print("Exiting")
                    else:
                        print("Exiting")
                elif green_lotto_play == "3":
                    green_lotto_win = input("An error occurred. Please try again later.\n"
                                            "Error Code: (SL - 17086421843889)\n"
                                            "0. Exit"
                                            )
                    if green_lotto_win == "0":
                        print("Exiting")
                    else:
                        print("Exiting")

                else:
                    pass
            elif green_lotto == "6":
                green_lotto_scratch = input("Select stake amount\n"
                                            "1. 50\n"
                                            "2. 100\n"
                                            )
                if green_lotto_scratch == "1":
                    lotto_deduction_source50 = input("Select Deduction Source\n"
                                                     "1. Airtime\n"
                                                     "2. Wallet\n")
                    if lotto_deduction_source50 == "1":
                        print("Object reference not set to an instance of an object")
                    elif lotto_deduction_source50 == "2":
                        print("Object reference not set to an instance of an object")

                    else:
                        print("exiting")
                elif green_lotto_scratch == "2":
                    lotto_deduction_source100 = input("Select Deduction Source\n"
                                                      "1. Airtime\n"
                                                      "2. Wallet\n")
                    if lotto_deduction_source100 == "1":
                        print("Object reference not set to an instance of an object")
                    elif lotto_deduction_source100 == "2":
                        print("Object reference not set to an instance of an object")

                    else:
                        print("exiting")
                else:
                    print("Exiting")
            elif green_lotto == "7":
                print("There is no winning in your account")
                # comeback here
            elif green_lotto == "8":
                pass
            # comeback here
            elif green_lotto == "0":
                print("Exiting, thank you")
            elif green_lotto == "88":
                green_lotto_next = input("9. History\n"
                                         "10. Check Wallet Balance\n"
                                         "11. Result\n"
                                         "12. Unsubscribe\n"
                                         "99. Back\n"
                                         "0. Exit\n"
                                         )
                if green_lotto_next == "9":
                    print("You have no transaction for today")
                elif green_lotto_next == "10":
                    print("Wallet Balance\n"
                          "1. Cashin Wallet Balance: NGN 0\n"
                          "2. Cashout Wallet balance balance: NGN 0\n"
                          "3. Promo Balance: NGN 0\n"
                          )
                elif green_lotto_next == "11":
                    green_lotto_result = input("An error occurred. Please try again later.\n"
                                               "Error Code: (SL - 17086443072160)\n"
                                               "0. Exit"
                                               )
                    if green_lotto_result == "0":
                        print("Exiting")
                    else:
                        print("Exiting")
                elif green_lotto_next == "12":
                    green_lotto_unsubscribe = input("Please Select\n"
                                                    "1. Economy Pack\n"
                                                    "2. Premium Pack\n"
                                                    "99. Back\n"
                                                    "0.Exit\n"
                                                    )
                    if green_lotto_unsubscribe == "1":
                        lotto_unsubscribe_economy = input("For Economy pack, Please choose\n"
                                                          "1. Auto Renewal Daily\n"
                                                          "2. One-Time\n"
                                                          "99. Back\n"
                                                          "0. Exit"
                                                          )
                        if lotto_unsubscribe_economy == "1":
                            print("This service is not available. Please try again later.")
                        elif lotto_unsubscribe_economy == "2":
                            print("This service is not available. Please try again later.")
                        elif lotto_unsubscribe_economy == "99":
                            pass
                        elif lotto_unsubscribe_economy == "0":
                            print("Exiting")
                        else:
                            print("invalid")

                    elif green_lotto_unsubscribe == "2":
                        lotto_unsubscribe_premium = input("For Premium pack, Please choose\n"
                                                          "1. Auto Renewal Daily\n"
                                                          "2. One-Time\n"
                                                          "99. Back\n"
                                                          "0. Exit"
                                                          )
                        if lotto_unsubscribe_premium == "1":
                            print("This service is not available. Please try again later.")
                        elif lotto_unsubscribe_premium == "2":
                            print("This service is not available. Please try again later.")
                        elif lotto_unsubscribe_premium == "99":
                            pass
                        elif lotto_unsubscribe_premium == "0":
                            print("Exiting")
                        else:
                            print("invalid")
                    elif green_lotto_unsubscribe == "99":
                        pass
                    elif green_lotto_unsubscribe == "0":
                        print("Exiting, thank you")
                    else:
                        print("invalid")
                elif green_lotto_next == "99":
                    pass
                elif green_lotto_next == "0":
                    print("exiting, thank you")
                else:
                    print("invalid")

            else:
                print("Invalid")
        elif lottery == "3":
            pass
        elif lottery == "4":
            pass
        elif lottery == "5":
            pass
        elif lottery == "6":
            pass
        elif lottery == "99":
            pass
        elif lottery == "0":
            pass
        else:
            pass
    elif vas == "4":
        entertainment = input("1. Glo Magazine\n"
                              "2. TAPESTRY\n"
                              "99. Back\n"
                              "0. Exit\n")
        if entertainment == "1":
            magazine_services = input("Welcome to Glo Magazine Service. Press\n" +
                                      "1. Daily Auto @N30\n" +
                                      "2. Weekly Auto @N100\n" +
                                      "3. Monthly Auto @N200\n" +
                                      "4. Daily one time @N30\n" +
                                      "5. Weekly One time @100\n" +
                                      "6. Monthly Onetime @N200\n" +
                                      "99. Back\n"
                                      "0. Exit\n")
            if magazine_services == "1":
                print("Failed to subscribe to the product. Try again later.")
            elif magazine_services == "2":
                print("Failed to subscribe to the product. Try again later.")
            elif magazine_services == "3":
                print("Failed to subscribe to the product. Try again later.")
            elif magazine_services == "4":
                print("Failed to subscribe to the product. Try again later.")
            elif magazine_services == "5":
                print("Failed to subscribe to the product. Try again later.")
            elif magazine_services == "5":
                print("Failed to subscribe to the product. Try again later.")
            elif magazine_services == "6":
                print("Failed to subscribe to the product. Try again later.")
            elif magazine_services == "99":
                pass
            elif magazine_services == "0":
                print("Exiting Thank you")
            else:
                pass
        elif entertainment == "2":
            tapestry = input("TAPESTRY Comedy: Subscribe to the Service Select Category:" +
                             "1. Daily Auto @N50\n" +
                             "2. Weekly Auto @N200\n" +
                             "3. Daily one time @N50\n" +
                             "4. Weekly One time @200\n" +
                             "5. Unsubscribe\n" +
                             "99. Back\n" +
                             "0. Exit\n")
            if tapestry == "1":
                print("Failed to subscribe to the product. Try again later.")
            elif tapestry == "2":
                print("Failed to subscribe to the product. Try again later.")
            elif tapestry == "3":
                print("Failed to subscribe to the product. Try again later.")
            elif tapestry == "4":
                print("Failed to subscribe to the product. Try again later.")
            elif tapestry == "5":
                tapestry_unsubscribe = input("To Unsubscribe from the Service Select Category:\n" +
                                             "1. Daily Auto @N50\n" +
                                             "2. Weekly Auto @N200\n" +
                                             "3. Daily one time @N50\n" +
                                             "4. Weekly One time @200\n" +
                                             "99. Back\n" +
                                             "0. Exit\n")
                if tapestry_unsubscribe == "1":
                    print("Failed to unsubscribe to the product. Try again later.")
                elif tapestry_unsubscribe == "2":
                    print("Failed to unsubscribe to the product. Try again later.")
                elif tapestry_unsubscribe == "3":
                    print("Failed to unsubscribe to the product. Try again later.")
                elif tapestry_unsubscribe == "4":
                    print("Failed to unsubscribe to the product. Try again later.")
                elif tapestry_unsubscribe == "99":
                    pass
                elif tapestry_unsubscribe == "0":
                    print("Exiting,thank you")
                else:
                    print("invalid selection")
            elif tapestry == "99":
                pass
            elif tapestry == "0":
                print("exiting thank you")

            else:
                print("invalid")
        elif entertainment == "99":
            pass
        elif entertainment == "0":
            print("exiting,thank you")
        else:
            print("invalid")
    elif vas == "5":
        sports_service = input("1. Sports Video Portal\n"
                               "2. Sports Portal\n"
                               "99. Back\n"
                               "0. Exit\n")
        if sports_service == "1":
            sport_video = input("Welcome to Sports Video Portal Service.Press\n" +
                                "1. Daily Auto @N30\n" +
                                "2. Weekly Auto @N100\n" +
                                "3. Daily one time @N30\n" +
                                "4. Weekly One time @100\n" +
                                "99. Back\n" +
                                "0. Exit\n")
            if sport_video == "1":
                pass
            elif sport_video == "2":
                pass
            elif sport_video == "3":
                pass
            elif sport_video == "4":
                pass
            elif sport_video == "99":
                pass
            elif sport_video == "0":
                pass
            else:
                print("Invalid")
        elif sports_service == "2":
            pass
        elif sports_service == "99":
            pass
        elif sports_service == "0":
            pass
        else:
            print("invalid")
    elif vas == "6":
        print("This service is not available. Please try again later.")
    elif vas == "7":
        borrow_services = input("Dear Customer, Welcome, you are eligible for N1500\n" +
                                "Reply with: \n" +
                                "1. My BMC Account\n" +
                                "2. Borrow Credit\n" +
                                "3. Borrow Data\n" +
                                "4. Borrow Credit for Others\n" +
                                "5. Borrow Data for Others \n"
                                )
        if borrow_services == "1":
            print("Dear Customer, your request stopped unexpectedly at this time. Please try again later")
        elif borrow_services == "2":
            borrow_credit = input("You are eligible for N1500\n"
                                  " Reply with\n"
                                  "1. N25\n"
                                  "2. N50\n"
                                  "3. N100\n"
                                  "4. N200\n"
                                  "5. N300\n"
                                  "6. N400\n"
                                  "7. N500\n"
                                  "8. N800\n"
                                  "9. N1000\n"
                                  "10. N1200\n"
                                  "11. N1500\n"
                                  "0. Back\n"
                                  )
            if borrow_credit == "1":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N22 airtime at N3 service charge.")
            elif borrow_credit == "2":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N47 airtime at N3 service charge.")
            elif borrow_credit == "3":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N97 airtime at N3 service charge.")
            elif borrow_credit == "4":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N197 airtime at N3 service charge.")
            elif borrow_credit == "5":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N297 airtime at N3 service charge.")
            elif borrow_credit == "6":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N397 airtime at N3 service charge.")
            elif borrow_credit == "7":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N497 airtime at N3 service charge.")
            elif borrow_credit == "8":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N797 airtime at N3 service charge.")
            elif borrow_credit == "9":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N997 airtime at N3 service charge.")
            elif borrow_credit == "10":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N1197 airtime at N3 service charge.")
            elif borrow_credit == "11":
                print(
                    "Dear Customer, please note that *303# is our New Borrow-Me Credit code. You have been credited "
                    "with N1497 airtime at N3 service charge.")
            elif borrow_credit == "0":
                pass
            else:
                print("invalid")
        elif borrow_services == "3":
            borrow_data = input("Eligible N1500\n"
                                "Reply with\n"
                                "1. N50 = 35MB + 5MB\n"
                                "2. N100 = 95MB + 130MB\n"
                                "3. N200 = 200MB + 310MB\n"
                                "4. N500 = 650MB + 1.65GB\n"
                                "5. N1000 = 1.6GB + 2GB\n"
                                "6. N1500 = 3GB + 4GB\n"
                                "0. Back\n")
            if borrow_data == "1":
                print(
                    "Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 35MB "
                    "data Bundle")
            elif borrow_data == "2":
                print(
                    "Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 95MB "
                    "data Bundle")
            elif borrow_data == "3":
                print(
                    "Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 200MB "
                    "data Bundle")
            elif borrow_data == "4":
                print(
                    "Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 650MB "
                    "data Bundle")
            elif borrow_data == "5":
                print(
                    "Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 1.6GB "
                    "data Bundle")
            elif borrow_data == "6":
                print(
                    "Dear Customer, please note that 303# is our New Borrow-Me Credit code. You have received 3GB "
                    "data Bundle")
            elif borrow_data == "0":
                pass
            else:
                print("invalid")
        elif borrow_services == "4":
            credit_others = input("You are eligible for N1500\n"
                                  " Reply with\n"
                                  "1. N25\n"
                                  "2. N50\n"
                                  "3. N100\n"
                                  "4. N200\n"
                                  "5. N300\n"
                                  "6. N400\n"
                                  "7. N500\n"
                                  "8. N800\n"
                                  "9. N1000\n"
                                  "10. N1200\n"
                                  "11. N1500\n"
                                  "0. Back\n"
                                  )
            if credit_others == "1":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N22 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")

            elif credit_others == "2":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N47 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "3":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N97 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "4":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N197 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "5":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N297 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "6":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N397 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "7":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N497 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "8":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N797 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "9":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N997 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "10":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N1197 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "11":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent N1497 at"
                          f"N3 service charge to {recipient_no} ")
                else:
                    print("Invalid Globacom user")
            elif credit_others == "0":
                pass
            else:
                print("invalid")
        # recipient_no = input("Reply with the phone number of the recipient: ")
        elif borrow_services == "5":
            data_others = input("Eligible N1500\n"
                                "Reply with\n"
                                "1. N50 = 35MB + 5MB\n"
                                "2. N100 = 95MB + 130MB\n"
                                "3. N200 = 200MB + 310MB\n"
                                "4. N500 = 650MB + 1.65GB\n"
                                "5. N1000 = 1.6GB + 2GB\n"
                                "6. N1500 = 3GB + 4GB\n"
                                "0. Back\n")
            if data_others == "1":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent 35MB data bundle to {recipient_no} ")
            elif data_others == "2":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code.You have sent 95MB data bundle to {recipient_no}  ")
            elif data_others == "3":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent 200MB data bundle to {recipient_no}  ")
            elif data_others == "4":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent 650MB data bundle to {recipient_no}  ")
            elif data_others == "5":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent 1.6GB data bundle to {recipient_no} ")
            elif data_others == "6":
                recipient_no = input("Reply with the phone number of the recipient: ")
                if recipient_no.isnumeric() and len(recipient_no) == 11:
                    print(f"Dear customer, please note *303# is our New"
                          f"Borrow-Me Credit code. You have sent 3GB data bundle to {recipient_no}  ")
            elif data_others == "0":
                pass
            else:
                print("invalid")
        else:
            print("invalid")
    elif vas == "8":
        glo_cloud = input("Glo Cloud Service. 1st Month free. Please visit https://glocloud.gloworld.com to "
                          "subscribe\n"
                          "99. Back\n"
                          "0. Exit\n")
    elif vas == "9":
        unsubscribe = input("To Unsubscribe,press\n"
                            "1. Gaming Service\n" +
                            "2. Educational Service\n" +
                            "3. Lottery Service\n" +
                            "4. Entertainment Service\n" +
                            "5. Sport Service\n" +
                            "6. Caller Tunes Service\n" +
                            "7. BMC Service\n" +
                            "8. Glo Cloud service\n" +
                            "99. Back\n" +
                            "0. Exit\n"
                            )
        if unsubscribe == "1":
            pass
        elif unsubscribe == "2":
            pass
        elif unsubscribe == "3":
            pass
        elif unsubscribe == "4":
            pass
        elif unsubscribe == "5":
            pass
        elif unsubscribe == "6":
            pass
        elif unsubscribe == "2":
            pass
        elif unsubscribe == "2":
            pass
        elif unsubscribe == "2":
            pass
        elif unsubscribe == "2":
            pass
        else:
            print("Invalid")


    elif vas == "0":
        pass
    else:
        print("Invalid")


def select_transaction():
    select_transaction1 = input("Select Transaction\n" +
                                "1. Data plans\n" +
                                "2. Borrow Services\n" +
                                "3. Recharge\n" +
                                "4. Data Share\n" +
                                "5. Check Balance\n" +
                                "6. Data Balance\n" +
                                "7. VAS\n"
                                "8. Glo Rewards Cash token\n"
                                "0. Exit\n"
                                "        \n"
                                "88. Next\n"
                                )
    if select_transaction1 == "1":
        data_plans()
    elif select_transaction1 == "2":
        borrow_options()
    elif select_transaction1 == "3":
        recharge_options()
    elif select_transaction1 == "4":
        data_share_options()
    elif select_transaction1 == "5":
        check_balance_options()
    elif select_transaction1 == "6":
        data_balance_options()
    elif select_transaction1 == "7":

        vas_options()
    elif select_transaction1 == "8":
        cash_tokens()
    elif select_transaction1 == "0":
        exit_menu()
    elif select_transaction1 == "88":
        pass
        # next_transaction_option()
    else:
        invalid()
        select_transaction()


main_menu()
