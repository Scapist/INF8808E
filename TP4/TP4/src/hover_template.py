'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip
    country = '<span style="font-weight: bold">Country : </span><span style="font-weight: normal">%{customdata[0]}</span><br>'
    population = '<span style="font-weight: bold">Population : </span><span style="font-weight: normal">%{customdata[1]}</span><br>'
    gdp = '<span style="font-weight: bold">GDP : </span><span style="font-weight: normal">%{x} $ (USD)</span><br>'
    co2_emissions = '<span style="font-weight: bold">CO2 emissions : </span><span style="font-weight: normal">%{y} metric tonnes</span><br>'
    return country + population + gdp + co2_emissions + '<extra></extra>'
