#include <stdio.h>
#include <stdlib.h>

double max_seq(double *a, int n) {
    double maxSum = 0;
    double currSum = 0;
    int begin = 0;
    int end = -1;
    int currBegin = 0;

    for (int i = 0; i < n; ++i) {
        currSum += a[i];    
        if (currSum > maxSum) {
            maxSum = currSum;
            begin = currBegin;
            end = i;
        }
        else if (currSum < 0) {
            currBegin = i + 1;
            currSum = 0;
        }
    }    
    return maxSum;
}

int main() {
    int len;
    scanf("%d", &len);
    len = abs(len);

    double *a = malloc(len * sizeof (double));
    if (!a) {
        printf("Memory allocation failed.");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < len; i++)
        scanf("%lf", &a[i]);

    printf("%lf\n", max_seq(a, len));

    return 0;
}
