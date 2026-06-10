try:
    import numpy as np

    if not hasattr(np, "trapz") and hasattr(np, "trapezoid"):
        np.trapz = np.trapezoid
except Exception:
    pass
