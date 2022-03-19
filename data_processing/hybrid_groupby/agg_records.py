import pandas as pd 

def hybrid_groupby(df, grp_cols, sum_cols=[], avg_cols=[], min_cols=[], max_cols=[]): 
    """The purpose of this function is to replicate the functionality of a SQL GROUP BY clause. 
       Takes a DataFrame, a list of grouping columns, a few lists of columns to operate on, and 
       returns the aggregated data after applying the appropriate operators. Takes the first value 
       for ignored fields. Returns a DataFrame."""
    
    sum_df = df[grp_cols + sum_cols].groupby(grp_cols, as_index=False).sum()
    avg_df = df[grp_cols + avg_cols].groupby(grp_cols, as_index=False).mean()
    min_df = df[grp_cols + min_cols].groupby(grp_cols, as_index=False).min()
    max_df = df[grp_cols + max_cols].groupby(grp_cols, as_index=False).max()
    
    agg_cols = sum_cols + avg_cols + min_cols + max_cols
    df = df.drop_duplicates(subset=grp_cols, keep='first').copy()
    df.drop(columns=agg_cols, inplace=True)
    
    df = df.merge(sum_df).merge(avg_df).merge(min_df).merge(max_df)
    
    return df
