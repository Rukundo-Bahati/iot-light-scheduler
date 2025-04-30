// MQTT Client Setup
const client = new Paho.MQTT.Client("broker.hivemq.com", Number(8000), "webClient_" + Math.random().toString(16).substr(2, 8));

client.onConnectionLost = function(responseObject) {
  console.log("Connection lost:", responseObject.errorMessage);
  document.getElementById("status").innerText = "⚠️ Disconnected from broker";
};

client.onMessageArrived = function(message) {
  console.log("Message arrived:", message.payloadString);
};

function connectMqtt() {
  client.connect({
    onSuccess: function() {
      console.log("Connected to MQTT broker");
      document.getElementById("status").innerText = "✅ Connected to broker";
    },
    onFailure: function(err) {
      console.log("Connection failed:", err.errorMessage);
      document.getElementById("status").innerText = "❌ Connection failed";
    },
    useSSL: true
  });
}

// Connect when page loads
window.onload = connectMqtt;

// Form Submission
function submitSchedule(event) {
  event.preventDefault();
  
  const onTime = document.getElementById("onTime").value;
  const offTime = document.getElementById("offTime").value;
  const statusEl = document.getElementById("status");

  if (!onTime || !offTime) {
    statusEl.innerText = "❌ Please enter both times";
    return;
  }

  // Publish schedule
  const messageOn = new Paho.MQTT.Message(onTime);
  messageOn.destinationName = "light/schedule/on";
  client.send(messageOn);

  const messageOff = new Paho.MQTT.Message(offTime);
  messageOff.destinationName = "light/schedule/off";
  client.send(messageOff);

  statusEl.innerText = `✅ Schedule set: ON at ${onTime}, OFF at ${offTime}`;
  
  // Clear form
  event.target.reset();
}