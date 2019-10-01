var dom = document.getElementById("container");
var myChart = echarts.init(dom);
var app = {};
option = null;

function randomData() {
    now = new Date(+now + oneDay);
    value = value + Math.random() * 21 - 10;
    return {
        name: now.toString(),
        value: [
            [now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'),
            Math.round(value)
        ]
    }
}

var data = [];
var now = +new Date(1997, 9, 3);
var oneDay = 24 * 3600 * 1000;
var value = Math.random() * 1000;
for (var i = 0; i < 1000; i++) {
    data.push(randomData());
}

option = {
    title: {
        text: '动态数据 + 时间坐标轴'
    },
    tooltip: {
        trigger: 'axis',
        formatter: function (params) {
            params = params[0];
            var date = new Date(params.name);
            return date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear() + ' : ' + params.value[1];
        },
        axisPointer: {
            animation: false
        }
    },
    xAxis: {
        type: 'time',
        splitLine: {
            show: false
        }
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '100%'],
        splitLine: {
            show: false
        }
    },
    series: [{
        name: '模拟数据',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: data
    }]
};

setInterval(function () {

    // 调用  index.js  方法来交互  不符合 代码规范
    // echart_data = getCurrentFrames()

    // 当我们的视频播放的时候 才向后台请求数据 播放
    if (video.paused == false) {
        console.log(
            "播放数据  嘻嘻"
        )

        getCurrentFrames()
    }

    for (var i = 0; i < 5; i++) {
        data.shift();
        li_data = randomData();
        data.push(li_data);
    }

    myChart.setOption({
        series: [{
            data: data
        }]
    });


}, 1000);
;

if (option && typeof option === "object") {
    myChart.setOption(option, true);
}