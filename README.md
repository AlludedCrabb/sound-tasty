# Sound Tasty?
People need to eat, and there's so much variety in the available options! The problem is people don't always know what they like or don't like until they try it. The point of Sound Tasty is to hopefully help people find new foods they like.

## The Data
I Used Selenium to scrape recipes from Allrecipes.com, approximately 100 from each catagory.
<img src="Allrecipes.png">

## The Plan
To build a food recommendation system based off of flavors people like. Ask the user for ingredients they like, then find similar ingredients and recommend recipes that have those similar ingredients.

## The Preparation
I cleaned the recipe data by removing amounts and measures, cooking stop words, and some brand names. I also split the ingredients into individual words and phrases to prepare for modeling.

## The Modeling
I used Gensim's word2vec to vectorize the ingredient words, then return recipes that contain ingredients with similar vectors to the input words. I also included an "adventure" input that takes in either low, medium, or high, which will change the ingredient vectors used for recipe recommendation to the 20 most similar, the 20 vectors halfway similar, or the 20 least similar vectors, respectively.

## The Results
I deployed the final model to a flask app which you can find <a href=http:tasty.dsi.link>here</a>.

## Next steps
The small amount of data means that there are many ingredients and recipes Sound Tasty doesn't know. The next steps would include gathering more recipes to expand its knowledge, adding features like flavor or ingredient removal, finding local vendors that have those flavors, and so on.
