#include "lists.h"

/**
 * check_cycle - function that using hare and tortoise algorithm
 * @list: pointer to a node list.
 * Return: 1 in case of cycle detected otherwise 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
