#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 *check_cycle - prints a list length
 *@list: The character to print
 *Return: On success 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	if (list == NULL || temp == NULL)
		return (0);

	while (temp)
	{
		if (temp == list)
		{
			return (1);
		}
		else
		{
			temp = temp->next;
		}
	}
	return (0);
}
