const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const picArray = ["pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpg", "pic5.jpg"];
/* Declaring the alternative text for each image file */

const newImage = document.createElement('img');
/* Looping through images */
for (var i = 1; i <= picArray.length; i++) {
    newImage.setAttribute('src', "images/pic[i].jpg");
    newImage.setAttribute('alt', "a picture in this array");
    thumbBar.appendChild(newImage);
}

btn.addEventListener("click", () => {
    const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
    document.body.style.backgroundColor = rndCol;
  });

/* Wiring up the Darken/Lighten button */
