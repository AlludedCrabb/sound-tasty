def split_words_in_str_lst_items(string_list):
    """Splits a list of sentences into a
    list with lists of individual words as values"""

    split_words = []
    for item in string_list:
        split_words.append(item.split())
    return split_words


def lst_clean_cooking_stop_words(string_list):
    """Remove measurement and cooking words,
    leaving only ingredients"""

    cooking_stop_words = [
        'canned', 'cans', 'drained', 'and', 'halved', 'cup', 'cups',
        'teaspoon', 'tablespoon', 'teaspoons', 'tablespoons',
        'finely', 'freshly', 'fresh', 'thickcut', 'to', 'taste',
        'grated', 'cut', 'into', 'wedges', 'pounds', 'unpeeled', 'large',
        'minced', 'slice', 'slices', 'sliced', 'thick-cut', 'cut',
        'crosswise', 'pieces', 'toothpicks', 'low-fat', 'chopped', 'or',
        'taste', 'cooked', 'dry', 'shredded', 'beaten', 'dried', 'melted',
        'stems', 'removed', 'diced', 'ounce', 'ounces', 'packages',
        'softened', 'such', 'RedHot®', 'RedHot', 'Franks', "Frank's",
        'crumbled', 'Old', 'Bay®', 'Bay', 'pinch', 'for', 'garnish', 'slice',
        'slices', 'needed', 'inch', 'cubes', 'cooking', 'spray', 'ground',
        'rotisserie', 'lowfat', 'as', 'quarteres', 'cloves', 'more', 'can',
        'package', 'frozen', 'thawed', 'packet', 'reducedfat', 'Knorr',
        'container', 'pound', 'peeled', 'deveined', 'seeded', 'ripe',
        'English', 'juiced', 'plus', 'more', 'Hass', 'cubed', 'Mexicanstyle',
        'hearts', 'prepared', 'party', 'pitted', 'mashed',
        'roma', 'optional', 'chunk', 'Hot', 'bunch', 'cleaned', 'box',
        'chickenflavored', 'Golden', 'delicious', 'cored', 'any', 'flavor',
        'flavored', 'whole', 'allpurpose', 'all', 'purpose', 'deep', 'frying',
        'dash', 'packed', 'in', 'French', 'jar', 'small', 'head', 'little',
        'smokie', 'seasoned', 'Boston', 'Bibb', 'leaves', 'lean', 'pickled',
        'Asian', 'dark', 'flaked', 'rolled', 'packed', 'jellied',
        'thirds', 'with', 'attached', 'skewers', 'skinless', 'boneless',
        'half', 'kernels', 'rinsed', 'quart', 'quarts', 'kernel',
        'Italianstyle', 'unpopped', 'lightly', 'coating', 'SAUCE',
        'lengthwise', 'miniature', 'semisweet', 'rinsed', 'round',
        'squeezed', 'stewed', 'raw', 'the', 'liquid', 'reserved', 'medium',
        'instant', 'solid', 'pack', 'refrigerated', 'halves', 'distilled',
        'loaf', 'extra', 'virgin', 'crushed', 'kosher', 'toasted', 'buttery',
        'TM', 'panko', 'Japanese', 'regular', 'bottle', 'bottles', 'thin',
        'peel', 'paper', 'thick', 'circles', 'unbleached',
        'breast', 'breasts', 'wings', 'strips', 'jumbo', 'giant', 'chunks',
        'quickcooking', 'sweetened', 'flakes', 'Ranchstyle', 'snipped',
        'food', 'ROTEL', 'Italian', 'sticks', 'stick', 'crescent', 'thinly',
        'boiled', 'Genoa', 'roasted', 'thin', 'extrasharp', 'pressed',
        'sifted', 'split', 'tips', 'discarded', 'mini', 'deli', 'drain',
        'reserve', 'diameter', 'Greek', 'Thai', 'drops', 'square', 'crusty',
        'American', 'selfrising', 'imitation', 'Wings', 'apart', 'at',
        'joints', 'wing', 'tips', 'discarded', 'parts',
        'tops', 'seperated', 'blend', 'coarsely', 'sweet', 'stalk', 'heads',
        'husked', 'divided', 'pats', 'unsalted', 'active', 'warm', 'sea',
        'separated', 'herb', 'overripe', 'degrees', 'F', 'C', 'room',
        'temperature', 'machine', 'very', 'pint', 'puree', 'coarse',
        'envelopes', 'lukewarm', 'creamstyle', 'unsweetened',
        'lite', 'of', 'chilled', 'freezer', 'cold', 'brushing', 'nonfat',
        'squares', 'tails', 'thigh', 'quarters', 'Masterpiece', 'KC', 'from',
        'El', 'Paso', 'bulk', 'Hunts', 'Roma', 'light', 'fluid', 'lagerstyle',
        'stalks', 'quartered', 'undrained', 'drained', 'Tony', 'Chacheres',
        'lump', 'uncooked', 'cube', 'bits', 'hair', 'angel', 'trimmed',
        'stew', 'spaghetti', 'brisket', 'bitesized', 'matchstick', 'Chobani',
        'unbaked', 'crust', 'torn', 'bonein', 'pounded', 'bitesize',
        'granules', 'boiling', 'yolk', 'coloring',
    ]

    cleaned_items = []
    for item_string in string_list:
        for word in item_string:
            if word not in cooking_stop_words:

                cleaned_items.append(word)
    return cleaned_items


