#include "class_practice_code.h"


int compare_two_num()
{
    int a = 0;
    int b = 0;
    scanf("%d %d", &a, &b);
    if (a >= b)
        printf("%d", a);
    else
        printf("%d", b);
    return 0;
}

int lowest_common_multiple()
{
    int a, b;
    while (scanf("%d %d", &a, &b) != EOF) { // ע�� while ������ case
        // 64 λ������� printf("%lld") to
        // int c = (a > b? a, b);
        // int d = (a <= b? a, b);
        int i = 0;
        for (i = 1; i <= a; i++) {
            if ((b * i) % a == 0) {
                printf("%d\n", (b * i));
                break;
            }
        }
        //��������ѭ����ѭ��a��b�н�С���Ǹ�������Ϊ�������Լ���ѭ������
        //��������ʦ�İ취�������
        /*while (a * i % b)
        {
            i++;
        }
        printf("%d\n", (b * i));*/
        //a��bӦ�ø�long long���ͣ� ��Ϊ�����ܴ������˿��ܳ�����int�ķ�Χ��printfʱҲӦ����lld��ӡ
    }
    return 0;
}

//��ʦ˵�����Ǳ�������������
// ����ÿ�����ʺ���Ӧ��ȥ��λ�÷ŵ�һ���µ�������
// ���д��û�п�������±�ӵ�\0��ʱ��Ͳ�����++���������������
//int invert_string()
//{
//    //char a = " ";
//    //char b = " ";
//    char arr1[101] = { 0 };
//    char arr2[101] = { 0 };
//    //arr1 = scanf("%s", &a);//scanf������������ո�Ͳ����ˣ�gets()���Զ�ȡһ���ַ��������м��пո�
//    //gets(arr1);
//    fgets(arr1, 100, stdio);
//    //�����ַ���������һ�������浹����ַ���
//    int i = 0;
//    int j = 0;
//    int n = 0;
//    int count_b_left = 100;
//    int count_b_right = 100;
//    int count_a = 0;
//    char* pa = &arr1;
//    char* pb = &arr2;
//    for (i = 0; i < 100; i++)
//    {
//        if (*(pa + i) != " ")
//        {
//            count_a++;
//            count_b_left--;
//        }
//        else
//        {
//            for (j = count_b_left; j <= count_b_right; j++)
//            {
//                for (n = 0; n <= count_a; n++)
//                    *(pb + j) = *(pa + n);
//            }
//            count_a++;
//            *(pb + count_b_left) = " ";
//            count_b_right = count_b_left;
//            count_b_left--;
//        }
//    }
//    printf("%s", arr2);
//    return 0;
//}

//��ʦ�ķ�����
//��һ�������������ַ���
//�ڶ�����������ÿ������
//������ÿ�����������������ַ�����һ����
//����һ�����ʺ����������ַ������߼���һ���ģ����ǵ�һ�������һ��������Ȼ�󲻶����м���
void reverse(char* left, char* right)
{
    while (left < right)
    {
        char tmp = *left;
        *left = *right;
        *right = tmp;
        left++;
        right--;
    }
}

int invert_string()
{
    char arr[101];
    //gets(arr);
    int len = strlen(arr);
    reverse(arr, arr + len - 1);

    char* start = arr;
    char* cur = arr;

    while (*cur)
    {
        while (*cur != ' ' && *cur != '\0')
        {
            cur++;
        }
        reverse(start, cur - 1);
        start = cur + 1;
        if (*cur == ' ')//����\0����++�������ָ����������
            cur++;
    }
    printf("%s\n", arr);
    return 0;
}

//1.Ϊʲô��char��������Ϳ��Դ洢�ַ���������ֱ�Ӵ洢�������Բ���ʼ��
//2.Խ�������

