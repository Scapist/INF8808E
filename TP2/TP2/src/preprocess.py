'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # Group by act and player
    my_df = my_df.groupby(by=['Act', 'Player']).count()
    # Transform one of the columns to a LineCount column
    my_df = my_df.rename(columns={'PlayerLine': 'LineCount'})
    # Remove the Scene and Line column
    my_df = my_df.drop(columns=['Scene', 'Line'])
    # Add percentage per player per act
    my_df['LinePercent'] = (my_df['LineCount'] / my_df.groupby('Act').sum()['LineCount']) * 100
    # Ungroup the dataframe
    my_df = my_df.reset_index()
    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # Find the top 5 players
    top_5_index = my_df.groupby(by='Player').sum().nlargest(5, 'LineCount').index.tolist()
    output_df = pd.DataFrame()
    # Loop over each group:
    for act, group in my_df.groupby(by='Act'):
      # Keep the top 5 players
      top_5_group = group[group['Player'].isin(top_5_index)]
      # Group the other players
      other_group = group[~group['Player'].isin(top_5_index)]
      # Merge other_group into a single line
      other_df = pd.DataFrame(data={
        'Act': [act],
        'Player': ['OTHER'],
        'LineCount': [other_group['LineCount'].sum()],
        'LinePercent': [other_group['LinePercent'].sum()],
      })
      # Merge top_5_group and other_df
      combined_group = pd.concat([top_5_group, other_df], ignore_index=True)
      # Add the group to the output_df
      output_df = pd.concat([output_df, combined_group], ignore_index=True)
      
    return output_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # Capitalize Player names
    my_df['Player'] = my_df['Player'].str.title()
    
    return my_df
