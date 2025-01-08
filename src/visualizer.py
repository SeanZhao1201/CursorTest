import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List
import pandas as pd

class SurveyVisualizer:
    def __init__(self, data: pd.DataFrame):
        """
        初始化可视化器
        
        Args:
            data: 包含调查数据的DataFrame
        """
        self.df = data
        
    def plot_demographics(self, column: str, figsize: tuple = (10, 6)):
        """绘制人口统计学数据的可视化图表"""
        plt.figure(figsize=figsize)
        sns.countplot(data=self.df, x=column)
        plt.title(f'{column} Distribution')
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt
        
    def plot_likert(self, column: str, figsize: tuple = (10, 6)):
        """绘制李克特量表数据的可视化图表"""
        plt.figure(figsize=figsize)
        sns.histplot(data=self.df, x=column, bins=len(self.df[column].unique()))
        plt.title(f'{column} Response Distribution')
        plt.xlabel('Response')
        plt.ylabel('Count')
        plt.tight_layout()
        return plt
        
    def correlation_matrix(self, columns: Optional[List[str]] = None, figsize: tuple = (12, 8)):
        """绘制相关性矩阵"""
        if columns is None:
            corr = self.df.corr()
        else:
            corr = self.df[columns].corr()
            
        plt.figure(figsize=figsize)
        sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Matrix')
        plt.tight_layout()
        return plt 