//δ�������
//����n�Ľ׳�
int factorial()
{
    int n = 0;
    int j = 0;
    int ret = 1;
    scanf("%d", &n);
    for (j = 1; j <= n; j++)
    {
        ret *= j;
    }
    printf("%d", ret);
    return 0;
}
//����1��+2��+3��������+10��
int factorial_fun(int n)
{
    int j = 0;
    int ret = 1;
    for (j = 1; j <= n; j++)
    {
        ret *= j;
    }
    printf("%d ", j);
    printf("%d ", ret);
    return ret;
}
int factorial_10()
{
    int n = 0;
    int j = 0;
    int ret = 0;
    for (n = 1; n <= 10; n++)
    {
        ret += factorial_fun(n);
    }
    printf("ret = %d", ret);
    return 0;
}
//����1��+2��+3��������+10��
int factorial_all_in_one()
{
    int n = 10;
    int i = 0;
    int j = 0;
    int ret2 = 0;
    for (i = 1; i <= n; i++)
    {
        int ret1 = 1;
        for (j = 1; j <= i; j++)
        {
            ret1 *= j;
        }
        ret2 += ret1;
    }
    printf("%d", ret2);
    return 0;
}
//��һ����õ�ֵ��Ҫ���ǣ�����ֱ�Ӽӵ�����ֵ��
int factorial_all_in_one_simple()
{
    int n = 10;
    int i = 0;
    int ret = 1;
    int sum = 0;
    for (i = 1; i <= n; i++)
    {
        ret *= i;
        sum += ret;
    }
    printf("%d", sum);
    return 0;
}

//��һ�����������в���ĳ������n�����ֲ��ң�
int find_n()
{
    int arr[10] = { 0 };
    int n = 0;
    int i = 0;
    //scanf("%d", arr);
    scanf("%d", &n);
    int sz = sizeof(arr) / sizeof(arr[0]);
    int left = 0;
    int right = sz - 1;

    for (i = 0; i < sz; i++)
    {
        arr[i] = i;
        printf("%d ", arr[i]);
    }

    //if (arr[left] == n)
    //{
    //    printf("left=%d %d", left, n);
    //    return 0;
    //}
    //if (arr[right] == n)
    //{
    //    printf("right=%d %d", right, n);
    //    return 0;
    //}
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (arr[mid] == n)
        {
            printf("%d n=%d", mid, n);
            break;
        }
        else if (arr[mid] < n)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    return 0;
}

//��ʾʵ�ֶ���ַ��������ƶ����м���
//����Ҫ����Ļ����ʾwelcome to bit����
void move_from_two_sides()
{
    char arr1[] = "wlecome to bit !!!";
    char arr2[] = "##################";//ע���ַ�������ĳ�ʼ����ʽ
    //int sz = sizeof(arr) / sizeof(arr[0]);
    int sz = strlen(arr1) - 1;//ע���󳤶ȵķ�ʽ
    int left = 0;
    int right = sz;
    int i = 0;
    while (left <= right)
    {
        arr2[left] = arr1[left];
        arr2[right] = arr1[right];
        printf("%s\n", arr2);
        Sleep(1000);//sleep��Ҫwindowsͷ�ļ�
        system("cls");//������Ļ
        left++;
        right--;
    }
    printf("%s\n", arr2);
}

//ģ���û���¼ҳ�棬ֻ�����¼���Σ����������������ȷ�͵�¼�ɹ�������͵�¼ʧ��
//�����ַ����Ƚ���ȣ�������==��Ӧ����strcmp�⺯��,����0��ʾ��ȣ����ش���0�����ֱ�ʾ��һ���ַ������ڵڶ����ַ���������С��0�����ֱ�ʾ��һ���ַ���С�ڵڶ����ַ���
int log_in()
{
    int i = 0;
    char password[20] = { 0 };
    int flag = 0;
    for (i = 0; i < 3; i++)
    {
        printf("���������룺");
        scanf("%s", password);
        if (strcmp(password, "123456") == 0)
        {
            printf("������ȷ����½�ɹ�\n");
            flag = 1;
            break;
        }
        else
        {
            printf("�������\n");
        }
    }
    if (flag == 0)//��Ϊ��ȷ�ʹ��󶼻᷵�ص������������Ҫ�ж�һ���Ƿ�����������������½ʧ��
        printf("��½ʧ��\n");
    return 0;
}

int str_len_a()
{
    char a[1000];
    int i;
    for (i = 0; i < 1000; i++)
    {
        a[i] = -1 - i;
    }
    printf("%d", strlen(a));
    return 0;
}
//����char a[1000]��������-1 -2 -3 ������ -128 127 126 ������3 2 1 0Ȼ��ѭ����ֱ��1000������
//strlen������ַ������ȣ���\0��ʱ��ֹͣ��\0��ASCII��ֵ��0�����Ե���һ��0��ʱ��ֹͣ�����Խ����255

