from pathlib import Path
from typing import List, Tuple

from torch.utils.data import Dataset

COCO_ROW_T = Tuple[int, float, float, float, float]


def jpg_to_label(img_path: Path) -> Path:
    path_str = img_path.as_posix()
    label_path_str = path_str.replace("images", "labels").replace(".jpg", ".txt")
    return Path(label_path_str)


def parse_row(row: str) -> COCO_ROW_T:
    label, x, y, w, h = row.split(" ")
    return (int(label), float(x), float(y), float(w), float(h))


def parse_file(label_path: Path) -> List[COCO_ROW_T]:
    rows = label_path.read_text().splitlines()
    return [parse_row(row) for row in rows]


class Coco128(Dataset):
    def __init__(self, dataset_root: Path):
        self.img_files = sorted(dataset_root.glob("**/*.jpg"))
        label_files = [jpg_to_label(img_path) for img_path in self.img_files]
        self.labels = [parse_file(p) for p in label_files]

    def __getitem__(self, index: int) -> None:
        """
        1. Load image
        2. Letterbox
        3. HWC -> CHW, BGR2RGB
        3. Load labels + letterbox
        """
