const client = new Paho.MQTT.Client("157.173.101.159", Number(9001), "webClient" + Math.random());

// Called when the client connects
client.onConnectionLost = function (responseObject) {
  if (responseObject.errorCode !== 0)
    console.log("🛑 Connection lost:" + responseObject.errorMessage);
};

client.onMessageArrived = function (message) {
  console.log("[MQTT] Message Arrived: " + message.payloadString);
};

client.connect({
  onSuccess: function () {
    console.log("✅ Connected to MQTT broker");
  },
  useSSL: false
});

function submitSchedule() {
  event.preventDefault(); // prevent form reload

  const onTime = document.getElementById("onTime").value;
  const offTime = document.getElementById("offTime").value;
  const status = document.getElementById("status");

  if (!/^\d{2}:\d{2}$/.test(onTime) || !/^\d{2}:\d{2}$/.test(offTime)) {
    status.innerText = "❌ Invalid time format. Use HH:MM.";
    return;
  }

  const messageOn = new Paho.MQTT.Message(onTime);
  messageOn.destinationName = "light/schedule/on";
  client.send(messageOn);

  const messageOff = new Paho.MQTT.Message(offTime);
  messageOff.destinationName = "light/schedule/off";
  client.send(messageOff);

  status.innerText = `✅ Schedule sent: ON at ${onTime}, OFF at ${offTime}`;
}
