const express = require('express')
const app = express()

const port = process.argv[2]

app.listen(port, () => console.log(`Listening on port ${port}.`))

app.get('/hello', (req, res) => {
    console.log(req.headers)
    res.send('Hello.\n')
})