const express = require('express');
const fetch = require('node-fetch');

const app = express();
app.set('view engine', 'ejs');

app.use(express.static('public'));

let obj = {
	hi: "world",
	num: 3,
}

app.get('/', function(req, res) {
  res.render('homepage');
});

app.get('/about', function(req, res) {
	res.render('about');
});

app.get('/projects', function(req, res) {
	res.render('projects');
});

app.get('/calendar', function(req, res) {
	res.render('calendar');
});

app.get('/videos', function(req, res) {
	fetch('https://www.googleapis.com/youtube/v3/search?key=AIzaSyB8tF_u2E19Poo147OkY02zNwpNfFdVnYI&type=video&part=snippet&channelId=UC1aXDYhzYCzOCNxJV6hYdLA&maxResults=20&q=')
	.then((videoStream) => videoStream.json())
	.then((videos) => res.render('videos', { videos: videos.items }))
	.catch((err) => console.warn(err));
});

app.listen(process.env.PORT || 8080, function(err) {
	if (err) return console.log(err);

	console.log("app started on port " + (process.env.PORT || 8080));
});
