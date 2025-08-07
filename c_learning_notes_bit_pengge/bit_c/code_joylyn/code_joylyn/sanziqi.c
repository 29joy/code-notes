#include "sanziqi.h"

void sanziqi_menu()
{
	printf("************************\n");
	printf("******   1.play   ******\n");
	printf("******   0.exit   ******\n");
	printf("************************\n");
}


void sanziqi_play_game()
{
	printf("已成功进入游戏\n");
}

int sanziqi()
{
	int choice = 0;
	//打印菜单，用户选择
	do
	{

		sanziqi_menu();
		printf("请选择对应的数字->");
		scanf("%d", &choice);
		switch (choice)
		{
		case 1:
			sanziqi_play_game();
			break;
		case 0:
			printf("已退出游戏\n");
			break;
		default:
			printf("选择错误，请重新选择\n");
			break;
		}
	} while (choice);
	return 0;
}
