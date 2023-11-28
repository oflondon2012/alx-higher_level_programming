#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle
 * @list: pointer to singly linked list
 *
 * Return: 0 when there is no cycle or 1 when there is
 */
int check_cycle(listint_t *list)
{
	listint_t *sl, *prev;

	if (list == NULL || list->next == NULL)
		return (0);
	sl = list->next;
	prev = list->next->next;
	while (sl && prev && prev->next)
	{
		if (sl == prev)
			return (1);
		sl = sl->next;
		prev = prev->next->next;
	}
	return (0);
}
