import torch 
import pandas as pd 

import torch.nn as nn 
import torch.nn.functional as F 
from torch.utils.data import Dataset

class UIT_VFSC(Dataset): 
    def __init__(self, file_dir): 
        super().__init__() 
        
        self.folder_dir = file_dir


        