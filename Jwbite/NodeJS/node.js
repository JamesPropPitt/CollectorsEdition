var express = require('express');
var mysql = require('mysql');
var app = express();

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'admin',
    password: 'c0e5f3dfa0db72e3ca4102767b80b765db2de51a798e9305',
    database: 'falmout6_pom',
})

connection.connect(function(error){
    if(!!error){
        console.log('Error');
    }
    else{
        console.log('Connected');
    }
});

app.get('/', function(req, resp){
    connection.query("", function(error, rows,field){
        if(!!error){
            console.log('Error');
        } else{
            console.log('It worked');
        }
    })
})
app.listen(3306);

