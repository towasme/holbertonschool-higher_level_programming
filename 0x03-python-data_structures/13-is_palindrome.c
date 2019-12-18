#include "lists.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
/**
 *is_palindrome - prints a list length
 *@head: the first position
 *Return: On success 1.
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int i = 0, cont = 0;
	int num_arr[1025];

	if (!head)
	{
		return (0);
	}
	while (temp)
	{
		num_arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	while ((i / 2) >= 0)
	{
		if (num_arr[cont] != num_arr[i - 1])
		{
			return (0);
		}
		else
		{
			i--;
			cont++;
		}
	}
	return (1);
}
