# coding:utf-8
import plotly
import plotly.graph_objs as go

import pprint


def draw_chart(x_data, y_data):
    title = 'CPU and RAM'

    labels = ['CPU', 'Mem']

    colors = ['rgba(67,67,67,1)', 'rgba(115,115,115,1)', 'rgba(49,130,189, 1)', 'rgba(189,189,189,1)']

    mode_size = [8, 8, 12, 8]

    line_size = [2, 2, 4, 2]

    x_data = x_data[0:2]

    # x_data = [
    #     [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
    #     [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
    #     [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
    #
    # ]

    # y_data = [
    #     [74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 69], #CPU
    #     [45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28], #Mem
    #     [13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
    #
    # ]

    traces = []

    for i in range(0, len(x_data)):
        traces.append(go.Scatter(
            x=x_data[i],
            y=y_data[i],
            mode='lines',
            line=dict(color=colors[i], width=line_size[i]),
            connectgaps=True,
        ))

        traces.append(go.Scatter(
            x=[x_data[i][0], x_data[i][len(x_data[0]) - 1]],
            y=[y_data[i][0], y_data[i][len(y_data[0]) - 1]],
            mode='markers',
            marker=dict(color=colors[i], size=mode_size[i])
        ))

    layout = go.Layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            autotick=False,
            ticks='outside',
            tickcolor='rgb(204, 204, 204)',
            tickwidth=2,
            ticklen=5,
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=False,
        margin=dict(
            autoexpand=False,
            l=100,
            r=20,
            t=110,
        ),
        showlegend=False,
    )

    annotations = []

    # Adding labels
    for y_trace, label, color in zip(y_data, labels, colors):
        # labeling the left_side of the plot
        annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                xanchor='right', yanchor='middle',
                                text=label + ' {}%'.format(y_trace[0]),
                                font=dict(family='Arial',
                                          size=16,
                                          color=colors, ),
                                showarrow=False))
        # labeling the right_side of the plot
        annotations.append(dict(xref='paper', x=0.95, y=y_trace[len(y_data[0]) - 1],
                                xanchor='left', yanchor='middle',
                                text='{}%'.format(y_trace[len(y_data[0]) - 1]),
                                font=dict(family='Arial',
                                          size=16,
                                          color=colors, ),
                                showarrow=False))
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                            xanchor='left', yanchor='bottom',
                            text='CPU and RAM ',
                            font=dict(family='Arial',
                                      size=30,
                                      color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                            xanchor='center', yanchor='top',
                            text='Source: PewResearch Center & ' +
                                 'Storytelling with data',
                            font=dict(family='Arial',
                                      size=12,
                                      color='rgb(150,150,150)'),
                            showarrow=False))

    layout['annotations'] = annotations

    fig = go.Figure(data=traces, layout=layout)
    plotly.offline.plot(fig, filename='news-source')


if __name__ == '__main__':
    draw_chart(12, 2)
