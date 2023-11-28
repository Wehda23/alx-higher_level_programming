#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function used to insert a node of value to certain position
 * @head: is a list node
 * @number: is value of the node.
 * Return: pointer to the listnode.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *current = *head, *prev = NULL;

	tmp = (listint_t *) malloc(sizeof(listint_t));

	if (tmp == NULL)
	{
		return (NULL);
	}

	tmp->n = number;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		tmp->next = *head;
		*head = tmp;
	}
	else
	{
		prev->next = tmp;
		tmp->next = current;
	}

	return (tmp);
}
