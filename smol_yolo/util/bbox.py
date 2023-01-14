from typing import Tuple


def rel_xywh_to_abs_min_max(x: float, y: float, w: float, h: float, hw: Tuple[int, int]) -> Tuple[int, int, int, int]:
    """Converts relative x,y,w,h to x_min, y_min, x_max, y_max

    Args:
        x (float): x coordinate
        y (float): y coordinate
        w (float): width
        h (float): height
        hw (tuple): image size

    Returns:
        tuple: (xmin, ymin, xmax, ymax)
    """
    img_h, img_w = hw
    xmin = int((x - w / 2) * img_w)
    ymin = int((y - h / 2) * img_h)
    xmax = int((x + w / 2) * img_w)
    ymax = int((y + h / 2) * img_h)
    return (xmin, ymin, xmax, ymax)
