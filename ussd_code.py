ussd_code = input("Enter your ussd code below: ")
if ussd_code == "*301#":
    select_transaction = input("Select Transaction\n" +
                               "1. Data plans\n" +
                               "2. Borrow Services\n" +
                               "3. Recharge\n" +
                               "4. Data Share\n" +
                               "5. Check Balance\n" +
                               "6. Data Balance\n" +
                               "7. VAS\n" +
                               "8. Glo Rewards Cash token\n"
                               )
    if select_transaction == "1":
        data_plans = input("1. Buy Data\n" +
                           "2. Gift Data\n" +
                           "3. Share Data\n" +
                           "4. Check Data Bal\n" +
                           "5. Voice/ Data Roaming Offers\n" +
                           "6. Glo Rewards - Cash token\n"
                           )
        if data_plans == "1":
            buy_data = input("1. Proceed (Auto-Renew)\n" +
                             "2. Proceed (One-off)\n" +
                             "99. Back\n" +
                             "Exit\n"
                             )
            if buy_data == "1":
                auto_buy_data = input("1. Mini Plans\n" +
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
                if auto_buy_data == "1":
                    mini_plans = input("1. N100 = 150MB 1 Day incl 35MB nite\n" +
                                       "2. N200 = 350MB 2 Days incl 110MB nite\n" +
                                       "3. N500 = 1.8GB 14 Days incl 1 GB nite\n" +
                                       "4. N50 = 50MB 1 Day incl 5MB nite\n" +
                                       "5. More Plans\n" +
                                       "99. Back\n" +
                                       "0. Exit\n"
                                       )

            elif buy_data == "2":
                one_off_buy_data = input("1. Mini Plans\n" +
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
            else:
                print("Input required, Try again")

        elif data_plans == "2":
            gift_data = input("1. Mini Plans\n" +
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
        elif data_plans == "3":
            share_data = input("1. Share Data\n" +
                               "2. Unshare Data\n" +
                               "3. List of Shared Numbers\n" +
                               "4. Get Data Settings\n" +
                               "5. Manual Configuration Details\n" +
                               "6. Easy Share (Credit Share)\n"
                               "0. Exit\n"
                               )
        elif data_plans == "4":
            print(
                "Dear Customer, your plan has expired and you do not have a data plan. To buy a data plan and continue "
                "browsing visit https://hsi.glo.com or dial *312#")
        elif data_plans == "5":
            voice_data_roaming = input("1. My Tariff Plan\n" +
                                       "2. Intl Call Offers\n" +
                                       "3. Data Roaming Offers\n" +
                                       "99. Back\n" +
                                       "0. Exit\n"
                                       )
            if voice_data_roaming == "1":
                tariff_plan = input("1. My Package\n"
                                    "2. My Number\n"
                                    "3. Friends and family Number\n"
                                    "4. Easy Share\n"
                                    "99. Back\n"
                                    "0. Exit")
                if tariff_plan == "1":
                    package = input("1. To Know Your Package Dial #100#\n"
                                    "2. To Migrate to other profile Dial *100#\n"
                                    "99. Back\n"
                                    "0. Exit\n")
                    if package == "1":
                        package = input("1. To Know Your Package Dial #100#\n"
                                        "2. To Migrate to other profile Dial *100#\n"
                                        "99. Back\n"
                                        "0. Exit\n")
                    elif package == "2":
                        package = input("1. To Know Your Package Dial #100#\n"
                                        "2. To Migrate to other profile Dial *100#\n"
                                        "99. Back\n"
                                        "0. Exit\n")
                    elif package == "99":
                        pass
                    elif package == "0":
                        print("Exiting, Thank you")
                    else:
                        print("invalid")
                elif tariff_plan == "2":
                    my_number = input("Dear customer, to know you Glo Number, please dial 777*#\n"
                                      "99. Back\n"
                                      "0.Exit\n")
                    if my_number == "99":
                        pass
                    elif my_number == "0":
                        print("Exiting, thank you")
                    else:
                        print("invalid")
                elif tariff_plan == "3":
                    family_friend = input("1. To manage friends and family, Dial *606*1#\n"
                                          "2. View friends and family list, Dial *170*50#\n"
                                          "99. Back\n"
                                          "0. Exit\n")
                    if family_friend == "1":
                        family_friend1 = input("1. To manage friends and family, Dial *606*1#\n"
                                               "2. View friends and family list, Dial *170*50#\n"
                                               "99. Back\n"
                                               "0. Exit\n")
                    elif family_friend == "2":
                        family_friend1 = input("1. To manage friends and family, Dial *606*1#\n"
                                               "2. View friends and family list, Dial *170*50#\n"
                                               "99. Back\n"
                                               "0. Exit\n")
                    elif family_friend == "99":
                        pass
                    elif family_friend == "0":
                        print("Exiting, Thank you")
                    else:
                        print("invalid")

                elif tariff_plan == "4":
                    easy_share = input("Dear Customer,for Me2U please dial *131*nPhone Number * Amount * Pin #\n"
                                       "99. Back\n"
                                       "0. Exit\n")
                    if easy_share == "99":
                        pass
                    elif easy_share == "0":
                        print("Exting, Thank you"
                              )
                    else:
                        print("invalid")

                elif tariff_plan == "99":
                    pass
                elif tariff_plan == "0":
                    print("Exiting, thank you")
                else:
                    print("invalid")
            elif voice_data_roaming == "2":
                international_calls = input("1. N100 = 4 min 3 Days\n"
                                            "2. N200 = 8 min 7 Days\n"
                                            "3. N500 = 22 min 14 Days\n"
                                            "4. N1000 = 44 min 30 Days\n"
                                            "5. List of 10 countries\n"
                                            "6. Check IDD Pack Balance\n"
                                            "99. Back\n"
                                            "0. Exit\n")
                if international_calls == "1":
                    int_hundred = input("Please E-top up your line with N99 to enjoy benefits under this plan.\n"
                                        "For paper recharge of N100 Dial *605*\n"
                                        "99. Back\n"
                                        "0. Exit\n")
                    if int_hundred == "99":
                        pass
                    elif int_hundred == "0":
                        print("Exiting, thank you")
                    else:
                        print("Exiting. Thank you")
                elif international_calls == "2":
                    int_thundred = input("Please E-top up your line with N199 to enjoy benefits under this plan.\n"
                                         "For paper recharge of N200 Dial *605*\n"
                                         "99. Back\n"
                                         "0. Exit\n")
                    if int_thundred == "99":
                        pass
                    elif int_thundred == "0":
                        print("Exiting, thank you")
                    else:
                        print("Exiting. Thank you")
                elif international_calls == "3":
                    int_fhundred = input("Please E-top up your line with N499 to enjoy benefits under this plan.\n"
                                         "For paper recharge of N500 Dial *605*\n"
                                         "99. Back\n"
                                         "0. Exit\n")
                    if int_fhundred == "99":
                        pass
                    elif int_fhundred == "0":
                        print("Exiting, thank you")
                    else:
                        print("Exiting. Thank you")
                elif international_calls == "4":
                    int_thousand = input("Please E-top up your line with N999 to enjoy benefits under this plan.\n"
                                        "For paper recharge of N1000 Dial *605*\n"
                                        "99. Back\n"
                                        "0. Exit\n")
                    if int_thousand == "99":
                        pass
                    elif int_thousand == "0":
                        print("Exiting, thank you")
                    else:
                        print("Exiting. Thank you")
                elif international_calls == "5":
                    country_list = input("Canada,India, Malaysia, Mongolia, Norway, Puerto Rico, Romania\n"
                                         "99. Back\n"
                                         "0. Exit\n")
                    if country_list == "99":
                        pass
                    elif country_list == "0":
                        print("Exiting, thank you")
                    else:
                        print("invalid")
                elif international_calls == "6":
                    print(" IDD-16 countries pack balance in seconds:\n"
                          "IDD-100:0; IDD-200:0; IDD-500:0; IDD-1000:0 ")
                elif international_calls == "99":
                    pass
                elif international_calls == "0":
                    print("Exiting, thank you")
                else:
                    print("invalid")

            elif voice_data_roaming == "3":
                data_roaming = input("1. N2000 = 300MB 3 Days\n"
                                     "2. N3500 = 600MB 7 Days\n"
                                     "3. N6500 = 1.25GB 15 Days\n"
                                     "4. N15000 = 3GB 30 Days\n"
                                     "5. N30000 = 6GB 180 Days\n"
                                     "6. List of countries & partners\n"
                                     "99. Back\n"
                                     "0. Exit\n")
            elif voice_data_roaming == "99":
                pass
            elif voice_data_roaming == "0":
                print("Exiting, thank you")
            else:
                print("invalid")
        elif data_plans == "6":
            glo_rewards = input("Recharge and win assured cashback, exciting prizes and chance to win up to N100M "
                                "every week:\n" +
                                "1. Opt-in\n" +
                                "2. Opt-out\n" +
                                "99. Back\n" +
                                "0. Exit \n"
                                )
            if glo_rewards == "1":
                print("Dear Customer, You have successfully opted-in for Promo. Keep Recharging, win assured cashback, "
                      "exciting prizes up to N100MnEvery week.")
            elif glo_rewards == "2":
                print("Dear Customer, Thank you for your patronage. You can opt-in again by  dialing *301*8# anytime "
                      "during promo period and start inning gain.")
            elif glo_rewards == "99":
                pass
            elif glo_rewards == "0":
                print("Exiting, thank you.")

        else:
            print("Exiting, thank you")

    elif select_transaction == "2":
        borrow_services = input("Dear Customer, Welcome, you are eligible for N1500\n" +
                                "Reply with: \n" +
                                "1. My BMC Account\n" +
                                "2. Borrow Credit\n" +
                                "3. Borrow Data\n" +
                                "4. Borrow Credit for Others\n" +
                                "5. Borrow Data for Others \n"
                                )
    elif select_transaction == "3":
        recharge = input("Dear Customer, as per NCC directive, the airtime recharge code is now 311.\n" +
                         "To recharge dial *311*RechargePin#.\n" +
                         "Thanks\n" +
                         "99. Back\n" +
                         "0. Exit\n"
                         )
    elif select_transaction == "4":
        data_share = input("1. Share Data\n" +
                           "2. Unshare Data\n" +
                           "3. List of Shared Numbers\n" +
                           "4. Get Data Settings\n" +
                           "5. Manual Configuration Details\n" +
                           "6. Easy Share (Credit Share)\n"
                           "0. Exit"
                           )
    elif select_transaction == "5":
        check_balance = input("1. Main A/C Balance\n" +
                              "2. Bonus A/C Balance\n" +
                              "3. Post Paid A/C Balance: Dial *310#\n" +
                              "99. Back\n" +
                              "0. Exit\n"
                              )
    elif select_transaction == "6":
        print("Dear Customer, your plan has expired and you do not have a data plan. To buy a data plan and continue "
              "browsing visit https://hsi.glo.com or dial *312#")
    elif select_transaction == "7":
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
            bmc = input("Dear ")
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
        elif vas == "0":
            pass
        else:
            print("Invalid")
    elif select_transaction == "8":
        cash_tokens = input("Recharge and win assured cashback, exciting prizes and chance to win up to N100M "
                            "every week:\n" +
                            "1. Opt-in\n" +
                            "2. Opt-out\n" +
                            "99. Back\n" +
                            "0. Exit \n"
                            )
        if cash_tokens == "1":
            print("Dear Customer, You have successfully opted-in for Promo. Keep Recharging, win assured cashback, "
                  "exciting prizes up to N100MnEvery week.")
        elif cash_tokens == "2":
            print("Dear Customer, Thank you for your patronage. You can opt-in again by  dialing *301*8# anytime "
                  "during promo period and start inning gain.")
        elif cash_tokens == "99":
            pass
        elif cash_tokens == "0":
            print("Exiting, thank you.")

        else:
            print("invalid")
    else:
        print("Invalid")


else:
    print("Connection problem or invalid MMI code.")
