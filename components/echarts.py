import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import time

def forecast_line(df):
    option = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "cross"
            }
        },

        "legend": {
            'top': 'top',
            'left': 'right',
        },
        "xAxis": {
            "type": "category",
            "data": df['Waktu'].tolist()
        },

        "yAxis": {
            "type": "value"
        },

        "dataZoom": [
            {"type": "inside"},
            {"type": "slider"}
        ],
        "series": [{
            "name": "Inflasi",
            "type": "line",
            "data": df['Aktual'].tolist(),
            "smooth": True,
            "showSymbol": True,
            "symbolSize": 6,
            "hoverAnimation": True,
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"
        }, 
        {
            "name": "Forecast",
            "type": "line",
            "data": df['Forecast'].tolist(),
            "smooth": True,
            "lineStyle": {'color': 'red', 'type':'dashed'},
            "hoverAnimation": True,
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"
        }],
    }
    return st_echarts(options=option, height=400)    

def prophet_line_forecast(df):
    option = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "cross"
            }
        },

        "legend": {
            'top': 'top',
            'left': 'right'
        },

        "xAxis": {
            "type": "category",
            "data": df['Waktu'].astype(str).tolist(),
        },

        "yAxis": {
            "type": "value",
        },

        "dataZoom": [
            {"type": "inside"},
            {"type": "slider"}
        ],

        "series": [
            {
            "name": "Forecast (%)",
            "type": "line",
            "data": df['Forecast'].tolist(),
            "smooth": True,
            "showSymbol": True,
            "hoverAnimation": True,
            "lineStyle": {'color': 'blue'},
            "areaStyle": {},
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"
            }, 
            {
            "name": "Lower Bound (%)",
            "type": "line",
            "data": df['Batas Bawah'].tolist(),
            "smooth": True,
            "showSymbol": False,
            "hoverAnimation": True,
            "lineStyle": {'color': 'black', 'type':'dashed', 'width':1},
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"                
            },
            {
            "name": "Upper Bound (%)",
            "type": "line",
            "data": df['Batas Atas'].tolist(),
            "smooth": True,
            "showSymbol": False,
            "hoverAnimation": True,
            "lineStyle": {'color': 'red', 'type':'dashed', 'width':1},
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"
            }
        ]
    }
    return st_echarts(options=option, height=400)

def demo_line(df):
    option = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "cross"
            }
        },

        "legend": {
            'top': 'top',
            'left': 'right',
        },
        "xAxis": {
            "type": "category",
            "data": df['Waktu'].tolist()
        },

        "yAxis": {
            "type": "value"
        },

        "dataZoom": [
            {"type": "inside"},
            {"type": "slider"}
        ],
        "series": [{
            "name": "Inflasi",
            "type": "line",
            "data": df['Aktual'].tolist(),
            "smooth": True,
            "showSymbol": True,
            "symbolSize": 6,
            "hoverAnimation": True,
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"
        }, 
        {
            "name": "Forecast",
            "type": "line",
            "data": df['Forecast'].tolist(),
            "smooth": True,
            "lineStyle": {'color': 'red', 'type':'dashed'},
            "hoverAnimation": True,
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"
        }],
    }

    st_echarts(options=option, height=300)    

def prophet_line_demo(df):
    option = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "cross"
            }
        },

        "legend": {
            'top': 'top',
            'left': 'right'
        },

        "xAxis": {
            "type": "category",
            "data": df['Waktu'].astype(str).tolist(),
        },

        "yAxis": {
            "type": "value",
        },

        "dataZoom": [
            {"type": "inside"},
            {"type": "slider"}
        ],

        "series": [
            {
            "name": "Forecast (%)",
            "type": "line",
            "data": df['Forecast'].tolist(),
            "smooth": True,
            "showSymbol": True,
            "hoverAnimation": True,
            "lineStyle": {'color': 'blue'},
            "areaStyle": {},
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"
            }, 
            {
            "name": "Lower Bound (%)",
            "type": "line",
            "data": df['Batas Bawah'].tolist(),
            "smooth": True,
            "showSymbol": False,
            "hoverAnimation": True,
            "lineStyle": {'color': 'black', 'type':'dashed', 'width':1},
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"                
            },
            {
            "name": "Upper Bound (%)",
            "type": "line",
            "data": df['Batas Atas'].tolist(),
            "smooth": True,
            "showSymbol": False,
            "hoverAnimation": True,
            "lineStyle": {'color': 'red', 'type':'dashed', 'width':1},
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"
            }
        ]
    }
    st_echarts(options=option, height=400)    
    
