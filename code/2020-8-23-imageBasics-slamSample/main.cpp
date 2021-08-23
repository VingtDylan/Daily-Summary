#include <iostream>
#include <chrono>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace std;
using namespace cv;

int main(int argc, char** argv){
    Mat image;
    image = imread(argc > 1 ? argv[1] : "../ubuntu.png");
	//imshow("raw show", image);
    assert(image.data != nullptr);
    
    cout << "cols: " << image.cols << " rows: " << image.rows << " channels: " << image.channels() << endl;
    imshow("image", image);
    waitKey(0);
    
    assert(image.type() == CV_8UC1 || image.type() == CV_8UC3);
    chrono::steady_clock::time_point t1 = chrono::steady_clock::now();
    for(size_t y = 0; y < image.rows; y++){
        unsigned char* row_ptr = image.ptr<unsigned char>(y);
        for(size_t x = 0; x < image.cols; x++){
            unsigned char* data_ptr = &row_ptr[x * image.channels()];
            for(int c = 0; c < image.channels(); c++){
                unsigned char data = data_ptr[c];
            }
        }
    }
    
    chrono::steady_clock:: time_point t2 = chrono::steady_clock::now();
    chrono::duration<double> time_used = chrono::duration_cast<chrono::duration<double>>(t2 - t1);
    cout << "time cost :" << time_used.count() << "seconds" << endl;
    
    Mat imageB = image;
    imageB(Rect(0, 0, 100, 100)).setTo(0);
    imshow("image", imageB);
    waitKey(0);
    
    Mat ImageC = image.clone();
    ImageC(Rect(0, 0, 100, 100)).setTo(255);
    imshow("image", image);
    imshow("image_clone" ,ImageC);
    waitKey(0);
    
    destroyAllWindows();
    return 0;
}
