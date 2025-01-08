# 问卷调查分析工具

一个用于分析和可视化问卷调查数据的Python工具包。

## 主要功能

- 人口统计学数据分析
- 李克特量表数据分析 
- 数据可视化
- 相关性分析

## 安装

```bash
pip install survey-analyzer
```

## 使用

```python
from survey_analyzer import SurveyAnalyzer
```

## 示例

```python
# 创建分析器实例
analyzer = SurveyAnalyzer("survey_data.csv")

# 设置列类型
demographic_cols = ['age', 'gender', 'education']
likert_cols = ['q1', 'q2', 'q3', 'q4', 'q5']
analyzer.set_column_types(demographic_cols, likert_cols)

# 分析人口统计学数据
demo_results = analyzer.analyze_demographics()
print("人口统计分析结果:")
for col, results in demo_results.items():
    print(f"\n{col} 统计:")
    print(results['counts'])

# 分析李克特量表数据
likert_results = analyzer.analyze_likert()
print("\n李克特量表分析结果:")
print(likert_results)

# 可视化
from survey_analyzer import SurveyVisualizer
visualizer = SurveyVisualizer(analyzer.data)

# 绘制人口统计图表
visualizer.plot_demographics('gender')

# 绘制李克特量表响应分布
visualizer.plot_likert('q1')

# 绘制相关性矩阵
visualizer.correlation_matrix(likert_cols)
```

## 依赖

- pandas
- numpy
- matplotlib
- seaborn
- jupyter

## 开发环境设置

1. 克隆仓库
```bash
git clone https://github.com/yourusername/survey-analyzer.git
cd survey-analyzer
```

2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

## 许可证

MIT License

## 贡献指南

欢迎提交 Issue 和 Pull Request！
