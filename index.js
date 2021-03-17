const express = require('express');

const app = express();
app.set('view engine', 'ejs');

app.use(express.static('public'));

app.get('/videos/:id', function(req, res) {
  res.send("hi");
});

app.get('/', function(req, res) {
  res.render('homepage');
});

app.listen(process.env.PORT || 8080, function(err) {
	if (err) return console.log(err);

	console.log("app started on port " + (process.env.PORT || 8080));
});
