#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 *insert_node - prints a list length
 *@head: the first position
 *@number: position to be inserted
 *Return: On success 1.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
		return (NULL);

	while (temp)
	{
		if (temp->next == NULL)
		{
			new->next = temp;
			temp->next = new;
			return (new);
		}
		if (number < temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
/*		if (head == NULL)
		{
			new->next = temp;
			*head = new;
			return (new);
		}*/
		temp = temp->next;
	}
	return (new);
}
