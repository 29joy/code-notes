function displayMessage() {
  const html = document.querySelector("html");

  const panel = document.createElement("div");
  panel.setAttribute("class", "msgBox");
  html.appendChild(panel);

  const msg = document.createElement("p");
  msg.textContent = "This is a message box";
  panel.appendChild(msg);

  const closeBtn = document.createElement("button");
  closeBtn.textContent = "x";
  panel.appendChild(closeBtn);

  closeBtn.onclick = function () {
    panel.parentNode.removeChild(panel);
  };

}