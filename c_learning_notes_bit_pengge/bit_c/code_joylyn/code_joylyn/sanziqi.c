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
	printf("�ѳɹ�������Ϸ\n");
}

int sanziqi()
{
	int choice = 0;
	//��ӡ�˵����û�ѡ��
	do
	{

		sanziqi_menu();
		printf("��ѡ���Ӧ������->");
		scanf("%d", &choice);
		switch (choice)
		{
		case 1:
			sanziqi_play_game();
			break;
		case 0:
			printf("���˳���Ϸ\n");
			break;
		default:
			printf("ѡ�����������ѡ��\n");
			break;
		}
	} while (choice);
	return 0;
}
