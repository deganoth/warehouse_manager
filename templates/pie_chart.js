var ctx = document.getElementById('pieChart').getContext('2d');
	var pieChart = new Chart(ctx, {
		type: 'pie',
		data: {
			labels: [{% for product in bar_product %}
			"{{product.product_name}}",
			{% endfor %}],
			datasets: [{
				label: '{{bar_name}}',
				data: [{% for product in bar_quantity %}
				"{{product.product_quantity}}",
				{% endfor %}],
				backgroundColor: [
				'rgba(255, 99, 132, 0.2)',
				'rgba(54, 162, 235, 0.2)',
				'rgba(255, 206, 86, 0.2)',
				'rgba(75, 192, 192, 0.2)',
				'rgba(153, 102, 255, 0.2)',
				'rgba(255, 159, 64, 0.2)'
				],
				borderColor: [
				'rgba(255, 99, 132, 1)',
				'rgba(54, 162, 235, 1)',
				'rgba(255, 206, 86, 1)',
				'rgba(75, 192, 192, 1)',
				'rgba(153, 102, 255, 1)',
				'rgba(255, 159, 64, 1)'
				],
				borderWidth: 1
			}]
		},
		options: {
			responsive: true,
			legend: {
				display: false
			},
			legendCallback: function(chart) {
				var text = [];
				text.push('<div class="' + chart.id + '-legend">');
				for (var i = 0; i < chart.data.datasets[0].data.length; i++) {
					text.push('<ul><span style="background-color:' + chart.data.datasets[0].backgroundColor[i] + '">');
					if (chart.data.labels[i]) {
						text.push(chart.data.labels[i]);
					}
					text.push('</span><span class="product_quantity">' + chart.data.datasets[0].data[i] + '</span></ul>');
				}

				text.push('</div>');
				return text.join("");
			},

		}

	});
	document.getElementById('pie-legend').innerHTML = pieChart.generateLegend();
