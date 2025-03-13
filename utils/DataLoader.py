# utils/DataLoader.py
import pandas as pd

def convert(df):
    mapping = {
        "yes": 1, "no": 0,
        "high": 2, "low": 1, "none": 0
    }
    for col in df.iloc[:, :12].columns:
        df[col] = df[col].map(mapping).fillna(df[col])
    return df

def load_data(train_path, test_path, cols_to_drop=None):
    # Load
    train_df = pd.read_pickle(train_path)
    test_df = pd.read_pickle(test_path)
    
    # Drop cột nếu có truyền
    if cols_to_drop is not None:
        train_df = train_df.drop(columns=cols_to_drop, errors='ignore')
        test_df = test_df.drop(columns=cols_to_drop, errors='ignore')
    
    # Convert
    train_df = convert(train_df)
    test_df = convert(test_df)
    
    return train_df, test_df
