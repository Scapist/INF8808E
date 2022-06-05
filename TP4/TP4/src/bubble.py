'''
    This file contains the code for the bubble plot.
'''

import plotly.express as px

import hover_template


def get_plot(my_df, gdp_range, co2_range):
    '''
        Generates the bubble plot.

        The x and y axes are log scaled, and there is
        an animation between the data for years 2000 and 2015.

        The markers' maximum size is 30 and their minimum
        size is 5.

        Args:
            my_df: The dataframe to display
            gdp_range: The range for the x axis
            co2_range: The range for the y axis
        Returns:
            The generated figure
    '''
    # TODO : Define figure with animation
    fig = px.scatter(my_df,
                     x='GDP',
                     y='CO2',
                     animation_frame='Year',
                     animation_group='Country Name',
                     range_x=gdp_range,
                     range_y=co2_range,
                     log_x=True,
                     log_y=True,
                     size='Population',
                     size_max=30,
                     color='Continent',
                     custom_data=['Country Name', 'Population'],
                     )
    fig.update_traces(marker=dict(sizemin=5))
    return fig


def update_animation_hover_template(fig):
    '''
        Sets the hover template of the figure,
        as well as the hover template of each
        trace of each animation frame of the figure

        Args:
            fig: The figure to update
        Returns:
            The updated figure
    '''

    # TODO : Set the hover template

    fig.update_traces(hovertemplate=hover_template.get_bubble_hover_template())

    # Taken from https://github.com/plotly/plotly.py/issues/2722
    for frame in fig.frames:
        for data in frame.data:
            data.hovertemplate = hover_template.get_bubble_hover_template()
    return fig


def update_animation_menu(fig):
    '''
        Updates the animation menu to show the current year, and to remove
        the unnecessary 'Stop' button.

        Args:
            fig: The figure containing the menu to update
        Returns
            The updated figure
    '''
    # TODO : Update animation menu

    menu_dict = [{
        'buttons': [{
            'args': [None],
            'label': 'Animate',
            'method': 'animate',
        },
        {
            'visible': False,
        }]
    }]

    slider_dict = [{
        'currentvalue': {
            'prefix': 'Data for year: ',
            'visible': True
        }
    }]

    fig.update_layout(sliders=slider_dict)
    fig.update_layout(updatemenus=menu_dict)
    return fig

def update_axes_labels(fig):
    '''
        Updates the axes labels with their corresponding titles.

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    # TODO : Update labels
    fig.update_layout(xaxis_title_text='GDP per capita ($ USD)',
                      yaxis_title_text='CO2 emissions per capita (metric tonnes)')
    return fig


def update_template(fig):
    '''
        Updates the layout of the figure, setting
        its template to 'simple_white'

        Args:
            fig: The figure to update
        Returns
            The updated figure
    '''
    # TODO : Update template
    fig.update_layout(template='simple_white')
    return fig


def update_legend(fig):
    '''
        Updated the legend title

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    # TODO : Update legend
    fig.update_layout(legend_title_text='Legend')
    return fig
