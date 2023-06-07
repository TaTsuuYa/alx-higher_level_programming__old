#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inesrt a node into a sorted list
 * @head: first element
 * @number: value of the node
 *
 * Return: pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;

	if (*head == NULL)
		return (NULL);

	current_node = *head;

	new_node = malloc(sizeof(listint_t));
	new_node->n = number;

	if (current_node->next)
	{
		new_node->next = current_node->next;
		*head = new_node;
		return (new_node);
	}

	while (current_node)
		if (current_node->next->n > number)
		{
			new_node->next = current_node->next->next;
			current_node->next = new_node;
			return (new_node);
		}
	new_node->next = current_node->next->next;
	current_node->next = new_node;
	return (new_node);
}
