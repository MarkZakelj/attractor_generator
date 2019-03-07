#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double next_x(double x, double y, double a, double b) {
	return sin(a*y) - cos(b*x);
}

double next_y(double x, double y, double c, double d) {
	return sin(c*x) - cos(d*y);
}

void generate_values(int** matrix, double a, double b, double c, double d,long n_iters, int width, int height) {
	double x = 1.000;
	double y = 1.000;
	for(long i = 0; i < n_iters; i++) {
		//scale and translate to fit into matrix
		int x_mat = round(x*0.2*width + width/2);
		int y_mat = round(y*0.2*height + height/2);

		if(x_mat < width && y_mat < height) {
			matrix[y_mat][x_mat] += 1;
		}
		double xtmp = next_x(x, y, a, b);
		double ytmp = next_y(x, y, c, d);
		x = xtmp;
		y = ytmp;
	}
}


int main(int argc, char* argv[]) {
	if(argc < 6) {
		printf("Error! too few arguments.\n");
		return 1;
	}

	int width = 1100;
	int height = 1100;

	//read parameters
	double a = atof(argv[1]);
	double b = atof(argv[2]);
	double c = atof(argv[3]);
	double d = atof(argv[4]);
	long n_iters = atol(argv[5]);

	if(argc == 8) {
		//possible arguments width and height (1100 each by default)
		width = atoi(argv[6]);
		height = atoi(argv[7]);
	}
	
	//create empty matrix
	int** matrix = (int**)malloc(sizeof(int*)*height);
	for(int y = 0; y < height; y++) {
		matrix[y] = (int*)calloc(sizeof(int), width);
	}

	generate_values(matrix, a, b, c, d, n_iters, width, height);
	
	//write matrix to csv file	
	FILE* f = fopen("matrix.csv", "w");
	for(int j = 0; j < height; j++) {
		for(int i = 0; i < width-1; i++) {
			fprintf(f, "%d,", matrix[j][i]);
		}
		fprintf(f, "%d\n", matrix[j][width-1]);
	}
	fclose(f);

	//free memory
	for(int i = 0; i < height; i++) {
		free(matrix[i]);
	}
	free(matrix);

	return 0;
}