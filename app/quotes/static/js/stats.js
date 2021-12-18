var activeUsersChart = new Chart(document.getElementById("active-users"), {
  type: "line",
  data: {
    labels: activeUsersNames,
    datasets: [
      {
        label: "Users every month of the last year",
        data: activeUsersCount
      }
    ]
  },
  options: {
    scales: {
      y: {
        ticks: {
          beginAtZero: true
        }
      }
    }
  }
});


var postsCategoriesChart = new Chart(document.getElementById("posts-categories"), {
  type: 'doughnut',
  data: {
  labels: postsCateogoriesNames,
  datasets: [{
    label: 'My First Dataset',
    data: postsCateogoriesCount,
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4
  }]
},
});

var genderChart = new Chart(document.getElementById("genders"), {
  type: 'bar',
  data: {
  labels: genderPlatformNames,
  datasets: [{
    label: 'Genders of the platform',
    data: genderPlatformCount,
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
    ],
    borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
    ],
    borderWidth: 1
  }]
},
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  },
});


