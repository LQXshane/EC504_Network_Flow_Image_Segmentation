###Kmeans Clustering

We utilized kmeans clustering in cv2 library:
> Color Quantization is the process of reducing number of colors in an image. One reason to do so is to reduce the memory. Sometimes, some devices may have limitation such that it can produce only limited number of colors. In those cases also, color quantization is performed. Here we use k-means clustering for color quantization.
> There is nothing new to be explained here. There are 3 features, say, R,G,B. So we need to reshape the image to an array of Mx3 size (M is number of pixels in image). And after the clustering, we apply centroid values (it is also R,G,B) to all pixels, such that resulting image will have specified number of colors. And again we need to reshape it back to the shape of original image.

Some visuals in examples folder:
2.jpg: choose cluster number K = 2, e.g. the resulting image would only have two RGB numbers
8.jpg, where K = 8