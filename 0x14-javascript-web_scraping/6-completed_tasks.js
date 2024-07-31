#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve tasks information. Status code:', response.statusCode);
  } else {
    const tasks = JSON.parse(body);

    const completedTasks = tasks.filter(task => task.completed);

    const completedTasksByUser = completedTasks.reduce((result, task) => {
      const userId = task.userId.toString();
      result[userId] = (result[userId] || 0) + 1;
      return result;
    }, {});

    console.log(completedTasksByUser);
  }
});
