Highcharts.chart('container', {
    chart: {
        type: 'bar',
        height: 600
    },
    title: {
        text: 'Données distantes'
    },
    legend: {
        enabled: false
    },
    subtitle: {
        text: 'Données basiques'

    },
    data: {
		csvURL: "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/7_OneCatOneNum_header.csv"
	},
    plotOptions: {
        bar: {
            colorByPoint: true
        },
        series: {
            zones: [{
                color: '#4CAF50',
                value: 1000
            }, {
                color: '#8BC34A',
                value: 2000
            }, {
                color: '#CDDC39',
                value: 3000
            }, {
                color: '#CDDC39',
                value: 4000
            }, {
                color: '#FFEB3B',
                value: 5000
            }, {
                color: '#FFEB3B',
                value: 6000
            }, {
                color: '#FFC107',
                value: 7000
            }, {
                color: '#FF9800',
                value: 8000
            }, {
                color: '#FF5722',
                value: 9000
            }, {
                color: '#F44336',
                value: 10000
            }, {
                color: '#F44336',
                value: Number.MAX_VALUE
            }],
            dataLabels: {
                enabled: true,
                format: '{point.y:.0f}'
            }
        }
    },
    tooltip: {
        valueDecimals: 1,
    },
    xAxis: {
        type: 'category',
        labels: {
            style: {
                fontSize: '10px'
            }
        }
    },
    yAxis: {
        max: 15000,
        title: false,
        plotBands: [{
            from: 0,
            to: 5000,
            color: '#E8F5E9',
       }, {
            from: 5000,
            to: 10000,
            color: '#888888',

        }, {
            from: 10000,
            to: 15000,
            color: '#000000',
        }]
    }
});