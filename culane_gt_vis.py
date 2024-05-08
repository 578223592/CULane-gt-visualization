import cv2
import numpy as np
import os
import glob


# 이미지와 좌표 파일 경로
# image_path = '/home/jua/다운로드/CULane/driver_37_30frame/05181432_0203.MP4/02520.jpg'
# txt_path = '/home/jua/다운로드/CULane/driver_37_30frame/05181432_0203.MP4/02520.lines.txt'


def draw_lane(image, lines):
    # 좌표에 따라 차선 그리기
    for line in lines:
        for i in range(len(line) - 1):
            start_point = (int(line[i][0]), int(line[i][1]))
            end_point = (int(line[i + 1][0]), int(line[i + 1][1]))
            cv2.line(image, start_point, end_point, (0, 255, 0), 2)

    return image


def read_coords(txt_path):
    # .txt 파일에서 차선 좌표 읽기
    lines = []
    with open(txt_path, "r") as file:
        for line in file:
            coords = line.strip().split()
            line_coords = []
            for i in range(0, len(coords), 2):
                x, y = float(coords[i]), float(coords[i + 1])
                if y > 0:  # 유효한 좌표인 경우에만 추가
                    line_coords.append((x, y))
            lines.append(line_coords)
    return lines


def load_test_list(test_list_path: str) -> set:
    test_list_set = set()
    with open(test_list_path, "r") as file:
        for line in file:
            test_list_set.add(line.strip())
    return test_list_set

def IsImgInsImgInTestList(image_path, test_list_set):
    # 使用 split() 方法拆分字符串
    parts = image_path.split("/driver")

    # 获取以 "/driver" 开始的部分，并重新添加 "/driver" 前缀
    result = "/driver" + parts[1]
    return result in test_list_set
def process_images(input_folder, output_folder, only_test_pic: bool):
    # input_folder 내의 모든 .jpg 파일을 검색
    if only_test_pic:
        test_list_set = load_test_list(os.path.join(input_folder, "list/test.txt"))
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # 检查文件是否以.jpg结尾
            if file.endswith(".jpg"): ##lanseg 以.png结尾 会被滤除掉
                image_path = os.path.join(root, file)

                base_name = os.path.basename(image_path)
                txt_path = image_path.replace(".jpg", ".lines.txt")

                # .lines.txt 파일이 있는지 확인
                if os.path.exists(txt_path):
                    if only_test_pic and not IsImgInsImgInTestList(image_path, test_list_set):
                        continue
                    print(txt_path)
                    image = cv2.imread(image_path)
                    lines = read_coords(txt_path)
                    lane_image = draw_lane(image, lines)

                    # output
                    output_path = image_path.replace(input_folder, output_folder)
                    # 确保输出文件夹存在，如果不存在，则创建它
                    if not os.path.exists(os.path.dirname(output_path)):
                        os.makedirs(os.path.dirname(output_path))
                    cv2.imwrite(output_path, lane_image)


if __name__ == "__main__":

    input_folder = "/small_datasets/swx/dataset/culane/unzip/"
    output_folder = "/small_datasets/swx/dataset/culane/gt_vis/"
    only_test_pic = True  #only ouput test pic or not
    # 처리 함수 호출
    process_images(input_folder, output_folder, only_test_pic)
