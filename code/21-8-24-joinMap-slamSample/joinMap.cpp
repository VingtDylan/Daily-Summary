#include <iostream>
#include <fstream>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <Eigen/Geometry>
#include <boost/format.hpp>
#include <pcl/point_types.h>
#include <pcl/io/pcd_io.h>
#include <pcl/visualization/pcl_visualizer.h>

using namespace std;
using namespace cv2;
using namespace Eigen;
using namespace boost;

const int counter = 5;

int main(int argc, char** argv){
	vector<Mat> colorImgs, depthImgs;
	vector<Isometry3d, aligned_allocator<Isometry3d>> poses;

	ifstream fin("./pose.txt");
	assert(fin != nullptr);

	for(int i = 0; i < counter; i++){
		format fmt("./%s/%d.%s");
		colorImgs.push_back(imread((fmt%"color"%(i + 1)%"png").str()));
		depthImgs.push_back(imread((fmt%"depth"%(i + 1)%"pgm").str(), -1));
		double data[7] = {0};
		for(auto& d : data){
			fin >> d;
			Quaterniond q(data[6], data[3], data[4], data[5]);
			Isometry3d T(q);
			T.pretranslate(Vector3d(data[0], data[1], data[2]));
			poses.push_back(T);
		}
	}

	return 0;
}


