#include "lists.h"

int listintlen(listint_t **head);

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to the head of the list
 *
 * Retrun: 1 if is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current_node;
	int i, len, *nlist;

	if (*head == NULL)
		return (1);

	len = listintlen(head);
	if (len % 2 != 0)
		return (0);

	nlist = malloc(sizeof(int) * len);
	if (nlist == NULL)
		return (0);

	for (i = 0; i < len / 2; i++)
	{
		nlist[i] = current_node->n;
		current_node = current_node->next;
	}

	for (i = 0; i < len / 2; i++)
		if (nlist[i] != nlist[(len - 1) - i])
			return (0);

	return (1);
}

/**
 * listintlen - calculates the len of
 * a singely linked list
 * @head: pointer to the head of the list
 *
 * Retrun: the length of the list
 */

int listintlen(listint_t **head)
{
	listint_t *current_node = *head;
	int i = 0;

	for (i = 0; current_node; i++)
		current_node = current_node->next;

	return (i);
}