def line_chart(df, time, data_1, data_2, label_1, label_2):
    series = [
        {
            "name": label_1,
            "type": "line",
            "data": df[data_1].tolist(),
            "smooth": True,
            "showSymbol": True,
            "symbolSize": 6,
            "hoverAnimation": True,
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut"
        }
    ]

    if data_2 is not None:
        series.append({
            "name": label_2,
            "type": "line",
            "data": df[data_2].tolist(),
            "smooth": True,
            "showSymbol": True,
            "symbolSize": 6,
            "hoverAnimation": True,
            "animation": True,
            "animationDuration": 1500,
            "animationEasing": "cubicOut",
            "lineStyle": {
                "color": "red",
                "type": "dashed"
            }
        })

    option = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross"}
        },
        "legend": {
            "top": "top",
            "left": "right"
        },
        "xAxis": {
            "type": "category",
            "data": df[time].tolist()
        },
        "yAxis": {"type": "value"},
        "dataZoom": [
            {"type": "inside"},
            {"type": "slider"}
        ],
        "series": series
    }

    return st_echarts(options=option, height=400)

def bar_chart(df, kategory, data_1, data_2, label_1, label_2):

    series = [
        {
            "name": label_1,
            "type": "bar",
            "data": df[data_1].tolist(),
            "animationDuration": 1000,
            "animationEasing": "cubicOut",
            "animationDelay": "function (idx) { return idx * 150; }",
            "itemStyle": {
                "borderRadius": [6, 6, 0, 0]
            }
        }
    ]

    if data_2 is not None:
        series.append({
            "name": label_2,
            "type": "bar",
            "data": df[data_2].tolist(),
            "animationDuration": 1000,
            "animationEasing": "cubicOut",
            "animationDelay": "function (idx) { return idx * 150; }",
            "itemStyle": {
                "borderRadius": [6, 6, 0, 0]
            }
        })

    option = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "shadow"}
        },
        "legend": {
            "top": "top",
            "right": "0%"
        },
        "xAxis": {
            "type": "category",
            "data": df[kategory].tolist()
        },
        "yAxis": {
            "type": "value"
        },
        "dataZoom": [
            {"type": "inside"},
            {"type": "slider"}
        ],
        "series": series
    }

    return st_echarts(options=option, height=400)

def pie_chart(df, kategory, data, label):

    data_series = [
        {"name": k, "value": v}
        for k, v in zip(df[kategory], df[data])
    ]

    series = [
        {
            "name": label,
            "type": "pie",
            "radius": "60%",
            "data": data_series,
            "animationDuration": 1000,
            "animationEasing": "cubicOut",
            "animationDelay": "function (idx) { return idx * 150; }"
        }
    ]

    option = {
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "top": "top",
            "left": "center"
        },
        "series": series
    }

    return st_echarts(options=option, height=400)

def donut_chart(df, kategory, data, label):

    data_series = [
        {"name": k, "value": v}
        for k, v in zip(df[kategory], df[data])
    ]

    series = [
        {
            "name": label,
            "type": "pie",
            "radius": ["25%", "75%"],
            "data": data_series,
            "animationDuration": 1000,
            "animationEasing": "cubicOut",
            "animationDelay": "function (idx) { return idx * 150; }",
            "label": {
                "formatter": "{b}: {d}%"
            }
        }
    ]

    option = {
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "top": "top",
            "left": "right"
        },
        "series": series
    }

    return st_echarts(options=option, height=400)

def radar_chart(df, kategory, data, label):

    indicator = [
        {"name": k, "max": df[data].max()}
        for k in df[kategory]
    ]

    values = df[data].tolist()

    option = {
        "tooltip": {},
        "legend": {
            "top": "top",
            "left": "right"
        },
        "radar": {
            "indicator": indicator,
            "radius": "65%",

            "splitNumber": 5,

            "splitLine": {
                "lineStyle": {
                    "width": 1
                }
            },

            "splitArea": {
                "show": True
            },

            "axisLine": {
                "lineStyle": {
                    "width": 1
                }
            }
        },

        "series": [
            {
                "name": label,
                "type": "radar",
                "data": [
                    {
                        "value": values,
                        "name": label
                    }
                ],
                "areaStyle": {
                    "opacity": 0.25
                },
                "animationDuration": 1000,
                "animationEasing": "cubicOut"
            }
        ]
    }

    return st_echarts(options=option, height=400)