#include "list.h"
/**
 * insert_node - function that insert a number into sorted linked list
 * @head: list head
 * @number: the number to add to node
 *
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t newnode, start;

	start = *head;
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (start->next != NULL)
	{
		if ((start->next)->n >= number)
		{
			newnode->next = start->next;
			start->next = newnode;
			return (newnode);
		}
		start = start->next;
	}
	newnode->next = NULL;
	start->next = newnode;
	return (newnode);
}
