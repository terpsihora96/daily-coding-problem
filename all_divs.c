#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int all_divs(int *a, int n) {
	int j = 0;

	for (int i = 1; i <= sqrt(n); ++i) {
		if (n % i == 0) {
		    if (n/i == i) {	
				a[j++] = i;
			}
			else {
				a[j++] = i;
				a[j++] = n/i;
			}
		}
	}

	return j;
}

int main(int argc, char** argv) {
	int *a = malloc(100 * sizeof (int));
	if (!a) {
		perror("Memory allocation failed.");
		exit(EXIT_FAILURE);
	}
	if (argc != 2) {
		perror("Number needed.");
		exit(EXIT_FAILURE);
	}

	int n = abs(atoi(argv[1]));
	int len = all_divs(a, n);
	printf("All divisors of %d\n", n);
	for (int i = 0; i < len; i++) {
		printf("%d ", a[i]);
	}
	
	return 0;
}
