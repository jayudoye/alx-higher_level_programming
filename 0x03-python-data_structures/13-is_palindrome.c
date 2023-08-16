#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome- Function that checks if a singly linked list is a palindrome
 * @head: Head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int values[9999], x = 0, y = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	node = *head;
	if (!node->next)
	{
		return (1);
	}
	while (node)
	{
		values[x] = node->n;
		node = node->next;
		x++;
	}
	x--;
	while (x >= 0 && y <= x)
	{
		if (values[x] != values[y])
		{
			return (0);
		}
		x--;
		y++;
	}
	return (1);
}
