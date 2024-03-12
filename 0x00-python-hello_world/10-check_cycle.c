#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *t, *h;

	if (list == NULL || list->next == NULL)
		return (0);

	t = list;
	h = list->next;

	while (h != NULL && h->next != NULL)
	{
		if (t == h)
			return (1);

		t = t->next;
		h = h->next->next;
	}

	return (0);
}
