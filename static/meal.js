// There are a couple problems with how the API returns the data that's difficult to fix on the backend. I'll fix these problems on the frontend here.

// Problem #1 - The YouTube URLs that are returned from the API are direct view YouTube links. The problem with that is, YouTube doesn't allow other websites to embed their videos using direct view links. Instead, I need the embeddable links.

// Select the video element
const video = document.getElementsByClassName('youtube');

// Get the video URL from the video element
const youtubeUrl = video[0].id;

// Fix video URL so it's embeddable
const newYoutubeUrl = youtubeUrl.replace("watch?v=", "embed/");

// Set video element's source attribute as the new URL which is embeddable
video[0].attributes[4].value = newYoutubeUrl;

/*/ Problem #2 - The API returns ingredients and their measurements separately and also one by one.

    Ex: strIngredient1, strIngredient2, strMeasure1, strMeasure2

    It's extremely difficult to work with them this way so I'll need to combine those and put everything in a single array.
/*/

// Cache container element to display ingredients
const ingredientsContainer = document.getElementById('ingredients-container');

// Select the button element. Both buttons have the same id, but this is not a problem because only one button is visible on the page depending on if the user has favorited the meal or not.
const button = document.getElementById('meal-id-btn');

// Get the ID of meal from the button. This is probably not the best way to get the needed data but in this case, it's the simplest way.
mealID = button.getAttribute('value');

// Make an API request to get the meal information
async function getMealById(mealID) {
  result = await axios.get(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${mealID}`)
  
  const meal = result.data.meals[0]
  
  getMealIngredients(meal)
}

// Store meal ingredients for a meal and display them inside the ingredients container element.
function getMealIngredients(meal) {
  const ingredients = [];

  for (let i = 1; i <= 20; i++) {
    if (meal[`strIngredient${i}`]) {
      ingredients.push(
        `${meal[`strIngredient${i}`]} - ${meal[`strMeasure${i}`]}`
      );
    } else {
      break;
    }
  }

  ingredientsContainer.innerHTML = `
  <div class="single-meal">
    <h2 class="mb-4">Ingredients</h2>
    <ul>
      ${ingredients.map(ing => `<li>${ing}</li>`).join('')}
    </ul>
  </div>
  `;
}

// On Load
getMealById(mealID);