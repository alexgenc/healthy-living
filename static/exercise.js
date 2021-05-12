// There are a couple problems with how the API returns the data that's difficult to fix on the backend. I'll fix these problems on the frontend here.

// Problem #1 - The exercise descriptions include html tags such as p, ol, li. I'll need to get rid of those.

// Select element containing exercise description.
descriptionContainer = document.getElementById("exercise-description")

// Get exercise description as text.
description = descriptionContainer.innerText;

// Replace all unwanted tags with "" .
description = description.replaceAll("<p>", "").replaceAll("</p>", "").replaceAll("<ol>", "").replaceAll("</ol>", "").replaceAll("<li>", "").replaceAll("</li>", "");

// Set description of element as the new description that doesn't contain any html tags.
descriptionContainer.innerText = description;


/* Problem #2 - The image URLs returned from the original exercise API do not work for some unknown reason. I'll use Contextual Web Search API to get images and display them. 

Contextual Web Search API does a simple Google Images search and returns the first 10 images as a result. For simplicity purposes, I'm only using the first image that's returned. 

Note, the image that is returned isn't always the correct image for the exercise, but it's OK in this case since this is an educational demonstration and I don't have control over the returned data.

*/

// Select image container
imagesContainer = document.getElementById('images-container');

// The name of each exercise is stored as the id of h1 element. Get the name of the exercise from there.
exerciseTitle = document.querySelector('h1').getAttribute('id');

// Send API request and display image in image container. API key is visible here because this is a free API.

async function getExerciseImage() {
  const options = {
    method: 'GET',
    url: 'https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI',
    params: {q: `${exerciseTitle} Exercise`, pageNumber: '1', pageSize: '10', autoCorrect: 'true'},
    headers: {
      'x-rapidapi-key': '5dc65faf87msh677bcb705315d43p104f53jsn64eb3d3aeafb',
      'x-rapidapi-host': 'contextualwebsearch-websearch-v1.p.rapidapi.com'
    }
  };
  
  axios.request(options).then(function (response) {
      imgEl= document.createElement('img');
      imgEl.classList.add("exercise-img");
      imgEl.src = response.data.value[0].url
      imagesContainer.append(imgEl);
  }).catch(function (error) {
    console.error(error);
  });
}

// On Load
getExerciseImage();