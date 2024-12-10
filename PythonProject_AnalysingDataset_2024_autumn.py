import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DrehmalApotheosis_v2.2.1_Dataset.csv', sep=';')

# print(df.head())
# print(df.shape[0])
# print(df.columns)

def Radar(coord_string, radius_string, df):
    coords = coord_string.replace('(', '').replace(')', '').replace(',', '').split(' ')
    if len(coords) == 3:
        coords = [int(coords[0]), int(coords[2])]
    else:
        coords = [int(coords[0]), int(coords[1])]
    if radius_string.split(' ') == '':
        radius = 8000
    else:
        radius = int(radius_string)
    results_counter = 0

    print("Here's what each colour means: ")
    print("Blue - your location")
    print("Red - Mythical Weapon")
    print("Magenta - Legendary Item")
    print("Cyan - Artifact")
    print("Yellow - Artisan Item")
    print("Grey - Fervor Stone")
    print("Green - Trinket")
    print("Black - Book")
    print("Purple - Runic Catalyst")

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    plt.xticks()
    plt.xticks()
    plt.grid(True, linestyle='dotted')

    plt.scatter(coords[0], coords[1], color='blue')

    for name in df.Name:
        name_coords = df[df['Name'] == name]['Coordinates'].iloc[0].replace("['", '').replace("']", '').split("', '")
        name_obtain = (df[df['Name'] == name]['Obtain'].iloc[0].
                       replace('"', "'").replace("['", '').replace("']", '').split("', '"))
        for i in range(len(name_coords)):
            name_coords_i_string = name_coords[i]

            if name_coords_i_string != '#NO_INFO':
                name_coords_i = name_coords_i_string.replace('(', '').replace(')', '').split(', ')
                name_coords_i_xz = [float(name_coords_i[0]), float(name_coords_i[2])]
                name_x = float(name_coords_i[0])
                name_z = float(name_coords_i[2])
                if ((abs(coords[0] - name_coords_i_xz[0]) <= radius)
                        and (abs(coords[1] - name_coords_i_xz[1]) <= radius)):
                    print("Item: " + df[df['Name'] == name]['Name'].iloc[0])

                    print("Class: " + df[df['Name'] == name]['Tag'].iloc[0])

                    print("Can be found at: " + name_coords[i])

                    if len(name_obtain) == len(name_coords):
                        print("How to obtain: " + name_obtain[i] + '\n')
                    else:
                        print("How to obtain: " + df[df['Name'] == name]['Obtain'].iloc[0].
                              replace('"', "'").replace("['", "").replace("']", "") + '\n')

                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Mythical Weapon':
                        plt.scatter(name_x, -name_z, color='red')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Legendary Item':
                        plt.scatter(name_x, -name_z, color='magenta')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Artifact':
                        plt.scatter(name_x, -name_z, color='cyan')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Artisan Item':
                        plt.scatter(name_x, -name_z, color='yellow')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Fervor Stone':
                        plt.scatter(name_x, -name_z, color='grey')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Trinket':
                        plt.scatter(name_x, -name_z, color='green')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Book':
                        plt.scatter(name_x, -name_z, color='black')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Runic Catalyst':
                        plt.scatter(name_x, -name_z, color='purple')

                    results_counter += 1
    if results_counter == 0:
        print("Oh, it seems there's no items nearby...")

    plt.savefig('Radar.png')
    plt.show()


def WorldLocation(df):

    print("Here's what each colour means: ")
    print("Red - Mythical Weapon")
    print("Magenta - Legendary Item")
    print("Cyan - Artifact")
    print("Yellow - Artisan Item")
    print("Grey - Fervor Stone")
    print("Green - Trinket")
    print("Black - Book")
    print("Purple - Runic Catalyst")

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    plt.xticks()
    plt.xticks()
    plt.grid(True, linestyle='dotted')
    for name in df.Name:
        name_coords = df[df['Name'] == name]['Coordinates'].iloc[0].replace("['", '').replace("']", '').split("', '")
        for i in range(len(name_coords)):
            name_coords_i_string = name_coords[i]
            if name_coords_i_string != '#NO_INFO':
                name_coords_i = name_coords_i_string.replace('(', '').replace(')', '').split(', ')
                name_x = float(name_coords_i[0])
                name_z = float(name_coords_i[2])
                if abs(name_x) < 10000:
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Mythical Weapon':
                        plt.scatter(name_x, -name_z, color='red')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Legendary Item':
                        plt.scatter(name_x, -name_z, color='magenta')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Artifact':
                        plt.scatter(name_x, -name_z, color='cyan')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Artisan Item':
                        plt.scatter(name_x, -name_z, color='yellow')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Fervor Stone':
                        plt.scatter(name_x, -name_z, color='grey')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Trinket':
                        plt.scatter(name_x, -name_z, color='green')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Book':
                        plt.scatter(name_x, -name_z, color='black')
                    if df[df['Name'] == name]['Tag'].iloc[0] == 'Runic Catalyst':
                        plt.scatter(name_x, -name_z, color='purple')


    plt.savefig('ItemDistribution.png')
    plt.show()

