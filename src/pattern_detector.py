
import pandas as pd

def detect_cup_and_handle(data, window=20):
    """
    Detect cup and handle patterns in stock price data.

    Parameters:
    - data (DataFrame): DataFrame containing 'close' price column.
    - window (int): Number of bars before and after center point to consider for peaks and bottom.

    Returns:
    - DataFrame of detected pattern points with timestamps and price levels.
    """

    patterns = []

    if 'close' not in data.columns:
        raise ValueError("Data must contain a 'close' column.")

    for i in range(window, len(data) - window):
        window_data = data['close'].iloc[i - window:i + window]

        left_peak = window_data.iloc[:window].max()
        cup_bottom = window_data.iloc[window - 5:window + 5].min()
        right_peak = window_data.iloc[window:].max()

        if (left_peak > cup_bottom) and (right_peak > cup_bottom):
            patterns.append({
                'timestamp': data.index[i],
                'left_peak': left_peak,
                'cup_bottom': cup_bottom,
                'right_peak': right_peak
            })

    return pd.DataFrame(patterns)
