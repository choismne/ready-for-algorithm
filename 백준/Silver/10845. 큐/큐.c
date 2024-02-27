#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
	int que[10000];
	int size;
}queue;

void push(queue* pq, int data) {
	for (int i = pq->size; i > 0; i--)
		pq->que[i] = pq->que[i - 1];
	pq->que[0] = data;
	pq->size++;
}
int pop(queue* pq) {
	if (pq->size == 0)
		return -1;
	else {
		int idx;
		idx = pq->size - 1;
		pq->size--;
		return pq->que[idx];
	}
}
int size(queue* pq) {
	return pq->size;
}
int empty(queue* pq) {
	if (pq->size == 0)
		return 1;
	else
		return 0;
}
int front(queue* pq) {
	if (pq->size == 0)
		return -1;
	else
		return pq->que[pq->size - 1];
}
int back(queue* pq) {
	if (pq->size == 0)
		return -1;
	else
		return pq->que[0];
}
int main() {
	queue queue;
	queue.size = 0;
	int n, i, data;
	char cmd[6];
	scanf("%d", &n);
	getchar();
	for (i = 0; i < n; i++) {
		scanf("%s", cmd);
		getchar();
		if (strcmp(cmd, "push") == 0) {
			scanf("%d", &data);
			push(&queue, data);
		}
		if (strcmp(cmd, "pop") == 0) {
			printf("%d\n", pop(&queue));
		}
		if (strcmp(cmd, "size") == 0) {
			printf("%d\n", size(&queue));
		}
		if (strcmp(cmd, "empty") == 0) {
			printf("%d\n", empty(&queue));
		}
		if (strcmp(cmd, "front") == 0) {
			printf("%d\n", front(&queue));
		}
		if (strcmp(cmd, "back") == 0) {
			printf("%d\n", back(&queue));
		}
	}
	return 0;
}