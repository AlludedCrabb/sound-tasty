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
        'granules', 'boiling', 'yolk', 'coloring', 'pinch', 'a', 'blender',
        'fine', 'which', 'extralarge', 'use', 'will', 'make', 'garnish',
        'barely', 'moistened', 'about', 'right', 'before', 'serving', 'mix',
        
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

def lower_list_strings(list_object):
        
    low_words = []
    for word in list_object:
        low_words.append(word.lower())
    return low_words


def ingred_series_compare(ingredient_series, compare_list):
    """Check if each list in a series of lists contains specific words"""

    indices_of_recipes = []
    for k, j in enumerate(ingredient_series):
        for i in j:
            if i in compare_list:
                indices_of_recipes.append(k)
    return indices_of_recipes


def sound_tasty(word_vec_model,
                ingred_series,
                title_series,
                ingred_1=None,
                ingred_2=None,
                ingred_3=None,
                ingred_4=None,
                adventure="low"):
    """Recommend recipes based on ingredient similarity"""
    import random

    ing_1 = input()
    ing_2 = input()
    ing_3 = input()
    ing_4 = input()
    ingred_input = [x.lower() for x in [ing_1, ing_2, ing_3, ing_4] if x != '']
    
    try:
        ingre_list = parse_ingred_tuples(word_vec_model.wv.most_similar(
            positive=(ingred_input),
            topn=100000)
            )

        user_input = adventure.lower()

        if user_input == "low":
            comp_list = ingre_list[:20]

        elif user_input == "medium":
            middle = round(len(ingre_list)/2)
            comp_list = ingre_list[middle:(middle + 20)]

        elif user_input == "high":
            comp_list = ingre_list[-20:]

        else:
            comp_list = ingre_list[:20]

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

        result = []

        rec_dict = {"Title" :title_series[high_value[0]],
                    "Ingreds" : ingred_series[high_value[0]]}
        result.append(rec_dict)

        for i in range(len(runners_up)):
            rec_dict = {}
            rec_dict["Title"] = title_series[runners_up[i][0]]
            rec_dict["Ingreds"] = ingred_series[runners_up[i][0]]
            result.append(rec_dict)

        return result

    except KeyError as x:
        return x
