import numpy as np
from sklearn.cluster import KMeans

def getImageMainColor(image):
    # 获取图像的形状信息
    height, width, channels = image.shape
    # # 将图像数据重塑为二维数组，每行代表一个像素，每列代表一个通道
    data = image.reshape((height * width, channels))
    # # 创建KMeans聚类器，指定簇数为5
    kmeans = KMeans(n_clusters=5, max_iter=1, init='k-means++', n_init=1)
    # 训练模型
    kmeans.fit(data)
    # 获取聚类中心点，即每个簇的平均颜色
    centroids = kmeans.cluster_centers_
    colors = []
    for item in centroids:
        colors.append(np.full((50, 200, 3), item/255))
    return (centroids, colors)

# 分析图片
def analysisImage(image):
    (centroids, colors) = getImageMainColor(image)
    return centroids[0], centroids[1], centroids[2], centroids[3], centroids[4], colors
