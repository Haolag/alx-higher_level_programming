#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * insert_node - insert a new node at sort of a listint_t list
  * @head: pointer to pointer of first node of listint_t list
  * @number: integer to be included in new node
  * Return: address of the new element or NULL if it fails
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copyhead = *head, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}

	for (; copyhead != NULL; copyhead = copyhead->next)
	{
		if (number <= copyhead->n)
		{
			*head = new;
			new->next = copyhead;
			return (new);
		}
		if (number >= copyhead->n && copyhead->next == NULL)
		{
			new->next = NULL;
			copyhead->next = new;
			return (new);
		}
		if (number >= copyhead->n && number <= copyhead->next->n)
		{
			new->next = copyhead->next;
			copyhead->next = new;
			return (new);
		}
	}

	return (NULL);
}
