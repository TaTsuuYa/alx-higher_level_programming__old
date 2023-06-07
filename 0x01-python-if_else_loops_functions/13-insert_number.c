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

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}

	current_node = *head;
	if (current_node->n > number)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}

	while (current_node->next)
	{
		if ((current_node->next)->n >= number)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
			return (new_node);
		}
		current_node = current_node->next;
	}
	current_node->next = new_node;
	return (new_node);
}

