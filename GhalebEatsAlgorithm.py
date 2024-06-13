# Ghaleb Eats

import random

previously_recommended = set()

Locations = {
    "Mivida": {
        "BRGR": ["Original Double", "J-Bomb Double", "CHKN BRGR", "Chicken Bites", "Cheese Fries", "Regular Fries"],
        "Nathan's": ["Chicken Combo Offer","Chicken Tenders 5pcs (Buffalo/Original)","Bacon Cheddar Single",
                     "Southern Chicken Single","Buffalo Chicken Single","Original Fries"],
        "Jimmy's Pizza": ["Margherita","Pepperoni","Buffalo Chicken","BBQ Chicken"]
    },
    "Point 90": {
        "Labash": ["Chicken Strips (Breast), kg dependant on group size"],
        "Lord of the wings": ["6 piece Boneless Sweet Chili","6 piece Boneless Garlic Parmesean"],
        "Sizzler": ["Chicken Pomodoro Pasta","Chicken Alfredo Pasta","Penne Arabiata",
                    "Grilled Chicken + Creamy Pepper", "Grilled Chicken + Hickory Smoked BBQ",
                    "Grilled Chicken + Mixed Cheese", "Sweet Chilli Chicken", "Country Chicken Parmesan"]
    },
    "Cairo Festival City Mall": {
        "Labash": ["Chicken Strips (Breast), kg dependant on group size"],
        "Friday's": ["Buffalo Chicken Quesadilla","Cheese Nachos"],
        "I-Hop": ["Chicken and Waffles", "The Classic Burrito", "Hashbrowns"],
        "Mahraja": ["Butter Chicen and Rice"],
        "Hameed": ["Spicy Maple Glazed Bacon Burger", "Original Maple Glazed Sandwich", "Spicy and Crunchy Sandwich",
                   "Chili-Butter Glazed", "Large French Fries"]
    },
    "Open Air Mall": {
        "Ted's": ["Pepperoni Piza","Alfredo Pasta (no mushroom)","Arabiata Pasta","Lemon Chicken Plate"],
        "Hameed": ["Spicy Maple Glazed Bacon Burger", "Original Maple Glazed Sandwich", "Spicy and Crunchy Sandwich",
                   "Chili-Butter Glazed", "Large French Fries"],
        "Sizzler": ["Chicken Pomodoro Pasta","Chicken Alfredo Pasta","Penne Arabiata",
                    "Grilled Chicken + Creamy Pepper", "Grilled Chicken + Hickory Smoked BBQ",
                    "Grilled Chicken + Mixed Cheese", "Sweet Chilli Chicken", "Country Chicken Parmesan"]
    },
    "Arkan": {
        "El Beiruti":["Chicken Shawarma Sandwich","Batata Hara"],
        "Caracas": ["Shish Tawouk","Batata Hara"],
        "Mistika": ["Shish Tawouk and Fries","Chesse Sambousak"],
        "Bitter Sweet": ["Pepperoni Pizza","Linguine Pasta + Creamy White Sauce + Grilled Chicken Slices + Parmesan",
                         "Linguine Pasta + Italian Tomato Sauce + Grilled Chicken Slices + Parmesan"],
        "Casatalia": ["The 400 degree Garlic Cheese","Brie Garlic Knots","Pepperoni Pizza","Penne Arabiata",
                      "Grilled Boneless Chicken","Chicken Escalope & Truffle Mac N'Cheese"],
        "Willow's": ["Chicken Alfredo Pasta","Neapolitan Pasta","Chicken Kiev","Chicken Roulade"]
    },
    "Park Strt": {
        "BRGR": ["Original Double", "J-Bomb Double", "CHKN BRGR", "Chicken Bites", "Cheese Fries", "Regular Fries"],
        "Qahwa": ["Chicken Quesadillas","Chicken Coriander Sandwich","Crispy Chicken Sub Sandwich"],
        "Bebabel": ["Cheese Rolls","Chilli Potatoes","Sambousek","Cheese Manakeesh","Shish Tawook","Mixed Grill"],
        "Em Sherif Cafe": ["Cheese Manakish","Lahme bi Aageen","Batata Harra","Tawouk","Chicken Shawarma"]
    },
    "Mall Of Arabia": {
        "BRGR": ["Original Double", "J-Bomb Double", "CHKN BRGR", "Chicken Bites", "Cheese Fries", "Regular Fries"],
        "Caracas": ["Shish Tawouk","Batata Hara"],
        "Mista": ["Pepperoni Pizza","Arabiata Pasta","Al Pomodoro Pasta","Chicekn Cardon Bleu Plate",
                  "Chicken Parmesean Plate"],
        "Lado's Pizza": ["Margerita Pizza","Cheesy Pizza","Pepperoni Pizza"]
    },
    "District 5": {
        "Mo Bistro": ["Mongolian Chicken","Chicken Lemon Spaghetti Pasta","Penne Pomodoro Pasta",
                      "Parmesean Chicken Dish","Camembert Alamo"],
        "Mista": ["Pepperoni Pizza","Arabiata Pasta","Al Pomodoro Pasta","Chicekn Cardon Bleu Plate",
                  "Chicken Parmesean Plate"],
        "Don Eatery": ["Teriyaki Fries","Chicken Katsu Bao","Chicken Sesame Noodles"],
        "Howlin Bird": ["5 Jumbo Chicken Tenders","3 Jumbo Chicken Tenders","Nuggies","Cheese Fries","Regular Fries",
                        "Mac and Cheese"]
    },
    "Walk Of Cairo": {
        "Caracas": ["Shish Tawouk","Batata Hara"],
        "Seecoz": ["Chicken Gyro","Buffalo Fried Chicken Souvlaki","Halloumi Fries","Spicy Feta Fries"]
    },
    "Capital Business Park": {
        "Mo Bistro": ["Mongolian Chicken","Chicken Lemon Spaghetti Pasta","Penne Pomodoro Pasta",
                      "Parmesean Chicken Dish","Camembert Alamo"]
    }
}

