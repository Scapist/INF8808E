'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # Draw the map base
    new_trace = go.Choroplethmapbox(
      geojson=montreal_data,
      locations=locations,
      z=z_vals,
      colorscale=colorscale,
      marker_line_color='white',
      showscale=False,
      featureidkey='properties.NOM',
    )
    fig.add_trace(new_trace)
    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # Add the scatter markers to the map base
    data_label = 'properties.TYPE_SITE_INTERVENTION'
    every_type_site_intervention = street_df.groupby([data_label]).groups.keys()
    for type_site_intervention in every_type_site_intervention:
      row = street_df.loc[street_df[data_label] == type_site_intervention]
      new_trace = go.Scattermapbox(
        lon=row['properties.LONGITUDE'],
        lat=row['properties.LATITUDE'],
        text=row[data_label],
        name=type_site_intervention,
        showlegend=True,
        marker=go.scattermapbox.Marker(size=10, opacity=0.5),
      )
      fig.add_trace(new_trace)
    return fig
