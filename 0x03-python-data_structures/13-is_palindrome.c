#include <stdbool.h>
#include "stdlib.h"
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *second_half = NULL;
	int palindrome = 1; /* Assume palindrome by default */

	if (*head == NULL || (*head)->next == NULL)
		return (palindrome);
	/* Find the middle of the linked list using slow and fast pointers */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	/* If the number of nodes is odd, move slow one step ahead */
	if (fast != NULL)
		slow = slow->next;
	/* Reverse the second half of the linked list */
	second_half = slow;
	prev_slow->next = NULL;
	second_half = reverse_list(second_half);

	/* Compare the first half and the reversed second half */
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	/* Restore the original list */
	second_half = reverse_list(slow);
	prev_slow->next = second_half;

	return (palindrome);
}
