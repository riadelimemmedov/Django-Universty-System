'use strict';

$(document).ready(function() {

	// Area chart

	let getAvgMonthRevenue = window.location.href.replace('account/','get/avg/month/revenue')
	let getEveryYearStudentsCount = window.location.href.replace('account/','get/every/year/students/count')
	var urls = [getAvgMonthRevenue, getEveryYearStudentsCount]

	let admissionMonthList = null
	let months = ['January','February','March','April','May','June','July','August','September','October','November','December']
	let avgMonthRevenue = []

	$.each(urls, function(index,element){
		$.ajax({
			type: 'GET',
			url:element,
			success: function(response){
				admissionMonthList = response.admission_months_list
				console.log('Response value', response)
			},
			error: function(err){
				console.log('Error value ', err)
			}
		})
	})

	setTimeout(()=>{
		months.forEach((value,index)=>{
			avgMonthRevenue.push(admissionMonthList[index][value][0]==null ? 0 : Number(admissionMonthList[index][value][0]))
		})
	},1000)

	setTimeout(()=>{
	},1500)

	if ($('#apexcharts-area').length > 0) {
	var options = {
		chart: {
			height: 350,
			type: "area",
			toolbar: {
				show: false
			},
		},
		dataLabels: {
			enabled: false
		},
		stroke: {
			curve: "smooth"
		},
		series: [{
			name: "Teachers",
			data: [45, 60, 75, 51, 42, 42, 30,42,92,65,22,15]
		}, {
			name: "Students",
			color: '#FFBC53',
			data: avgMonthRevenue
		}],
		xaxis: {
			categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July','Aug','Sept','Oct','Nov','Dec'],
		}
	}
	var chart = new ApexCharts(
		document.querySelector("#apexcharts-area"),
		options
	);
	chart.render();
	}

	// Bar chart
	
	if ($('#bar').length > 0) {
	var optionsBar = {
		chart: {
			type: 'bar',
			height: 350,
			width: '100%',
			stacked: true,
			toolbar: {
				show: false
			},
		},
		dataLabels: {
			enabled: false
		},
		plotOptions: {
			bar: {
				columnWidth: '45%',
			}
		},
		series: [{
			name: "Boys",
			color: '#fdbb38',
			data: [420, 532, 516, 575, 519, 517, 454, 392, 262, 383, 446, 551, 563, 421, 563, 254, 452],
		}, {
			name: "Girls",
			color: '#19affb',
			data: [336, 612, 344, 647, 345, 563, 256, 344, 323, 300, 455, 456, 526, 652, 325, 425, 436],
		}],
		labels: [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
		xaxis: {
			labels: {
				show: false
			},
			axisBorder: {
				show: false
			},
			axisTicks: {
				show: false
			},
		},
		yaxis: {
			axisBorder: {
				show: false
			},
			axisTicks: {
				show: false
			},
			labels: {
				style: {
					colors: '#777'
				}
			}
		},
		title: {
			text: '',
			align: 'left',
			style: {
				fontSize: '18px'
			}
		}

	}
  
	var chartBar = new ApexCharts(document.querySelector('#bar'), optionsBar);
	chartBar.render();
	}
  
});