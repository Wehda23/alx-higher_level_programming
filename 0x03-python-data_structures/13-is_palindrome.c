#include "lists.h"
#include "stdlib.h"
#include "stdio.h"

/**
 * is_palindrome - is a function that checks if linked list is palindrom | not.
 * @head: is a pointer to a linked list
 * Return: 0 in case of not palindrom otherwise 1 if palindrom.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *numbers = (int *) malloc(sizeof(int));
	int index = 0, arraySize = 1;
	int isPalindrom = 0;

	if (numbers == NULL)
	{
		perror("Failed to allocate memory!.");
		free(numbers);
		exit(1);
	}

	while (current != NULL)
	{
		if (index >= arraySize)
		{
			arraySize++;
			numbers = (int *)realloc(numbers, arraySize * sizeof(int));

			if (numbers == NULL)
			{
				perror("Memory reallocation failed, Unable to resize array");
				free(numbers);
				exit(1);
			}
		}
		numbers[index] = current->n;
		index++;
		current = current->next;
	}
	index = 0;
	isPalindrom = palindrom(numbers, arraySize);

	free(numbers);
	return (isPalindrom);
}

/**
 * palindrom - function that checks if array of integers is palindrom | not.
 * @array: pointer to integer list of integers.
 * @size: size of array.
 * Return: 0 in case of failure, 1 incase of success.
 */
int palindrom(int *array, int size)
{
	int forward = 0, backwards = size - 1;

	if (size % 2 == 0)
	{
		while (forward < backwards)
		{
			if (array[forward] != array[backwards])
				return (0);
			forward++;
			backwards--;
		}
	}
	else
	{
		while (forward != backwards)
		{
			if (array[forward] != array[backwards])
				return (0);
			forward++;
			backwards--;
		}
	}
	return (1);
}
