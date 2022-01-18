const express = require('express')
const compression = require('compression');

const app = express()
const port = 3000

const shouldCompress = (req, res) => {
  if (req.headers['x-no-compression']) {
    return false
  }
  return compression.filter(req, res);
}

app.use(compression({
  filter: shouldCompress,
  level: 9,
}));

// serve your css as static
app.use(express.static(__dirname+"/static"));

app.get('/', (req, res) => {
    res.sendFile(__dirname + "/static/Portofolio.html");
})

app.listen(port, () => {
  console.log(`Portofolio app listening at http://localhost:${port}`)
})