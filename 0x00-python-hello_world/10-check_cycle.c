#include "lists.h"

/**
 * check_cycle - Checks if linked list has a loop or not
 * @list: pointer to linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = NULL, *ptr2 = NULL;
	ptr1 = ptr2 = list;

	while (ptr1 && ptr2)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
