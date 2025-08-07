const myImage = document.querySelector("img");

myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/picture1.jpg") {
    myImage.setAttribute("src", "images/picture2.jpg");
  } else {
    myImage.setAttribute("src", "images/picture1.jpg");
  }
};

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
    const myName = prompt("Please enter your name.");
    if (!myName) {
      setUserName();
    } else {
      localStorage.setItem("name", myName);
      myHeading.textContent = `JNT is designed for you, ${myName}`;
    }
}

if (!localStorage.getItem("name")) {
setUserName();
} else {
const storedName = localStorage.getItem("name");
myHeading.textContent = `JNT is designed for you, ${storedName}`;
}

myButton.onclick = function () {
    setUserName();
};
