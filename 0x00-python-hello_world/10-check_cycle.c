#include "lists.h"

/**
 * check_cycle - cheks if a singly linked list is cyclic
 * @list: pointer to head of a singly linked list
 *
 * Return: 0 if no cycle, 1 if cyclic
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list, *current = list->next;

	while (current)
	{
		if (current == first)
			return (1);

		current = current->next;
	}

	return (0);
}

