const express = require("express"),
  bodyparser = require("body-parser"),
  path = require("path"),
  port = 11235;
(homepage = "index.html"), (app = express());
app.use(bodyparser.json());

// GET
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, homepage));
});

// POST
app.post("/", (req, res) => {});

// Run the server
app.listen(port, () => {
  console.log("Listening on port " + port);
});
