#include <iostream>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;
class Sudoku {
 public:

	void input(istream &in) {
		for (int i = 0; i < MAX; i++) {
			for (int j = 0; j < MAX; j++) {
				in >> grid[i][j];
				edit[i][j] = !(grid[i][j]);
			}
		}
	}

	void output(ostream &out) {
		for (int i = 0; i < MAX; i++) {
			for (int j = 0; j < MAX; j++) {
				out << grid[i][j] << " ";
				if ((j + 1) % 3 == 0) {
					out << " ";
				}
			}
			out << endl;
			if ((i + 1) % 3 == 0) {
				out << endl;
			}
		}
	}

	bool solve() {
		int row = 0, col = 0;
		if (!nextEmpty(row, col)) {
			return 1;
		}

		for (int i = 1; i < MAX + 1; i++) {
			if (isValid(i, row, col)) {
				grid[row][col] = i;
				if (solve()) {
					return 1;
				} else {
					grid[row][col] = 0;
				}
			}
		}
		return 0;
	}

	bool isValid(int num, int row, int col) {
		if (grid[row][col]) { //if spot has already been assigned
			return 0;
		}
		return (checkRow(num, row) && checkCol(num, col) && checkSquare(num, row, col));
	}

 private:
	static const int MAX = 9;
	int grid[MAX][MAX];
	int edit[MAX][MAX];

	bool checkRow(int num, int row) {
		for (int i = 0; i < MAX; i++) {
			if (grid[row][i] == num) {
				return 0;
			}
		}
		return 1;
	}
	bool checkCol(int num, int col) {
		for (int i = 0; i < MAX; i++) {
			if (grid[i][col] == num) {
				return 0;
			}
		}
		return 1;
	}
	bool checkSquare(int num, int row, int col) {
		int rowStart = (row < 3 ? 0 : row < 6 ? 3 : 6);
		int colStart = (col < 3 ? 0 : col < 6 ? 3 : 6);
		for (int i = rowStart; i < rowStart + 3; i++) {
			for (int j = colStart; j < colStart + 3; j++) {
				if (grid[i][j] == num) {
					return 0;
				}
			}
		}
		return 1;
	}
	bool nextEmpty(int &row, int &col) {
		for (int i = 0; i < MAX; i++) {
			for (int j = 0; j < MAX; j++) {
				if (!grid[i][j]) {
					row = i;
					col = j;
					return 1;
				}
			}
		}
		return 0;
	}
};

int main() {
	ifstream fin("grid.txt");
	Sudoku obj;
	obj.input(fin);
	obj.output(cout);
	cout << endl;
	obj.solve();
	obj.output(cout);
	cout << endl;

	return EXIT_SUCCESS;
}

