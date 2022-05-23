'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import plotly.graph_objects as go
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    empty_scatter_trace = go.Scatter(x=[], y=[])
    empty_axis_layout = {
        'ticks': '',
        'showticklabels': False,
        'zeroline': False,
        'showgrid': False,
        'showline': False,
        'autorange': True,
    }
    no_data_annotation = {
        'text': 'No data to display. Select a cell in the heatmap for more information.',
        'x': 0,
        'y': 0,
        'showarrow': False,
    }

    layout = go.Layout(
        dragmode=False,
        xaxis=empty_axis_layout,
        yaxis=empty_axis_layout,
        showlegend=False,
        annotations=[no_data_annotation],
    )

    fig = go.Figure(data=[empty_scatter_trace], layout=layout)
    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    return None


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    scatter_mode = 'markers' if len(line_data) == 1 else 'lines'
    scatter_trace = go.Scatter(
        x=line_data['Date_Plantation'],
        y=line_data['Counts'],
        mode=scatter_mode,
    )
    fig = go.Figure(
        data=[scatter_trace],
        layout_title_text=f"Trees planted in {arrond} in {year}",
    )
    fig.update_yaxes(title_text="Trees")
    fig.update_xaxes(tickformat="%d %b", tickangle=-45)
    fig.update_traces(hovertemplate=hover_template.get_linechart_hover_template())
    
    return fig