Cravings = {
    "Fried Chicken": {
        "Nathan's": ["Chicken Combo Offer","Chicken Tenders 5pcs (Buffalo/Original)","Southern Chicken Single",
                     "Buffalo Chicken Single"],
        "Labash": ["Chicken Strips (Breast), kg dependant on group size"],
        "Howlin Bird": ["5 Jumbo Chicken Tenders","3 Jumbo Chicken Tenders","Nuggies"],
        "Chicken Worx": ["5 pcs + Worx Sauce"],
        "Cripsy Hen": ["The Loaded Bundle Offer","The Joker Bundle Offer","Tenders 4 piece meal"],
        "Willy's Kitchen": ["Buffalo Nacho Chicken Sandwich"],
        "Kak Squad": ["Dip meal 3 pieces + Kak sauce","Dip meal 3 pieces + Thai Chili sauce","Chicken Popcorn"]
    },
    "Burgers": {
        "BRGR": ["Original Double", "J-Bomb Double", "CHKN BRGR", "Chicken Bites", "Cheese Fries", "Regular Fries"],
        "Hameed": ["Spicy Maple Glazed Bacon Burger", "Original Maple Glazed Sandwich", "Spicy and Crunchy Sandwich",
                   "Chili-Butter Glazed", "Large French Fries"],
        "Willy's Kitchen": ["Chili Chili Burger Sandwich","Original Cheeseburger No veggies",
                            "Wily's Nacho Chicken Sandwich"]
    },
    "Pizza": {
        "Jimmy's Pizza": ["Margherita","Pepperoni","Buffalo Chicken","BBQ Chicken"],
        "Lado's Pizza": ["Margerita Pizza","Cheesy Pizza","Pepperoni Pizza"],
        "Papa John's": ["Pepperoni Pizza Rolls","Pepperoni Pizza","Chicken Barbeque Pizza"],
        "Domino's": ["Pepproni"],
        "Ted's": ["Pepperoni Pizza"]
    },
    "Pasta": {
        "Ted's": ["Alfredo Pasta (no mushroom)","Arabiata Pasta"],
        "Bitter Sweet": ["Pepperoni Pizza","Linguine Pasta + Creamy White Sauce + Grilled Chicken Slices + Parmesan",
                         "Linguine Pasta + Italian Tomato Sauce + Grilled Chicken Slices + Parmesan"],
        "Willow's": ["Chicken Alfredo Pasta","Neapolitan Pasta"],
        "Mista":["Arabiata Pasta","Al Pomodoro Pasta"],
        "Mo Bistro": ["Chicken Lemon Spaghetti Pasta","Penne Pomodoro Pasta"]
    },
    "Shawarma": {
        "Ibn el Sham": ["Chicken Shawarma"],
        "Brocar": ["Chicken Shawarma"],
        "Shawrma street": ["Chicken Shawarma"],
        "El Beiruti": ["Chicken Shawarma"],
        "Em Sherif Cafe": ["Chicken Shawarma"],
        "Shawarma el Reem": ["Chicken Shawarma"]
    },
    "Ramen": {
        "Don Eatery": ["Chicken Sesame Noodles"]
    }
}

