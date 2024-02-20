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
        elif data_plans == "6":
            glo_rewards = input("Recharge and win assured cashback, exciting prizes and chance to win up to N100M "
                                "every week:\n" +
                                "1. Opt-in\n" +
                                "2. Opt-out\n" +
                                "99. Back\n" +
                                "0. Exit \n"
                                )
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
                pass
            elif gaming_services == "99":
                pass
            elif gaming_services == "0":
                pass
            else:
                print("Invalid MMI code")
        elif vas == "2":
            pass
        elif vas == "3":
            pass
        elif vas == "4":
            pass
        elif vas == "5":
            pass
        elif vas == "6":
            pass
        elif vas == "7":
            pass
        elif vas == "8":
            pass
        elif vas == "9":
            pass
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
            print("Dear Customer, You have successfully opted-in for Promo. Kepp Recharging, win assured cashback, "
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
