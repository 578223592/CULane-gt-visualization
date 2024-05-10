# CULane-gt-visualization

## 用处

用于车道线检测的CULane数据集真值的可视化。
输出结果：
![image](https://github.com/578223592/CULane-gt-visualization/assets/65906820/f57d5385-3f49-40cf-b1e9-cea45c6de364)


## 用法

1. 克隆本仓库
2. 准备好CULane数据集，通用存放方式即可。
  我的存放方式展示
```
(base) xxx@xxxx:/small_datasets/swx/dataset/culane/unzip$ tree -L 1 ./
./
├── driver_100_30frame
├── driver_161_90frame
├── driver_182_30frame
├── driver_193_90frame
├── driver_23_30frame
├── driver_37_30frame
├── laneseg_label_w16
└── list

```

4. 修改代码中input_folder output_folder变量的值。input_folder是CULane数据集位置，output_folder是你想输出的可视化结果的位置。

我的展示：
```python
    input_folder = '/small_datasets/swx/dataset/culane/unzip/'
    output_folder = '/small_datasets/swx/dataset/culane/gt_vis/'
```

5. 运行即可，结果会输出在ouput_folder文件夹中，组合方式和原数据集相同。



## 感谢
- https://github.com/Claire-art/CULane-gt-visualization/blob/main/viscu.py
