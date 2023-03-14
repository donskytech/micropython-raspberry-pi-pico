// Slider
var redSlider = document.querySelector("#redSlider");
var redValue = document.querySelector("#redValue");

var greenSlider = document.querySelector("#greenSlider");
var greenValue = document.querySelector("#greenValue");

var blueSlider = document.querySelector("#blueSlider");
var blueValue = document.querySelector("#blueValue");

redSlider.addEventListener("change", () => {
  redValue.textContent = redSlider.value;
  sendMessage(
    JSON.stringify({
      red: redSlider.value,
      green: greenSlider.value,
      blue: blueSlider.value,
    })
  );
});

greenSlider.addEventListener("change", () => {
  greenValue.textContent = greenSlider.value;
  sendMessage(
    JSON.stringify({
      red: redSlider.value,
      green: greenSlider.value,
      blue: blueSlider.value,
    })
  );
});

blueSlider.addEventListener("change", () => {
  blueValue.textContent = blueSlider.value;
  sendMessage(
    JSON.stringify({
      red: redSlider.value,
      green: greenSlider.value,
      blue: blueSlider.value,
    })
  );
});

// WebSocket support
var targetUrl = `ws://${location.host}/ws`;
var websocket;
window.addEventListener("load", onLoad);

function onLoad() {
  initializeSocket();
}

function initializeSocket() {
  console.log("Opening WebSocket connection MicroPython Server...");
  websocket = new WebSocket(targetUrl);
  websocket.onopen = onOpen;
  websocket.onclose = onClose;
  websocket.onmessage = onMessage;
}
function onOpen(event) {
  console.log("Starting connection to WebSocket server..");
}
function onClose(event) {
  console.log("Closing connection to server..");
  setTimeout(initializeSocket, 2000);
}
function onMessage(event) {
  console.log("WebSocket message received:", event);
}

function sendMessage(message) {
  websocket.send(message);
}