All_Food_Outlets = {
    "BRGR": ["Original Double", "J-Bomb Double", "CHKN BRGR", "Chicken Bites", "Cheese Fries", "Regular Fries"],

    "Nathan's": ["Chicken Combo Offer","Chicken Tenders 5pcs (Buffalo/Original)","Bacon Cheddar Single",
                     "Southern Chicken Single","Buffalo Chicken Single","Original Fries"],

    "Jimmy's Pizza": ["Margherita","Pepperoni","Buffalo Chicken","BBQ Chicken"],

    "Labash": ["Chicken Strips (Breast), kg dependant on group size"],

    "Lord of the wings": ["6 piece Boneless Sweet Chili","6 piece Boneless Garlic Parmesean"],

    "Sizzler": ["Chicken Pomodoro Pasta","Chicken Alfredo Pasta","Penne Arabiata",
                "Grilled Chicken + Creamy Pepper", "Grilled Chicken + Hickory Smoked BBQ",
                "Grilled Chicken + Mixed Cheese", "Sweet Chilli Chicken", "Country Chicken Parmesan"],

    "Friday's": ["Buffalo Chicken Quesadilla","Cheese Nachos"],

    "I-Hop": ["Chicken and Waffles", "The Classic Burrito", "Hashbrowns"],

    "Mahraja": ["Butter Chicen and Rice"],

    "Hameed": ["Spicy Maple Glazed Bacon Burger", "Original Maple Glazed Sandwich", "Spicy and Crunchy Sandwich",
                "Chili-Butter Glazed", "Large French Fries"],

    "El Beiruti":["Chicken Shawarma Sandwich","Batata Hara"],

    "Caracas": ["Shish Tawouk","Batata Hara"],

    "Mistika": ["Shish Tawouk and Fries","Chesse Sambousak"],

    "Bitter Sweet": ["Pepperoni Pizza","Linguine Pasta + Creamy White Sauce + Grilled Chicken Slices + Parmesan",
                    "Linguine Pasta + Italian Tomato Sauce + Grilled Chicken Slices + Parmesan"],

    "Casatalia": ["The 400 degree Garlic Cheese","Brie Garlic Knots","Pepperoni Pizza","Penne Arabiata",
                  "Grilled Boneless Chicken","Chicken Escalope & Truffle Mac N'Cheese"],

    "Willow's": ["Chicken Alfredo Pasta","Neapolitan Pasta","Chicken Kiev","Chicken Roulade"],

    "Qahwa": ["Chicken Quesadillas","Chicken Coriander Sandwich","Crispy Chicken Sub Sandwich"],

    "Bebabel": ["Cheese Rolls","Chilli Potatoes","Sambousek","Cheese Manakeesh","Shish Tawook","Mixed Grill"],

    "Em Sherif Cafe": ["Cheese Manakish","Lahme bi Aageen","Batata Harra","Tawouk","Chicken Shawarma"],

    "Mista": ["Pepperoni Pizza","Arabiata Pasta","Al Pomodoro Pasta","Chicekn Cardon Bleu Plate",
              "Chicken Parmesean Plate"],

    "Lado's Pizza": ["Margerita Pizza","Cheesy Pizza","Pepperoni Pizza"],

    "Mo Bistro": ["Mongolian Chicken","Chicken Lemon Spaghetti Pasta","Penne Pomodoro Pasta",
                "Parmesean Chicken Dish","Camembert Alamo"],

    "Don Eatery": ["Teriyaki Fries","Chicken Katsu Bao","Chicken Sesame Noodles"],

    "Howlin Bird": ["5 Jumbo Chicken Tenders","3 Jumbo Chicken Tenders","Nuggies","Cheese Fries","Regular Fries",
                    "Mac and Cheese"],

    "Seecoz": ["Chicken Gyro","Buffalo Fried Chicken Souvlaki","Halloumi Fries","Spicy Feta Fries"],

    "Chicken Worx": ["5 pcs + Worx Sauce"],

    "Cripsy Hen": ["The Loaded Bundle Offer","The Joker Bundle Offer","Tenders 4 piece meal"],

    "Willy's Kitchen": ["Chili Chili Burger Sandwich","Original Cheeseburger No veggies",
                       "Wily's Nacho Chicken Sandwich","Buffalo Nacho Chicken Sandwich"],

    "Papa John's": ["Pepperoni Pizza Rolls","Pepperoni Pizza","Chicken Barbeque Pizza"],

    "Domino's": ["Pepproni"],

    "Ibn el Sham": ["Chicken Shawarma"],

    "Brocar": ["Chicken Shawarma"],

    "Shawrma street": ["Chicken Shawarma"],

    "Shawarma el Reem": ["Chicken Shawarma"],

    "Kak Squad": ["Dip meal 3 pieces + Kak sauce","Dip meal 3 pieces + Thai Chili sauce","Chicken Popcorn"],

    "Andrea": ["Nos Farkha Makhleya Sudoor","Shish Tawook + Fries","wara2 3einab"]
}

