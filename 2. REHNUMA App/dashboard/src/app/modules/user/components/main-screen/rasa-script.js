WebChat.default.init({
    selector: "#webchat",
    customData: {"language": "en"}, // arbitrary custom data. Stay minimal as this will be added to the socket
    socketUrl: "http://localhost:5005",
    socketPath: "/socket.io/",
    title: "Rehnuma",
    subtitle: "A guide to your health",
  })