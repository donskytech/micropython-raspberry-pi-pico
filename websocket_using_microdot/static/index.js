const sensorValues = document.querySelector("#sensor-values");

const sensorData = [];

/*
  Plotly.js graph and chart setup code
*/
var sensorChartDiv = document.getElementById("sensor-chart");

// History Data
var sensorTrace = {
  x: [],
  y: [],
  name: "LDR/Photoresistor",
  mode: "lines+markers",
  type: "line",
};

var sensorLayout = {
  autosize: false,
  width: 800,
  height: 500,
  colorway: ["#05AD86"],
  margin: { t: 40, b: 40, l: 80, r: 80, pad: 0 },
  xaxis: {
    gridwidth: "2",
    autorange: true,
  },
  yaxis: {
    gridwidth: "2",
    autorange: true,
  },
};
var config = { responsive: true };

Plotly.newPlot(sensorChartDiv, [sensorTrace], sensorLayout, config);

// Will hold the sensor reads
let newSensorXArray = [];
let newSensorYArray = [];

// The maximum number of data points displayed on our scatter/line graph
let MAX_GRAPH_POINTS = 50;
let ctr = 0;

function updateChart(sensorRead) {
  if (newSensorXArray.length >= MAX_GRAPH_POINTS) {
    newSensorXArray.shift();
  }
  if (newSensorYArray.length >= MAX_GRAPH_POINTS) {
    newSensorYArray.shift();
  }
  newSensorXArray.push(ctr++);
  newSensorYArray.push(sensorRead);

  var data_update = {
    x: [newSensorXArray],
    y: [newSensorYArray],
  };

  Plotly.update(sensorChartDiv, data_update);
}

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
  updateValues(event.data);
  updateChart(event.data);
}

function sendMessage(message) {
  websocket.send(message);
}

function updateValues(data) {
  sensorData.unshift(data);
  if (sensorData.length > 20) sensorData.pop();
  sensorValues.value = sensorData.join("\r\n");
}
