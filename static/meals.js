// Select meal container element
mealContainer = document.getElementById('meal-container');

// Meal category name and meal category id are stored on the h1 for easy access. Get those values from there.
h1 = document.querySelector('h1');
meal_category = h1.id;
meal_category_id = h1.dataset.id;

// Helper function for generating HTML markup
function generateHTML(meal) {
  return `
      <div class="col-12">
        <div class="d-flex justify-content-center">
          <h3 class="mb-3"><a class="meal-titles" href="/meals/${meal_category_id}/${meal.idMeal}">${meal.strMeal}</a></h3>
        </div>
        <div class="d-flex justify-content-center">
          <a class="meal-titles" href="/meals/${meal_category_id}/${meal.idMeal}">
          <img class="meal-category-img mb-5 img-thumbnail" src="${meal.strMealThumb}" alt="${meal.strMeal} image">
          </a>
          
        </div>
      </div>
  `;
}

// Send API request and display each meal in meal container element
async function getMealsByCategory() {
  res = await axios.get(`https://www.themealdb.com/api/json/v1/1/filter.php?c=${meal_category}`);
   
  meals = res.data.meals

  for (meal of meals) {
    let mealDiv = document.createElement('div');
    mealDiv.innerHTML = generateHTML(meal);
    mealContainer.append(mealDiv);
  }
}


// On Load
getMealsByCategory();


