#include "homework_point_chujie.h"

//дһ��������ӡarr��������ݣ���ʹ�������±꣬ʹ��ָ�롣
//arr��һ������һά���顣
int print_arr()
{
	int arr[5] = {1, 2, 3, 4, 5};
	int* p = &arr;
	int i = 0;
	for (i = 0; i < 5; i++)
	{
		printf("%d",*(p + i));
	}
	return 0;
}

int reverse_str()
{
	char arr[] = {0};
	int i = 0;
	gets(arr);
	i = strlen(arr);

	return 0;
}
