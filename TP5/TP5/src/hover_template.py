'''
    Provides the templates for the tooltips.
'''


def map_base_hover_template():
    '''
        Sets the template for the hover tooltips on the neighborhoods.

        The label is simply the name of the neighborhood in font 'Oswald'.

        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    neighborhood = '<span style="font-family: Oswald">%{properties.NOM}</span><br>'
    return neighborhood + "<extra></extra>"


def map_marker_hover_template(name):
    '''
        Sets the template for the hover tooltips on the markers.

        The label is simply the name of the walking path in font 'Oswald'.

        Args:
            name: The name to display
        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    name_path = f'<span style="font-family: Oswald">{name}</span><br>'
    return name_path + "<extra></extra>"