const express = require("express"),
  bodyparser = require("body-parser"),
  path = require("path"),
  axios = require("axios"),
  ejs = require("ejs"),
  port = 11235;
app = express();
app.use(bodyparser.json());

const getVideos = () => {
  let url =
    "https://www.googleapis.com/youtube/v3/search?key=AIzaSyB8tF_u2E19Poo147OkY02zNwpNfFdVnYI&" +
    "type=video&part=snippet&channelId=UC1aXDYhzYCzOCNxJV6hYdLA&maxResults=10&q=";
  const youtube_url = "https://youtube.com/embed/";
  return axios
    .get(url)
    .then((response) => {
      let videoIds = [];
      for (let i in response.data.items) {
        let item = response.data.items[i];
        videoIds.push(item.id.videoId);
      }
      return videoIds;
    })
    .catch((err) => {
      console.log("\n-- ERROR IN getVideos() --\n" + err);
      return [];
    });
};

app.get("/", (req, res) => {
  res.send("<h1>Hello</h1>");
});

app.get("/videos", (req, res) => {
  getVideos().then((videoIds, rej) => {
    console.log(videoIds);
    ejs.renderFile(
      path.join(__dirname, "views", "videos.html"),
      videoIds,
      {},
      (err, str) => {
        res.send(str);
      }
    );
  });
});

app.listen(port, () => {
  console.log("Listening on port " + port);
});
