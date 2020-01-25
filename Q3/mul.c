#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	if (argc != 3)
	{
		printf("Badly formatted arguments");
	}

	float num1 = atof(argv[1]);
	float num2 = atof(argv[2]);
	float result = num1 * num2;

	fprintf( stdout, "%f", result );

	return 0;
}
