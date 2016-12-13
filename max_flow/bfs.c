#include <math.h>
#ifdef NAN
/* NAN is supported */
#endif
#ifdef INFINITY
/* INFINITY is supported */
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct node
{
	int num;
	struct node *next;
};

typedef struct node node;

void enQueue(node *head, int num);
int isEmpty(node *head);
int deQueue(node *head);
bool bfs(int x,int y,int** rgraph, int s, int t, int len, int parent[len], int V);
bool *mincut(int x, int y, int graph[x][y], int s, int t, int V);

void enQueue(node *head, int num)
{
	node *tmp, *newNode;
	newNode = (node*)malloc(sizeof(node));
	newNode -> num = num;
	newNode -> next = NULL;
	
	tmp = head;
	while(tmp -> next != NULL)
		tmp = tmp -> next;
	tmp -> next = newNode;
}

int isEmpty(node *head)
{
	if(head -> next == NULL)
		return 1;
	else
		return 0;
}

int deQueue(node *head)
{
	int num = head -> next -> num;
	node *tmp;
	tmp = head -> next;
	head -> next = head -> next -> next;
	free(tmp); 
	return num;	
}


bool bfs(int x,int y,int **rgraph, int s, int t, int len, int parent[len], int V){
	bool visited[V];
	int current;
	int i;
	for (i=0;i<V;i++){
		visited[i] = false;
	}
	visited[s] = true;
	parent[s] = -1;
	node *queue;
	queue = (node*)malloc(sizeof(node));
	queue -> num = -1;
	queue -> next = NULL;

	enQueue(queue, s);
	while (!isEmpty(queue)){
		current= deQueue(queue);
		int i;
		for (i = 0; i < V; i++)
		{
			if ( !visited[i] && rgraph[current][i] > 0 )
			{
				enQueue(queue,i);
				parent[i] = current;
				visited[i] = true;
			}
		}

	}
	return visited[t];

}



bool *mincut(int x, int y, int graph[x][y], int s, int t, int V){
	//int rgraph[x][y];
	//int *rgraph[x];
	int i,j;
    int** rgraph;

    rgraph = malloc(x * sizeof(int*));
    for (i = 0; i < x; i++) {
        rgraph[i] = malloc(y * sizeof(int));
    }

	int total_flow = 0;
    for(i = 0; i<x; i++){
	for (j = 0 ; j<y; j++)
    {
        rgraph[i][j] = graph[i][j];
    }
}
	//memcpy( rgraph, graph, sizeof(graph) );
	int parent[V];
	int u;
	while (bfs(x,y,rgraph,s,t,V,parent,V))
	{
		float flow = 999999;
		int v = t;
		while ( v != s)
		{
			u = parent[v];
			if (flow > rgraph[u][v])
			{
				flow = rgraph[u][v];			
			}
			v = parent[v];
		}
		int bottleneck = flow;

		v = t;
		while ( v != s)
		{
			u = parent[v];
			rgraph[v][u] += bottleneck;
			rgraph[u][v] -= bottleneck;
			v = parent[v];
		}
		total_flow += bottleneck;

	}
	
	memset(parent, 0 , sizeof(parent));
	int len = 6;
	bool * visited;
	visited = (bool*)malloc(sizeof(bool));
	for (j=0;j<V;j++){
		visited[j] = false;
	}

	int current;
	visited[s] = true;
	parent[s] = -1;
	node *queue;
	queue = (node*)malloc(sizeof(node));
	queue -> num = -1;
	queue -> next = NULL;

	enQueue(queue, s);
	while (!isEmpty (queue)){
		current= deQueue(queue);
		int i;
		for (i = 0; i < V; i++)
		{
			if ( !visited[i] && rgraph[current][i] > 0 )
			{
				enQueue(queue, i);
				parent[i] = current;
				visited[i] = true;
			}
		}

	}
	for (i = 0; i < x; i++) {
    free(rgraph[i]);
    }
    free(rgraph);
	return visited;

}
//
//int main() {
//
//int graph[6][6] = { 0,16,13,0,0,0,0,0,10,12,0,0,0,4,0,0,14,0,0,0,9,0,0,20,0,0,0,7,0,4,0,0,0,0,0,0};
//int s = 0;
//int t = 5;
//int V = 6;
//int x = 6;
//int y = 6;
//bool *result;
//
//result = mincut(x,y,graph,s,t,V);
//int i;
//for ( i = 0; i < 10; i++ ) {
//      printf( "*(result + %d) : %d\n", i, result[i]);
// }

//}




