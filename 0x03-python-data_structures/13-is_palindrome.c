#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome - checks if list is palindrome
 * @head: double pointer to head of list
 * Return: 0 if palindrome, -1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *front = *head, *back = *head;
	int l, tl;

	if (*head == NULL)
		return (1);
	for (l = 0; back->next != NULL; l++)
		back = back->next;

	while (front->next != NULL && front != back)
	{
		tl = 0;
		if (front->n == back->n)
		{
			front = front->next;
			l--;
			back = *head;
			while (tl < l)
			{
				tl++;
				back = back->next;
			}
		}
		else
			return (-1);
	}
	return (1);
}
