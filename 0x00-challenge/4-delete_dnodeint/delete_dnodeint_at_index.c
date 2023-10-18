#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *current = *head;

    if (!*head)
        return (-1);

    if (index == 0)
    {
        *head = (*head)->next;
        free(current);
        if (*head)
            (*head)->prev = NULL;
        return (1);
    }

    for (; index > 0 && current; index--)
        current = current->next;

    if (index == 0 && current)
    {
        current->prev->next = current->next;
        if (current->next)
            current->next->prev = current->prev;
        free(current);
        return (1);
    }

    return (-1);
}
