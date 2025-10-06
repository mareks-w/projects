import numpy as np

def calculate_cents_error(predicted_hz, reference_hz):
    cents = []
    for p, r in zip(predicted_hz, reference_hz):
        if np.isnan(p) or np.isnan(r) or r == 0:
            cents.append(np.nan)
        else:
            cents.append(1200 * np.log2(p / r))
    return np.array(cents)
