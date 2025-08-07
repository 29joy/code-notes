#include "caishuzi.h"

//猜数字游戏：
//1、电脑随机生成一个数
//2、猜数字：1）猜大了，提醒猜大了继续猜；2）猜小了，提醒猜小了继续猜；3）猜对了恭喜你猜对了游戏结束
//3、玩完一把可以继续玩，不用退出程序

int menu()
{
	int i = 0;
	printf("------------------------\n");
	printf("------  1玩游戏   ------\n");
	printf("------  0退出游戏 ------\n");
	printf("------------------------\n");
	printf("请输入：");
	scanf("%d", &i);
	return i;
}

void play_game()
{
	//int num = rand();//电脑随机生成一个数
	int num = rand()%100 + 1;//电脑随机生成一个数，但是生成的数字可能很大，把随机数限制在1-100之间，%100的余数在0-99之间，加1就在1-100之间了
	//猜数字循环，while循环的
	int user_num = 0;
	while (1)
	{
		printf("请输入要猜的数字：");
		scanf("%d", &user_num);
		if (user_num == num)
		{
			printf("恭喜你猜对了\n");
			break;
		}
		else if (user_num < num)
		{
			printf("猜小了\n");
		}
		else
		{
			printf("猜大了\n");
		}
	}
}


int guess_number()//周日的目标，把三个游戏都靠自己实现一下，然后学新的课程
{
	int ret = 0;

	//while (1)//游戏是个循环游戏，最后再加上，一开始的时候反复的试验总是while循环不利于试验
	//{
	//	//打印菜单让用户选择：打印1选择玩游戏，打印0选择退出游戏
	//	ret = menu();
	//	if (ret == 1)//选择1开始玩游戏
	//	{
	//		srand((unsigned)time(NULL));
	//		printf("恭喜您已进入游戏\n");
	//		play_game();

	//	}
	//	else
	//	{
	//		printf("您已选择退出游戏\n");//选择0退出游戏
	//		break;
	//	}
	//}
	//这样写也可以，但是老师的方案似乎更完美
	//首先，除了输入0和1进行选择之外，还可能会输入其他的数值，所以要提醒选择错误
	//如上所说，用户选择了什么，用Switch语句比if语句好，以后可能会加入更多的选择，用Switch语句会更方便修改和实现
	//其次，用do while语句比while语句好的一点是，上来先执行一次打印菜单和让用户选择，之后根据用户的选择来限定while的判断，
	//当用户选择0的时候就可以直接退出循环，而输入其他为真的值就可以继续执行
	srand((unsigned int)time(NULL));//放在主函数里面只调用一次就可以，放在case1里每次都会设置一次随机数的生成起点，生成的随机数会不那么随机
	do
	{
		ret = menu();//menu里是否返回数字还是把scanf放在主函数里都可以，如果不在menu里返回值就写成void menu()
		switch (ret)
		{
		case 1:
			printf("恭喜您已进入游戏\n");
			play_game();
			break;
		case 0:
			printf("您已选择退出游戏\n");
			break;
		default:
			printf("选择错误重新选择\n");
			break;
		}
	} while (ret);
	return 0;
}
