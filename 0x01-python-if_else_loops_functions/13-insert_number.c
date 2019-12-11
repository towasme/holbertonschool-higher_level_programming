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

listint_t *insert_node(listint_t **head, int number);
{
	listint_t *temp = *head;
	listint_t *new = NULL;

	new->n = number;

