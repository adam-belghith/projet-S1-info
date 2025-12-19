Highcharts.chart('container', {title: {text: 'Historique des données Température (ou Humidité ou Gaz) enregistrées'},
			       subtitle: {text: 'données enregistrées depuis la rasberryPi'},
			       yAxis: {title: {text: 'Températures (en ° Celsius)'}},
			       xAxis: {accessibility: {rangeDescription: 'Range: 1 à 6 mois'}}, //JSP où apparait cette ligne dans l'exercice d'origine
			       legend: {layout: 'vertical',align: 'right',verticalAlign: 'middle'}, //Orientation et position de la légende
			       plotOptions: {series: {label: {connectorAllowed: false},pointStart: 1}}, //JSP
			       series:
			       [{name: 'Températures',data: [10, 11, 27, 26, 10, 11]}],
			       responsive: {
				   rules: [{condition: {maxWidth: 500},
					    chartOptions: {legend: {layout: 'horizontal',align: 'center',verticalAlign: 'bottom'}}
					   }]
			       }
			      }
		);

/*
Highcharts.chart('container', {title: {text: 'Consommation petit déjeuner'},
			       subtitle: {text: 'données inventées'},
			       yAxis: {title: {text: 'Typede petit déjeuner des 6 derniers mois'}},
			       xAxis: {accessibility: {rangeDescription: 'Range: 1 à 6 mois'}},
			       legend: {layout: 'vertical',align: 'right',verticalAlign: 'middle'},
			       plotOptions: {series: {label: {connectorAllowed: false},pointStart: 1}},
			       series:
			       [{name: 'Chocolats',data: [10, 11, 27, 26, 10, 11]},
				{name: 'Pains au chocolat',data: [23, 24, 29, 29, 30, 41]},
				{name: 'Pains au raisin',data: [11, 12, 16, 11, 20, 23]},
				{name: 'Brioches',data: [null, null, 8, 12, 15, 21]}],
			       responsive: {
				   rules: [{condition: {maxWidth: 500},
					    chartOptions: {legend: {layout: 'horizontal',align: 'center',verticalAlign: 'bottom'}}
					   }]
			       }
			      }
		);
*/
