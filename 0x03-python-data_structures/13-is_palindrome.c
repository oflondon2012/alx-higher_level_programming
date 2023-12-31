#include "lists.h"

/**
 * reverse_list - function that reverse a linked list
 * @start: the begining of the list
 *
 * Return: the pointer to reserved list
 */
listint_t *reverse_list(listint_t **start)
{
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (*start != NULL)
	{
		next = (*start)->next;
		(*start)->next = prev;
		prev = *start;
		*start = next;
	}
	return (prev);
}
/**
 * is_palindrome - function that check if linked list is pal
 * @start: the begining of list
 *
 * Return: (1) if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *s_half, *fast = *head;
	listint_t *lotion = *head, *prev = *head;
	int is_pal = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev = lotion;
			lotion = lotion->next;
		}
		if (fast != NULL)
			lotion = lotion->next;
		s_half = reverse_list(&lotion);
		lotion = s_half;

		while (lotion != NULL)
		{
			if ((*head)->n != lotion->n)
			{
				is_pal = 0;
				break;
			}
			*head = (*head)->next;
			lotion = lotion->next;
		}

		reverse_list(&s_half);
		prev->next = s_half;
	}
	return (is_pal);
}
