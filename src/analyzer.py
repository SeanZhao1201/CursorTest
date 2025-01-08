import pandas as pd
from typing import List, Dict

class SurveyAnalyzer:
    def __init__(self, data_path: str):
        """
        初始化问卷分析器
        
        Args:
            data_path: 数据文件路径（CSV格式）
        """
        self.df = pd.read_csv(data_path)
        self.demographic_cols = []
        self.likert_cols = []
        
    def set_column_types(self, demographic_cols: List[str], likert_cols: List[str]):
        """设置列的类型（人口统计学或李克特量表）"""
        self.demographic_cols = demographic_cols
        self.likert_cols = likert_cols
        
    def analyze_demographics(self) -> Dict:
        """分析人口统计学数据"""
        results = {}
        for col in self.demographic_cols:
            results[col] = {
                'counts': self.df[col].value_counts(),
                'percentages': self.df[col].value_counts(normalize=True) * 100
            }
        return results
    
    def analyze_likert(self) -> pd.DataFrame:
        """分析李克特量表数据"""
        likert_stats = self.df[self.likert_cols].agg([
            'count', 'mean', 'std', 'median'
        ])
        return likert_stats
    
    @property
    def data(self) -> pd.DataFrame:
        """获取数据框"""
        return self.df 