int sorted_array()
{
    int num = 0;
    int i = 0;
    int arr[50] = { 0 };
    BOOL flag_des = FALSE;
    BOOL flag_ase = FALSE;

    scanf("%d", &num);
    for (i = 0; i < num; i++)
    {
        scanf("%d", &arr[i]);
    }//����һ��Ȼ��scanf����Ϳ�����
    //scanf("%d %d", &arr);//��һ�����⣬����ڲ�ȷ�����鳤�ȵ���������뵽������
    //for (i = 0; i < num; i++)
    //{
    //    //�ж��ǵ������ǵݼ����������ǾͲ�����������
    //    if()
    //}
    i = 0;
    while ((flag_des == FALSE || flag_ase == FALSE) && (i < num - 1))
    {
        if (arr[i] < arr[i + 1])
            flag_ase = TRUE;
        else if (arr[i] > arr[i + 1])
            flag_des = TRUE;
        i++;
    }//�����ж�ǰ����������ȵ�ʱ��
    if (flag_des == TRUE && flag_ase == TRUE)
        printf("unsorted");
    else
        printf("sorted");
    return 0;
}

//int number_of_days_in_a_month()
//{
//    int month = 0;
//    int year = 0;
//    //����whileѭ������ѭ������
//    while (scanf("%d %d", &year, &month) == 2)
//    {
//        if (month == 1 || month == 3 || month == 5 || month == 7
//            || month == 8 || month == 10 || month == 12)
//        {
//            printf("%d", 31);
//        }
//        else if (month == 4 || month == 6 || month == 9 || month == 11)
//        {
//            printf("%d", 30);
//        }
//        else
//        {
//            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
//            {//1)�ܱ�4�����������ܱ�100����;2)�ܱ�400����
//                printf("%d", 29);
//            }
//            else
//            {
//                printf("%d", 28);
//            }
//        }
//    }
//    return 0;
//}

//int number_of_days_in_a_month()
//{
//    int month = 0;
//    int year = 0;
//    //������Switch��������һЩ
//    while (scanf("%d %d", &year, &month) == 2)
//    {
//        switch (month)
//        {
//        case 1:
//        case 3:
//        case 5:
//        case 7:
//        case 8:
//        case 10:
//        case 12:
//            printf("%d", 31);
//            break;
//        case 4:
//        case 6:
//        case 9:
//        case 11:
//            printf("%d", 30);
//            break;
//        case 2:
//            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
//            {//1)�ܱ�4�����������ܱ�100����;2)�ܱ�400����
//                printf("%d", 29);
//            }
//            else
//            {
//                printf("%d", 28);
//            }
//            break;
//        default:
//            break;
//    }
//    return 0;
//}

int number_of_days_in_a_month()
{
    int month = 0;
    int year = 0;
    int days[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    //����������ˣ�ֻ��Ҫ�����Ӧ�±������������������2��
    while (scanf("%d %d", &year, &month) == 2)
    {
        if (((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) && month == 2)
        {//1)�ܱ�4�����������ܱ�100����;2)�ܱ�400����
            printf("%d", 29);
        }
        else
        {
            printf("%d", days[month]);
        }
    }
    return 0;
}

int change_array()
{
    int arr1[] = {1, 2, 3, 4, 5, 6};
    int arr2[] = {7, 8, 9, 10, 11, 12};
    int i = 0;
    int len = sizeof(arr1) / sizeof(arr1[0]);
    for (i = 0; i < len; i++)
    {
        int tmp = arr1[i];
        arr1[i] = arr2[i];
        arr2[i] = tmp;
    }
    for (i = 0; i < len; i++)
    {
        printf("%d", arr1[i]);
    }
    printf("\n");
    for (i = 0; i < len; i++)
    {
        printf("%d", arr2[i]);
    }
    return 0;
}

int reverse_array()
{
    char arr[] = {"abcdef"};
    int len = strlen(arr);
    int left = 0;
    int right = len - 1;
    while (left < right)
    {
        char tmp = arr[left];
        arr[left] = arr[right];
        arr[right] = tmp;
        left++;
        right--;
    }
    printf("%s", arr);
    return 0;
}
