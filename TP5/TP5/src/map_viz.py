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
      hovertemplate=hover.map_base_hover_template(),
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
    fig_scatter = px.scatter_mapbox(
        street_df,
        lat="properties.LATITUDE",
        lon="properties.LONGITUDE",
        custom_data=["properties.TYPE_SITE_INTERVENTION", "properties.NOM_PROJET", "properties.MODE_IMPLANTATION", "properties.OBJECTIF_THEMATIQUE"],
        color="properties.TYPE_SITE_INTERVENTION",
    )
    fig_scatter.update_traces(hovertemplate=hover.map_marker_hover_template('%{customdata[0]}'))
    
    fig = go.Figure(fig.data + fig_scatter.data)
    return fig
