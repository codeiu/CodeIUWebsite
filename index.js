const express = require("express"),
  bodyparser = require("body-parser"),
  path = require("path"),
  axios = require("axios"),
  ejs = require("ejs"),
  port = 11235;
app = express();
app.use(bodyparser.json());

let youtube_template = "";

app.get("/", (req, res) => {
  res.send("<h1>Hello</h1>");
});

/* Responds with a JSON of format { videos: [] } with Code@IU YouTube video links.
At the moment, if there is an error, it will simply respond with an empty list*/
app.get("/videos", (req, res) => {
  let url =
    "https://www.googleapis.com/youtube/v3/search?key=AIzaSyB8tF_u2E19Poo147OkY02zNwpNfFdVnYI&" +
    "type=video&part=snippet&channelId=UC1aXDYhzYCzOCNxJV6hYdLA&maxResults=10&q=";
  const youtube_url = "https://youtube.com/embed/";
  let videoIds = [];
  axios
    .get(url)
    .then((response) => {
      for (let i in response.data.items) {
        let item = response.data.items[i];
        videoIds.push(item.id.videoId);
      }
    })
    .catch((err) => alert(err))
    .finally(() => {
      // ejs.renderFile(
      //   path.join(__dirname, "views", "videos.html"),
      //   { videos: videoIds },
      //   {},
      //   (err,str) => {
      //     res.send(str);
      //   }
      // );
      res.sendFile(path.join(__dirname, "views", "videos.html"));
    });
});

app.listen(port, () => {
  console.log("Listening on port " + port);
});