def welcome_message():
    print("Welcome to Ghaleb Eats! I know you're hungry, don't worry I'll help you decide what to order!")
def rand_select_from_locations(location):
    global previously_recommended
    remaining_options = []

    for restaurant, menu_items in Locations[location].items():
        for item in menu_items:
            if (restaurant, item) not in previously_recommended:
                   remaining_options.append((restaurant, item))

    if remaining_options:
        recommendation = random.choice(remaining_options)
        previously_recommended.add(recommendation)
        print(f"{recommendation[1]} from {recommendation[0]}")
    else:
        print("You're hopeless there are no more options, I hope you starve <3")
        exit

''' restaurant = random.choice(list(Locations[location].keys()))
   menu_item = random.choice(Locations[location][restaurant])
   print(f"{menu_item}"f" from {restaurant}") '''

def list_from_locations(location):
    for restaurant, menu_items in Locations[location].items():
        #print(f"- {restaurant} : {', '.join(menu_items)}")
        print(f"You like: {', '.join(menu_items)} from {restaurant}")
def rand_select_from_cravings(craving):
    global previously_recommended
    remaining_options = []

    for restaurant, menu_items in Cravings[craving].items():
        for item in menu_items:
            if (restaurant, item) not in previously_recommended:
                remaining_options.append((restaurant, item))

    if remaining_options:
        recommendation = random.choice(remaining_options)
        previously_recommended.add(recommendation)
        print(f"{recommendation[1]} from {recommendation[0]}")
    else:
        print("You're hopeless there are no more options, I hope you starve <3")
        exit

    '''restaurant = random.choice(list(Cravings[craving].keys()))
    menu_item = random.choice(Cravings[craving][restaurant])
    print(f"{menu_item} from {restaurant}")'''

def list_from_cravings(craving):
    for restaurant, menu_items in Cravings[craving].items():
        #print(f"- {restaurant} : {', '.join(menu_items)}")
        print(f"You'll like: {', '.join(menu_items)} from {restaurant}")

def recommend_from_restaurant(desired_restaurant):
    global previously_recommended
    remaining_options = []

    if desired_restaurant in All_Food_Outlets:
        for item in All_Food_Outlets[desired_restaurant]:
            if (desired_restaurant, item) not in previously_recommended:
                remaining_options.append(item)

        if remaining_options:
            recommendation = random.choice(remaining_options)
            previously_recommended.add(recommendation)
            print(f"You'd like: {recommendation}.")
        else:
            print("You're hopeless there are no more options, I hope you starve <3")
            exit

