// Jquery way of writing onLoad
$(function() {
  // Date picker
  $('#datetimepicker1').datetimepicker({
    format: 'YYYY/MM/DD',
  });
  $('#datetimepicker2').datetimepicker({
    format: 'YYYY/MM/DD',
  });
  // The function below gets canvas with ... id and populates it with data INITIAL
  // Start of drawing charts
  var $expanseChart = $('#expanse-chart');
  var $incomeChart = $('#income-chart');
  var expanseLabels;
  var expanseData;
  var expanseConfig;
  var incomeLabels;
  var incomeData;
  var incomeConfig;
  var expansePieChart;
  var incomePieChart;
  var invalidIncomeForm = function(referenceNode) {
    referenceNode.parentNode.insertBefore('', referenceNode.nextSibling).fadeOut().empty();
  };
  var colorArray = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
    '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
    '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
    '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
    '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
    '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
    '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
    '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
    '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
    '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'];
  var secColorArray = colorArray.slice().reverse();
  $.ajax({
    url: $expanseChart.data('url'),
    dataType: 'json',
    success: function(data) {
      var ctx = $expanseChart[0].getContext('2d');
      expanseData = data.data;
      expanseLabels = data.labels;
      expanseConfig = {
        type: 'pie',
        data: {
          datasets: [{
            data: expanseData,
            backgroundColor: colorArray,
            label: 'Expanses',
          }],
          labels: expanseLabels,
        },
        options: {
          responsive: true,
          title: {
            display: true,
            text: 'Expanses'
          },
        }
      };
      expansePieChart = new Chart(ctx, expanseConfig);
    },
  });
  $.ajax({
    url: $incomeChart.data('url'),
    dataType: 'json',
    success: function(data) {
      var ctx = $incomeChart[0].getContext('2d');
      incomeData = data.data;
      incomeLabels = data.labels;
      incomeConfig = {
        type: 'pie',
        data: {
          datasets: [{
            data: incomeData,
            backgroundColor: secColorArray,
            label: 'Incomes',
          }],
          labels: incomeLabels
        },
        options: {
          responsive: true,
          title: {
            display: true,
            text: 'Incomes'
          },
        }
      };
      incomePieChart = new Chart(ctx, incomeConfig);
    },
  });
  // End of drawing Charts

  // Add expanse ...
  $('#expanseForm').on('submit', function() {
    var $form = $(this);
    $.ajax({
      url: $form.attr('data-url'),
      data: $form.serialize(),
      type: $form.attr('method'),
      dataType: 'json',
      success: function(data) {
        if(data.is_valid) {
          expanseData = data.data;
          expanseLabels = data.labels;
          expanseConfig.data.datasets[0].data = expanseData;
          expanseConfig.data.labels = expanseLabels;
          expansePieChart.update();
          $('#total-expanse').text(data.user_total_expanse);
        } else {
          $form.after('<p id="added_expanse_message" class="text-danger text-center">Invalid Form Field</p>');
          var fade_out = function() {
            $('#added_expanse_message').fadeOut(2000, function() {
              $(this).remove();
            });
          }
          setTimeout(fade_out, 2000);
        }
      }
    });
    return false;
  });

  // Add income ...
  $('#incomeForm').on('submit', function() {
    var $form = $(this);
    $.ajax({
      url: $form.attr('data-url'),
      data: $form.serialize(),
      type: $form.attr('method'),
      dataType: 'json',
      success: function(data) {
        if(data.is_valid) {
          incomeData = data.data;
          incomeLabels = data.labels;
          incomeConfig.data.datasets[0].data = incomeData;
          incomeConfig.data.labels = incomeLabels;
          incomePieChart.update();
          $('#total-income').text(data.user_total_income);
        } else {
          $form.after('<p id="added_income_message" class="text-danger text-center">Invalid Form Field</p>');
          var fade_out = function() {
            $('#added_income_message').fadeOut(2000, function() {
              $(this).remove();
            });
          }
          setTimeout(fade_out, 2000);
        }
      },
    });
    return false;
  });
});
