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
    while (scanf("%d %d", &a, &b) != EOF) { // 注意 while 处理多个 case
        // 64 位输出请用 printf("%lld") to
        // int c = (a > b? a, b);
        // int d = (a <= b? a, b);
        int i = 0;
        for (i = 1; i <= a; i++) {
            if ((b * i) % a == 0) {
                printf("%d\n", (b * i));
                break;
            }
        }
        //本来想在循环里循环a和b中较小的那个数，因为这样可以减少循环次数
        //下面是老师的办法，更简洁
        /*while (a * i % b)
        {
            i++;
        }
        printf("%d\n", (b * i));*/
        //a和b应该给long long类型， 因为两个很大的数相乘可能超出了int的范围，printf时也应该用lld打印
    }
    return 0;
}

//老师说这样是笨方法哈哈哈，
// 按照每个单词和它应该去的位置放到一个新的数组里
// 这个写法没有考虑最后下标加到\0的时候就不能再++了所以引发了溢出
//int invert_string()
//{
//    //char a = " ";
//    //char b = " ";
//    char arr1[101] = { 0 };
//    char arr2[101] = { 0 };
//    //arr1 = scanf("%s", &a);//scanf这个函数读到空格就不读了，gets()可以读取一个字符串即便中间有空格
//    //gets(arr1);
//    fgets(arr1, 100, stdio);
//    //两个字符串，另外一个用来存倒序的字符串
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

//老师的方法：
//第一步：逆序整个字符串
//第二步：再逆序每个单词
//先逆序每个单词再逆序整个字符串是一样的
//逆序一个单词和逆序整个字符串的逻辑是一样的，都是第一个和最后一个交换，然后不断往中间走
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
        if (*cur == ' ')//不是\0才能++，否则就指向数组外了
            cur++;
    }
    printf("%s\n", arr);
    return 0;
}

//1.为什么用char类型数组就可以存储字符串，可以直接存储，还可以不初始化
//2.越界的问题

//未考虑溢出
//计算n的阶乘
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
//计算1！+2！+3！···+10！
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
//计算1！+2！+3！···+10！
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
//上一次算好的值不要覆盖，留着直接加到最后的值里
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

//在一个有序数组中查找某个数字n（二分查找）
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

//演示实现多个字符从两端移动向中间汇聚
//例如要在屏幕上显示welcome to bit！！
void move_from_two_sides()
{
    char arr1[] = "wlecome to bit !!!";
    char arr2[] = "##################";//注意字符串数组的初始化方式
    //int sz = sizeof(arr) / sizeof(arr[0]);
    int sz = strlen(arr1) - 1;//注意求长度的方式
    int left = 0;
    int right = sz;
    int i = 0;
    while (left <= right)
    {
        arr2[left] = arr1[left];
        arr2[right] = arr1[right];
        printf("%s\n", arr2);
        Sleep(1000);//sleep需要windows头文件
        system("cls");//清理屏幕
        left++;
        right--;
    }
    printf("%s\n", arr2);
}

//模拟用户登录页面，只允许登录三次，如果三次内输入正确就登录成功，否则就登录失败
//两个字符串比较相等，不能用==，应该用strcmp库函数,返回0表示相等，返回大于0的数字表示第一个字符串大于第二个字符串，返回小于0的数字表示第一个字符串小于第二个字符串
int log_in()
{
    int i = 0;
    char password[20] = { 0 };
    int flag = 0;
    for (i = 0; i < 3; i++)
    {
        printf("请输入密码：");
        scanf("%s", password);
        if (strcmp(password, "123456") == 0)
        {
            printf("密码正确，登陆成功\n");
            flag = 1;
            break;
        }
        else
        {
            printf("密码错误\n");
        }
    }
    if (flag == 0)//因为正确和错误都会返回到这里，所以这里要判断一下是否三次密码错误输出登陆失败
        printf("登陆失败\n");
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
//最终char a[1000]里面存的是-1 -2 -3 ··· -128 127 126 ···3 2 1 0然后循环，直到1000个填满
//strlen求的是字符串长度，到\0的时候停止，\0的ASCII码值事0，所以到第一个0的时候停止，所以结果是255

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
    }//遍历一遍然后scanf输入就可以了
    //scanf("%d %d", &arr);//第一个问题，如何在不确定数组长度的情况下输入到数组里
    //for (i = 0; i < num; i++)
    //{
    //    //判断是递增还是递减，都不是那就不是有序序列
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
    }//不用判断前后两个数相等的时候
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
//    //加上while循环可以循环输入
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
//            {//1)能被4整除，但不能被100整除;2)能被400整除
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
//    //鹏哥用Switch语句更合适一些
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
//            {//1)能被4整除，但不能被100整除;2)能被400整除
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
    //用数组更简单了，只需要输出对应下标的天数，除非是闰年2月
    while (scanf("%d %d", &year, &month) == 2)
    {
        if (((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) && month == 2)
        {//1)能被4整除，但不能被100整除;2)能被400整除
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
