from cv2 import *
def main():
    print("<<<<<<<Hello Computer Vision>>>>>>>>");
    print(cv2.__version__);
    imagespath="lena_color_256.tif";
    images=imread(imagespath);
    namedWindow("lena",WINDOW_AUTOSIZE)
    imshow("leena",images);#show images
    waitKey(0);#waits for the keyboard event
    destroyAllWindows();
if __name__=="__main__":
    main()