def list_from_restaurant(desired_restaurant):
    options = All_Food_Outlets[desired_restaurant]
    print(f"You like: {', '.join(options)} ")



def indecisiveSelect():
    global previously_recommended
    remaining_options = []

    for restaurant, menu_items in All_Food_Outlets.items():
        for item in menu_items:
            if (restaurant, item) not in previously_recommended:
                remaining_options.append((restaurant, item))

    if remaining_options:
        recommendation = random.choice(remaining_options)
        previously_recommended.add(recommendation)
        print(f"You'd like {recommendation[1]} from {recommendation[0]}")
    else:
        print("You're hopeless there are no more options, I hope you starve <3")
        exit

    '''restaurant = random.choice(list(All_Food_Outlets.keys()))
    menu_item = random.choice(All_Food_Outlets[restaurant])
    print(f"You'd like {menu_item} from {restaurant}")'''



def main():
    welcome_message()
    location_known = input("Do you know where you're going to eat?: ").lower()
    if location_known == "yes" or location_known == "y":
        while True:
            location = input("Please enter your intended destination: ").title()
            if location in Locations:
                decision = input("Would you like me to recommend select a restaurant and menu item for you?: ")
                if decision.lower() in ["yes", "y"]:
                    rand_select_from_locations(location)
                    while True:
                        satisfied = input("Are you satisfied with the recommendation? ")
                        if satisfied.lower() in ["yes", "y"]:
                            break
                        else:
                            rand_select_from_locations(location)
                elif decision.lower() in ["no", "n"]:
                    list_from_locations(location)
                break
            else:
             print("Invalid location, please try again.")

    elif location_known == "No" or "NO" or "no" or "n" or "N":
        restaurant_in_mind = input("Do you have a specifc restaurant in mind? ")
        if restaurant_in_mind.lower() in ["yes","y"]:
            while True:
                desired_restaurant = input("Enter the restaurant you would like to order from: ")
                if desired_restaurant in All_Food_Outlets:
                    decision = input("Would you like me to recommend a menu item for you? ")
                    if decision.lower() in ["yes", "y"]:
                        recommend_from_restaurant(desired_restaurant)
                        while True:
                            satisfied = input("Are you satisfied with the recommendation? ")
                            if satisfied.lower() in ["yes", "y"]:
                                break
                            else:
                                recommend_from_restaurant(desired_restaurant)
                    elif decision.lower() in ["No","N"]:
                        list_from_restaurant(desired_restaurant)
                        break
                else:
                    print("Invalid restaurant, please try again. ")

        elif restaurant_in_mind.lower() in ["No","N"]:
            craving_status = input("Are you experiencing any cravings? ").capitalize()
            if craving_status == "Yes" or craving_status == "Y":
                while True:
                    craving = input("Enter one of the following cravings: Fried Chicken - Burgers - Pizza - Pasta -"
                                    + " Shawarma - Ramen ").title()
                    if craving in Cravings:
                        decision = input("Would you like me to recommend a restaurant and menu item for you? ")
                        if decision.lower() in ["yes", "y"]:
                            rand_select_from_cravings(craving)
                            while True:
                                satisfied = input("Are you satisfied with the recommendation? ")
                                if satisfied.lower() in ["yes", "y"]:
                                    break
                                else:
                                    rand_select_from_cravings(craving)

                        elif decision.lower() in ["no", "n"]:
                            list_from_cravings(craving)
                        break

                    else:
                        print("Invalid Craving, please try again.")
            elif craving_status == "No" or craving_status == "N":
                feeling_indecisive = input("Are you feeling indecisive? ").lower()
                if feeling_indecisive == "yes" or feeling_indecisive == "y":
                    indecisiveSelect()
                    while True:
                        satisfied = input("Are you satisfied with the recommendation? ")
                        if satisfied.lower() in ["yes", "y"]:
                            break
                        else:
                            indecisiveSelect()
                else:
                    print("you're hopeless, I hope you starve <3")
                    exit 

if __name__ == "__main__":
    main()