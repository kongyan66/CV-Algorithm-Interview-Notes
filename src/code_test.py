# def func(m, n):
#     res = []
#     for i in range(m + 1, n+ 2):
#         res.append(fib(i))
#     print(res)

# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n- 2)

# func(1, 5)

# import cv2
# video_path = "a.mp4"

# capture = cv2.VideoCapture(video_path)
# frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
# frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
# frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)

# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# video_writer = cv2.VideoWriter("b.mp4", fourcc, 25, (1280,720))

# c = 1
# frameRate = 10


# while(True):
# 	ret, frame = capture.read()
# 	if ret:
# 		if(c % frameRate == 0):
# 			print("开始截取视频第：" + str(c) + " 帧")
#             # 保存到本地
#             b, g, r = cv2.split(frame)
#             bH = cv2.equalizeHist(b)
#             gH = cv2.equalizeHist(g)
#             rH = cv2.equalizeHist(r)
#             # 合并每一个通道
#             result = cv2.merge((bH, gH, rH))
# 			cv2.imwrite("./capture_image/" + 'a_' + str(c) + '.jpg', result)  
#             video_writer.write(frame)
# 		c += 1
# 		cv2.waitKey(0)
# 	else:
# 		print("所有帧都已经保存完成")
# 		break


# import cv2

# def resize_keep_aspectratio(image_src, dst_size):
#     src_h, src_w = image_src.shape[:2]
#     print(src_h, src_w)
#     dst_h, dst_w = dst_size

#     # 判断应该按哪个边做等比缩放
#     h = dst_w * (float(src_h) / src_w)  # 按照ｗ做等比缩放
#     w = dst_h * (float(src_w) / src_h)  # 按照h做等比缩放

#     h = int(h)
#     w = int(w)

#     if h <= dst_h:
#         image_dst = cv2.resize(image_src, (dst_w, int(h)))
#     else:
#         image_dst = cv2.resize(image_src, (int(w), dst_h))

#     h_, w_ = image_dst.shape[:2]
#     print(h_, w_)

#     top = int((dst_h - h_) / 2)
#     down = int((dst_h - h_ + 1) / 2)
#     left = int((dst_w - w_) / 2)
#     right = int((dst_w - w_ + 1) / 2)

#     value = [0, 0, 0]
#     borderType = cv2.BORDER_CONSTANT
#     print(top, down, left, right)
#     image_dst = cv2.copyMakeBorder(image_dst, top, down, left, right, borderType, None, value)

#     return image_dst

# if __name__ == '__main__':
#     image_src = cv2.imread(r"./000167.jpg")
#     dst_size = (256, 256)
#     image = resize_keep_aspectratio(image_src, dst_size)
#     image =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     print(image.shape)
#     if 27 == cv2.waitKey():
#         cv2.destroyAllWindows()
#     cv2.imwrite(r"./3.jpg",image,[cv2.IMWRITE_JPEG_QUALITY, 40])
# title = ['name', 'age', 'height', 'weight']
# with open("a.txt", "r") as f:
#     res = []
#     i = 0
#     data = f.readlines()
#     ans =[]
#     for line in data[1:]:
#         line = line.strip('\n')  #去掉列表中每一个元素的换行符
#         res = list(line.split(' '))
#         ans.append(res)
#     ans.sort(key=lambda x:x[2])
#     ans.insert(0, title)
#     output_file =open('a.txt', "w+")
#     for line in ans:
#         tem = ' '.join(line)
#         print(tem)
#         output_file.write(tem)
#         output_file.write('\n')

# with open("a.txt", "r") as f:
#     res = []
#     for line in f.readline():
#         line = line.strip('\n')
#         print(line)


class Solution2:
    def __init__(self):
        self.path = []
        self.result = []
        # 因为有重复元素，本题需要使用used，用来标记区别同一树层的元素使用重复情况，注意区分递归纵向遍历遇到的重复元素，和for循环遇到的重复元素
        
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        self.backtracking(candidates, target, 0)
        return self.result

    def backtracking(self, candidates, target, startindex):
        # 2.确定递归停止条件
        if sum(self.path) == target:
            self.result.append(self.path.copy())
            return 
        if sum(self.path) > target:
            return
        # 3.确定单层递归逻辑
        use = set()
        for i in range(len(candidates)):
            # if i > 0 and candidates[i] == candidates[i-1] and self.used[i-1] == False:
            #     continue
            if candidates[i] in use:
                continue
            self.path.append(candidates[i])
            use.add(candidates[i])
            self.backtracking(candidates, target, i+1)
            self.path.pop()
        
if __name__ == '__main__':
    su = Solution2()
    ans = su.combinationSum2([1, 2, 5], 100)
    print(len(ans))