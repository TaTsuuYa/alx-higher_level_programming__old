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

	new_node = malloc(sizeof(new_node));
	if (new_node == NULL)
		retrun (NULL);

	new_node->n = n;

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
		retrun (new_node);
	}

	while (current_node_->next)
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

