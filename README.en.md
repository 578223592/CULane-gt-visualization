# CULane-gt-visualization

## Purpose

Visualization of ground truth for lane detection using the CULane dataset.
Output example:
![image](https://github.com/578223592/CULane-gt-visualization/assets/65906820/f57d5385-3f49-40cf-b1e9-cea45c6de364)


## Usage




1. Clone this repository.
2. Prepare the CULane dataset, stored in a common way.
  Here is how I organize it:
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

4. Modify the values of the input_folder and output_folder variables in the code. `input_folder` is the location of the CULane dataset, and `output_folder` is the location where you want to output the visualization results.

Here is how I do it:
```python
    input_folder = '/small_datasets/swx/dataset/culane/unzip/'
    output_folder = '/small_datasets/swx/dataset/culane/gt_vis/'
```

5. Run the code, and the results will be output in the `ouput_folder` directory, organized in the same way as the original dataset.



## Acknowledgements
- https://github.com/Claire-art/CULane-gt-visualization/blob/main/viscu.py
