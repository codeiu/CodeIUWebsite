const express = require("express"),
  bodyparser = require("body-parser"),
  path = require("path"),
  port = 11235;
app = express();
app.use(bodyparser.json());

app.get("/", (req, res) => {
  res.send("<h1>Hello</h1>");
});

app.listen(port, () => {
  console.log("Listening on port " + port);
});
