import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict

class SurveyAnalyzer:
    def __init__(self, data_path: str):
        """
        初始化问卷分析器
        
        Args:
            data_path: 数据文件路径（CSV格式）
        """
        self.df = pd.read_csv(data_path)
        self.demographic_cols = []  # 存储人口统计学变量
        self.likert_cols = []      # 存储李克特量表变量
        
    def set_column_types(self, demographic_cols: List[str], likert_cols: List[str]):
        """
        设置列的类型（人口统计学或李克特量表）
        
        Args:
            demographic_cols: 人口统计学变量列表
            likert_cols: 李克特量表变量列表
        """
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
    
    def plot_demographics(self, column: str):
        """
        绘制人口统计学数据的可视化图表
        
        Args:
            column: 要绘制的人口统计学变量
        """
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df, x=column)
        plt.title(f'{column} Distribution')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def analyze_likert(self) -> pd.DataFrame:
        """分析李克特量表数据"""
        likert_stats = self.df[self.likert_cols].agg([
            'count', 'mean', 'std', 'median'
        ])
        return likert_stats
    
    def plot_likert(self, column: str):
        """
        绘制李克特量表数据的可视化图表
        
        Args:
            column: 要绘制的李克特量表变量
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x=column, bins=len(self.df[column].unique()))
        plt.title(f'{column} Response Distribution')
        plt.xlabel('Response')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.show()
        
    def correlation_matrix(self):
        """绘制李克特量表项目之间的相关性矩阵"""
        corr = self.df[self.likert_cols].corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Matrix of Likert Items')
        plt.tight_layout()
        plt.show()

# 使用示例
if __name__ == "__main__":
    # 创建分析器实例
    analyzer = SurveyAnalyzer("survey_data.csv")
    
    # 设置列类型
    demographic_cols = ['age', 'gender', 'education']
    likert_cols = ['q1', 'q2', 'q3', 'q4', 'q5']
    analyzer.set_column_types(demographic_cols, likert_cols)
    
    # 分析人口统计学数据
    demo_results = analyzer.analyze_demographics()
    print("Demographic Analysis:")
    for col, results in demo_results.items():
        print(f"\n{col.upper()} Statistics:")
        print(results['counts'])
        
    # 绘制人口统计学图表
    analyzer.plot_demographics('gender')
    
    # 分析李克特量表数据
    likert_results = analyzer.analyze_likert()
    print("\nLikert Scale Analysis:")
    print(likert_results)
    
    # 绘制李克特量表图表
    analyzer.plot_likert('q1')
    
    # 绘制相关性矩阵
    analyzer.correlation_matrix() 