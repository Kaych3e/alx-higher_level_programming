#!/usr/bin/node
// Script that computes the number of tasks completed by user id

// import request and request URL
const request = require('request');
const url = process.argv[2];

request(url, (error, response, data) => {
  if (error) {
    console.log(error);
  } else {
    const todos = (JSON.parse(data));
    const completeTasks = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completeTasks[todo.userId]) {
          completeTasks[todo.userId]++;
        } else {
          completeTasks[todo.userId] = 1;
        }
      }
    });
    console.log(completeTasks);
  }
});
