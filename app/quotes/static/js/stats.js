var activeUsersChart = new Chart(document.getElementById("active-users"), {
  type: "line",
  data: {
    labels: activeUsersNames,
    datasets: [
      {
        label: "Visits last 7 days",
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

var loadedPagesNamesChart = new Chart(document.getElementById("loaded-pages"), {
  type: 'bar',
  data: {
  labels: loadedPagesNamesNames,
  datasets: [{
    label: 'Loaded pages by name',
    data: loadedPagesNamesCount,
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


var visitsDayWeekChart = new Chart(document.getElementById("visits-day-week"), {
  type: 'bar',
  data: {
  labels: visitsDayOfTheWeekNames,
  datasets: [{
    label: 'Visits by day of the week',
    data: visitsDayOfTheWeekCount,
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


var postsCategoriesChart = new Chart(document.getElementById("imgs-with-alt-text"), {
  type: 'doughnut',
  data: {
  labels: imagePostsWithAltNames,
  datasets: [{
    label: 'Image posts adapted with alt texts',
    data: imagePostsWithAltCount,
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4
  }]
},
});


var videosWithDescriptionsChart = new Chart(document.getElementById("videos-with-descriptions"), {
  type: 'doughnut',
  data: {
  labels: videosWithTextDescriptionNames,
  datasets: [{
    label: 'Video posts adapted with readable descriptions',
    data: videosWithTextDescriptionCount,
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4
  }]
},
});