def lst_strip_numbers_and_punc(string_list):
    """Remove numbers and punctuation from a list of strings"""

    import re

    num_removed = []
    for x in string_list:
        current_string = re.sub("\d+", "", x)
        current_string = re.sub(r'[^\w\s]', '', current_string)

        num_removed.append(current_string)
    return num_removed


def clean_ingredients(string_list):
    """Take in a list of strings, strip it of numbers and punctuation,
    then split it into individual words, finally remove non-ingredient words"""

    stage_1 = lst_strip_numbers_and_punc(string_list)
    stage_2 = split_words_in_str_lst_items(stage_1)
    stage_3 = lst_clean_cooking_stop_words(stage_2)
    return stage_3


def parse_ingred_tuples(tupp_list):
    """Pull the first value from a list of tuples"""

    sim_ingreds = []
    for i in range(len(tupp_list)):
        sim_ingreds.append(tupp_list[i][0])
    return sim_ingreds


def ingred_series_compare(ingredient_series, compare_list):
    """Check if each list in a series of lists contains specific words"""

    indices_of_recipes = []
    for k, j in enumerate(ingredient_series):
        for i in j:
            if i in compare_list:
                indices_of_recipes.append(k)
    return indices_of_recipes


def sound_tasty(word_vec_model, ingred_series, title_series):
    """Recommend recipes based on ingredient similarity"""
    import random

    try:
        ingre_list = parse_ingred_tuples(word_vec_model.wv.most_similar(
            positive=[input('Choose an ingredient: ').lower(),
                      input('Choose another: ').lower(),
                      input('And another: ').lower(),
                      input('Last one: ').lower()],
            topn=100000)
            )

        user_input = input("""How adventurous are you feeling?
            low, medium, or high? """)
        print('\n')

        if user_input == "low":
            comp_list = ingre_list[:20]
            print("I'll get you food similar to what you're used too")
        elif user_input == "medium":
            middle = round(len(ingre_list)/2)
            comp_list = ingre_list[middle : (middle + 20)]

            print("I'll get you food sort of like what you're used too")
        elif user_input == "high":
            comp_list = ingre_list[-20:]
            print("I'll get food pretty different from what you're used too")
        else:
            print("that's not an option: defaulting to 'low' ")
            comp_list = ingre_list[:20]

        print('\n\n\n',
              'Ingredients like yours:',
              '\n\n',
              comp_list)

        count_me = ingred_series_compare(ingred_series, comp_list)

        ingred_count_dict = {i: count_me.count(i) for i in count_me}

        high_value = (0, 0)
        for x in ingred_count_dict.keys():
            if ingred_count_dict[x] > high_value[1]:
                high_value = (x, ingred_count_dict[x])

        runners_up = []

        for x in ingred_count_dict.keys():
            if (ingred_count_dict[x] == high_value[1] or
                    ingred_count_dict[x] == (high_value[1] - 1)):
                if x is not high_value[0]:
                    runners_up.append((x, ingred_count_dict[x]))

        responses = ["Not good enough hmm? let me try again.",
                     "You're picky aren't you?",
                     "It sounds like you already know what you want",
                     "Are you serious? gosh... fine!",
                     "Mmmm, you look tasty",
                     "Any objections to eating brains?",
                     "You could always order a pizza.",
                     "I've heard interest rates are on the move. Thoughts?",
                     "Don't skip leg day.",
                     "YOU CAN'T HANDLE THE TRUTH!",
                     "Maybe a churro? Who doesn't love churros?",
                     "I've got a dark and mysterious past.",
                     "In another life, they called me... Tim"]

        print('\n\n',
              "How about? ",
              "\n\n",
              title_series[high_value[0]],
              '\n\n',
              ingred_series[high_value[0]],
              '\n\n\n\n')
        if input('Sound tasty? yes/no: ') == "yes":
            pass
        else:
            print('\n\n',
                  "Fine, I'll find you something else. You're welcome.",
                  '\n\n')
            if len(runners_up) == 0:
                print("I got nothing.")
            for i in range(len(runners_up)):
                print('\n\n',
                      "How about? "
                      '\n\n',
                      title_series[runners_up[i][0]],
                      '\n\n',
                      ingred_series[runners_up[i][0]],
                      '\n\n\n\n')

                if input('Sound tasty? yes/no: ') == "yes":
                    break
                else:
                    print('\n\n')
                    choice = random.choice(responses)
                    print(choice)

    except KeyError:
        print('Ingredient not recognized... sorry :(')
