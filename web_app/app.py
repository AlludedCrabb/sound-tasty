import random
import pickle
from flask import Flask, request, render_template, jsonify


with open('ingred_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('ingredients.pkl', 'rb') as f:
    ingredients = pickle.load(f)

with open('title.pkl', 'rb') as f:
    title = pickle.load(f)
app = Flask(__name__, static_url_path="")


@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')


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


def sound_tasty(word_vec_model,
                ingred_series,
                title_series,
                ingred_1,
                ingred_2,
                ingred_3,
                ingred_4,
                adventure="low"):
    """Recommend recipes based on ingredient similarity"""
    import random

    try:
        ingre_list = parse_ingred_tuples(word_vec_model.wv.most_similar(
            positive=(ingred_1.lower().split() +
                      ingred_2.lower().split() +
                      ingred_3.lower().split() +
                      ingred_4.lower().split()),
            topn=100000)
            )

        user_input = adventure
        print('\n')

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

        recipes_to_return = [title_series[high_value[0]],
                             ingred_series[high_value[0]]]
        run_up_recips = []
        for i in range(len(runners_up)):
            run_up_recips.append(title_series[runners_up[i][0]])
            run_up_recips.append(ingred_series[runners_up[i][0]])

        return recipes_to_return + run_up_recips

    except KeyError:
        return 'Ingredient not recognized... sorry :('


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a random prediction."""
    data = request.json
    return jsonify(sound_tasty(model,
                               ingredients,
                               title,
                               data['user_input1'],
                               data['user_input2'],
                               data['user_input3'],
                               data['user_input4'],
                               adventure=data['user_input5']))
