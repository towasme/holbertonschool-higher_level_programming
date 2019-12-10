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
	listint_t *temp = list, *sec = list;

	if (list == NULL)
		return (0);

	while (temp->next && sec && temp && sec->next)
	{
		temp = temp->next;
		sec = sec->next->next;
		if (temp == sec)
		{
			return (1);
		}
	}
	return (0);
}
