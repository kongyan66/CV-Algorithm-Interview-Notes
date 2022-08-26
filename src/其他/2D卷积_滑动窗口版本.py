import numpy as np

class my_conv2d(object):
    def __init__(self, input_data, weight_data, stride, padding = "SAME"):
        self.input = np.asarray(input_data, np.float32)
        self.weight = np.asarray(weight_data, np.float32)
        self.stirde = stride
        self.padding = padding

    def conv2d(self):
        [c, h, w] = self.input.shape
        [kc, k, _] = self.weight.shape

        assert c == kc
        output = []

        # 分离通道，最后加起来
        for i in range(c):
            f_map = self.input[i]
            k_map = self.weight[i]
            res = self.compute_conv2d(f_map, k_map) 
            if output == []:
                output = res
            else:
                output += res
        return output

    def compute_conv2d(self, fm, kernel):
        # 单通道矩阵
        [h, w] = fm.shape
        [k, _] = kernel.shape
        
        # 根据不同模式，分别对计算填充和输出矩阵的尺寸
        # 模式一：输出尺寸不变，则需要对输入矩阵进行填充
        if self.padding == 'SAME':
            # 计算要填充的宽度和高度
            pad_h = (self.stirde * (h - 1) + (k - h)) // 2
            pad_w = (self.stirde * (w -1) + (k - w)) // 2
            # 输出尺寸不变
            res_h = h
            res_w = w
        elif self.padding == 'VALID':
            pad_h = 0
            pad_w = 0
            res_h = (h - k) // self.stirde + 1
            res_w = (w - k) // self.stirde + 1
        
        # 对输入矩阵进行填充
        padding_fm = np.zeros([h + 2 * pad_h, w + 2 * pad_w], np.float32)
        padding_fm[pad_h:pad_h+ h, pad_w:pad_w+w] = fm
        # 计算输出矩阵
        res = np.zeros([res_h, res_w], np.float32)
        for i in range(res_h):
            for j in range(res_w):
                # 切片要计算的矩阵快
                roi = padding_fm[i * self.stirde:(i * self.stirde + k), j * self.stirde:(j * self.stirde + k)]
                res[i, j] = np.sum(roi * kernel)
        return res


 
if __name__ == '__main__':

    input_data = [
        [
            [1, 0, 1, 2, 1],
            [0, 2, 1, 0, 1],
            [1, 1, 0, 2, 0],
            [2, 2, 1, 1, 0],
            [2, 0, 1, 2, 0],
        ],
        [
            [2, 0, 2, 1, 1],
            [0, 1, 0, 0, 2],
            [1, 0, 0, 2, 1],
            [1, 1, 2, 1, 0],
            [1, 0, 1, 1, 1],

        ],
    ]
    weight_data = [
        [
            [1, 0, 1],
            [-1, 1, 0],
            [0, -1, 0],
        ],
        [
            [-1, 0, 1],
            [0, 0, 1],
            [1, 1, 1],
        ]
    ]
    my_conv = my_conv2d(input_data, weight_data, 1, 'SAME')
    print(my_conv.conv2d())
        