def SuchItems(search_string, df):
    results_counter = 0
    search_string = search_string.lower()
    for name in df.Name:
        if ((name.lower().count(search_string) > 0)
                or ((df[df['Name'] == name]['Tag']).iloc[0].lower().count(search_string) > 0)
                or ((df[df['Name'] == name]['Base Item']).iloc[0].lower().count(search_string) > 0)):
            print("Item: " + df[df['Name'] == name]['Name'].iloc[0])

            print("Class: " + df[df['Name'] == name]['Tag'].iloc[0])

            Coordinates = df[df['Name'] == name]['Coordinates'].iloc[0]
            if '#NO_INFO' not in Coordinates:
                print("Can be found at: " + Coordinates.replace(']', '').replace('[', '').replace("'", ""))

            Attack_Damage = df[df['Name'] == name]['Attack Damage'].iloc[0]
            if Attack_Damage != '#NO_INFO':
                print("Attack Damage: " + Attack_Damage)

            Attack_Speed = df[df['Name'] == name]['Attack Speed'].iloc[0]
            if Attack_Speed != '#NO_INFO':
                print("Attack Speed: " + Attack_Speed)

            Ability = df[df['Name'] == name]['Ability'].iloc[0]
            if Ability != '#NO_INFO':
                print("Ability: " + Ability)

            Armor = df[df['Name'] == name]['Armor'].iloc[0]
            if Armor != '#NO_INFO':
                print("Armor: " + Armor)

            Armor_Toughness = df[df['Name'] == name]['Armor Toughness'].iloc[0]
            if Armor_Toughness != '#NO_INFO':
                print("Armor Toughness: " + Armor_Toughness)

            Enchantments = df[df['Name'] == name]['Enchantments'].iloc[0]
            if '#NO_INFO' not in Enchantments:
                print("Enchantments: " + Enchantments.replace(']', '').replace('[', '').replace("'", ""))

            Bonus_Stats = df[df['Name'] == name]['Bonus Stats'].iloc[0]
            if '#NO_INFO' not in Bonus_Stats:
                print("Bonus Stats: " + Bonus_Stats.replace(']', '').replace('[', '').replace("'", ""))

            print("How to obtain: " + df[df['Name'] == name]['Obtain'].iloc[0].
                  replace('"', "'").replace("'", "").replace("[","").replace("]", "") + '\n')

            results_counter += 1
    if results_counter == 0:
        print("Sorry, there's no such items...  :(")

def Item_Tag_Coord_Obtain(search_string, df):
    results_counter = 0
    for name in df.Name:
        if name.lower().count(search_string.lower()) > 0:
            print("Item: " + df[df['Name'] == name]['Name'].iloc[0])

            print("Class: " + df[df['Name'] == name]['Tag'].iloc[0])

            Coordinates = df[df['Name'] == name]['Coordinates'].iloc[0]
            if Coordinates != ['#NO_INFO']:
                print("Can be found at: " + Coordinates.replace("'", "").replace("[","").replace("]", ""))

            print("How to obtain: " + df[df['Name'] == name]['Obtain'].iloc[0].
                  replace('"', "'").replace("'", "").replace("[","").replace("]", "") + '\n')

            results_counter += 1
    if results_counter == 0:
        print("Sorry, there's no such items...  :(")

def Helper(option_number):
    if option_number == 1:
        print("Please, input your coordinates")
        coord_string = str(input())
        print("Please, input the radius of search")
        radius_string = str(input())
        print("Searching..." + "\n")
        Radar(coord_string, radius_string, df)
        return
    if option_number == 2:
        print("Here you are!  :)" + "\n")
        WorldLocation(df)
        return
    if option_number == 3:
        print("Please, input the item or item's type you're looking for")
        search_string = str(input())
        print("Searching..." + "\n")
        SuchItems(search_string, df)
        return
    if option_number == 4:
        print("Please, input the item or item's type you're looking for")
        search_string = str(input())
        print("Searching..." + "\n")
        Item_Tag_Coord_Obtain(search_string, df)
        return
    else:
        print("Sorry, but there is no such function...  :(")


print("This is your assistant to explore the overworld in the Drehmal Apotheosis v2.2.1 project.")
print("What function you would like to use?")
print("1. Radar ")
print("(shows all the items nearby, you'd be required to input your coordinates and the radius of the search)")
print("2. World Location")
print("(shows all item's locations at the world map)")
print("3. Find the item")
print("(input the item or type of weapon/armor you want to find, you'll be given a table of such items)")
print("4. Where's this item? How to get it?")
print("(You give me the item, I give you its coordinates and the way to have, a great deal, don't you think so?)")
print("\n")
print("Please, write the number of the option you chose")
option_number = int(input())
Helper(option_number)