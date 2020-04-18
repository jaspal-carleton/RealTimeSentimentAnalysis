//##############################################################################
// Script         : histogram.js
// Description    : JavaScript to plot histogram of live sentiments
// Author         : Jaspal Singh (jaspal.singh@carleton.ca)
// Date           : 04/12/2020
// Version        : 1.0
//##############################################################################

// Object for HighCharts Lib (used to plot histogram)
var chart;

// Web-Client Callback Function to receive Sentiment Score from Python main.py (Flask Web-Server)
function requestData() {
  $.ajax({
    url: '/live-stream',
    success: function(point) {
      // Show Maximum of Twenty Sentiments in Histogram
      var series = chart.series[0];
      var shift = series.data.length > 20;
      
      // Add Sentiment Score Data Points to HighChart histogram
      chart.series[0].addPoint(point[0], true, shift);
      chart.series[1].addPoint(point[1], true, shift);
      chart.series[2].addPoint(point[2], true, shift);
        
      // Embed Sentiment Scores in HTML DOM
      document.getElementById("tweet").innerHTML= point[3][1];
      document.getElementById("tweetNeg").innerHTML= "Negative "+point[0][1]+"%";
      document.getElementById("tweetNeu").innerHTML= "Neutral "+point[1][1]+"%";
      document.getElementById("tweetPos").innerHTML= "Positive "+point[2][1]+"%";

      // Recursive Call every two seconds
      setTimeout(requestData, 2000);
    },
    cache: false
  });
}

// JavaScript Function for Plotting Histogram
$(document).ready(function() {
  // Create HighCharts Lib Chart Object
  chart = new Highcharts.Chart({
    chart: {
      renderTo: 'data-container',
      defaultSeriesType: 'column', //Bar-Chart
      events: {
        load: requestData //Callback Function to get histogram data
      }
    },
    title: {
      text: 'Sentiment Analysis of COVID-19 Live Tweets'
    },
    xAxis: {
      type: 'datetime',
      tickPixelInterval: 150,
      maxZoom: 20 * 1000,
      title: {
        text: 'Time (UTC)',
        margin: 10
      },
      lineColor: '#CACACA',
      lineWidth: 1
    },
    yAxis: {
      minPadding: 0.2,
      maxPadding: 0.2,
      title: {
        text: 'Sentiment (Percentage)',
        margin: 10
      },
      endOnTick: false,
      min: 0,
      max: 100,
      tickInterval: 20,
      lineColor: '#CACACA',
      lineWidth: 1,
    },
    legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle',
      borderWidth: 0
    },
    series: [{
      name: 'Negative',
      color:'#E74C3C',
      data: []
    },{
      name: 'Neutral',
      color: '#CACFD2',
      data: []
    },{
      name: 'Positive',
      color: '#2ECC71',
      data: []
    }]
  });
});