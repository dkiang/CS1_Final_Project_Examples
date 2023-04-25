#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

#define SIZE 10
#define RED "\x1B[31m"
#define GREEN "\x1B[32m"
#define YELLOW "\x1B[33m"
#define BLUE "\x1B[34m"
#define RESET "\x1B[0m"

// Structure to represent a node (space) in the grid
typedef struct {
    int x, y, dist;
} Node;

typedef struct {
    int x, y, g, h, f;
} AStarNode;

int a_star(int grid[SIZE][SIZE], int path[SIZE][SIZE]); // A* search algorithm for finding the optimal path
int compareAStarNodes(const void *a, const void *b);
int compareNodes(const void *a, const void *b); // Compare function for qsort to sort nodes based on their distances
int dijkstra(int grid[SIZE][SIZE], int path[SIZE][SIZE]); // Dijkstra's algorithm for finding the optimal path
int dynamicProgramming(int grid[SIZE][SIZE], int path[SIZE][SIZE]); // Dynamic Programming algorithm for finding the optimal path
int findOptimalPath(int grid[SIZE][SIZE], int mode); // Find the optimal path using the selected algorithm (mode) and return the total fuel cost
void generateRandomGrid(int grid[SIZE][SIZE]); // Generate a 10x10 grid filled with random single-digit numbers
int heuristic(int x, int y);
void printGrid(int grid[SIZE][SIZE]); // Print the grid with fuel costs
void printPath(int path[SIZE][SIZE], int fuelCost);
int validMove(int x, int y); // Check if a move to (x, y) is valid

int main() {
    srand(time(NULL));
    int grid[SIZE][SIZE];
    int mode;
    int keepGrid = 1;
    generateRandomGrid(grid);
    while (1) {
        if (!keepGrid) {
            generateRandomGrid(grid);
        }
        printGrid(grid);

        printf("Enter mode (1 - Dynamic Programming, 2 - Dijkstra's, 3 - A*): ");
        scanf("%d", &mode);

        int fuelCost = findOptimalPath(grid, (mode-1));
        printf("Optimal path fuel cost: %d\n", fuelCost);

        printf("Do you want to keep the current grid? (1 - Yes, 0 - No): ");
        scanf("%d", &keepGrid);

        if (!keepGrid) {
            printf("Do you want to exit? (1 - Yes, 0 - No): ");
            int exit;
            scanf("%d", &exit);
            if (exit) {
                break;
            }
        }
    }

    return 0;
}


void generateRandomGrid(int grid[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            grid[i][j] = rand() % 10;
        }
    }
}

void printGrid(int grid[SIZE][SIZE]) {
    printf("Grid:\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (grid[i][j] < 3) {
                printf(GREEN "%d " RESET, grid[i][j]);
            }
            else if (grid[i][j] < 6) {
                printf(YELLOW "%d " RESET, grid[i][j]);
            }
            else {
                printf(RED "%d " RESET, grid[i][j]);
            }
        }
        printf("\n");
    }
}

// Find the optimal path using the selected algorithm (mode) and return the total fuel cost
int findOptimalPath(int grid[SIZE][SIZE], int mode) {
    int path[SIZE][SIZE] = {0};

    int fuelCost;
    switch (mode) {
        case 0:
            fuelCost = dynamicProgramming(grid, path);
            break;
        case 1:
            fuelCost = dijkstra(grid, path);
            break;
        case 2:
            fuelCost = a_star(grid, path);
            break;
        default:
            printf("Invalid mode\n");
            return -1;
    }

    printPath(path, fuelCost);
    return fuelCost;
}

int dynamicProgramming(int grid[SIZE][SIZE], int path[SIZE][SIZE]) {
    int dp[SIZE][SIZE];

    dp[0][0] = grid[0][0];
    for (int i = 1; i < SIZE; i++) {
        dp[i][0] = dp[i - 1][0] + grid[i][0];
        dp[0][i] = dp[0][i - 1] + grid[0][i];
    }

    for (int i = 1; i < SIZE; i++) {
        for (int j = 1; j < SIZE; j++) {
            dp[i][j] = grid[i][j] + (dp[i - 1][j] < dp[i][j - 1] ? dp[i - 1][j] : dp[i][j - 1]);
        }
    }

    int i = SIZE - 1, j = SIZE - 1;
    while (i > 0 || j > 0) {
        path[i][j] = 1;

        if (i == 0) {
            j--;
        } else if (j == 0) {
            i--;
        } else {
            if (dp[i - 1][j] < dp[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }
    }
    path[0][0] = 1;

    return dp[SIZE - 1][SIZE - 1];
}


int dijkstra(int grid[SIZE][SIZE], int path[SIZE][SIZE]) {
    int dist[SIZE][SIZE];
    int visited[SIZE][SIZE] = {0};
    int prev[SIZE][SIZE][2];

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            dist[i][j] = INT_MAX;
        }
    }

    int dx[] = {1, 0, -1, 0};
    int dy[] = {0, 1, 0, -1};

    dist[0][0] = grid[0][0];
    Node nodes[SIZE * SIZE];
    int nodeCount = 0;

    nodes[nodeCount++] = (Node) {0, 0, dist[0][0]};

    while (nodeCount > 0) {
        qsort(nodes, nodeCount, sizeof(Node), compareNodes);
        Node curr = nodes[--nodeCount];

        if (visited[curr.x][curr.y]) {
            continue;
        }

        visited[curr.x][curr.y] = 1;

        if (curr.x == SIZE - 1 && curr.y == SIZE - 1) {
            break;
        }

        for (int k = 0; k < 4; k++) {
            int x = curr.x + dx[k];
            int y = curr.y + dy[k];

            if (validMove(x, y) && !visited[x][y]) {
                int newDist = dist[curr.x][curr.y] + grid[x][y];

                if (newDist < dist[x][y]) {
                    dist[x][y] = newDist;
                    prev[x][y][0] = curr.x;
                    prev[x][y][1] = curr.y;
                    nodes[nodeCount++] = (Node) {x, y, newDist};
                }
            }
        }
    }

    int x = SIZE - 1, y = SIZE - 1;
    while (x != 0 || y != 0) {
        path[x][y] = 1;
        int prevX = prev[x][y][0];
        int prevY = prev[x][y][1];
        x = prevX;
        y = prevY;
    }
    path[0][0] = 1;

    return dist[SIZE - 1][SIZE - 1];
}


int a_star(int grid[SIZE][SIZE], int path[SIZE][SIZE]) {
    int visited[SIZE][SIZE] = {0};
    int g[SIZE][SIZE];
    int prev[SIZE][SIZE][2];

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            g[i][j] = INT_MAX;
        }
    }

    int dx[] = {1, 0, -1, 0};
    int dy[] = {0, 1, 0, -1};

    g[0][0] = grid[0][0];
    AStarNode nodes[SIZE * SIZE];
    int nodeCount = 0;

    nodes[nodeCount++] = (AStarNode) {0, 0, g[0][0], heuristic(0, 0), g[0][0] + heuristic(0, 0)};

    while (nodeCount > 0) {
        qsort(nodes, nodeCount, sizeof(AStarNode), compareAStarNodes);
        AStarNode curr = nodes[--nodeCount];

        if (visited[curr.x][curr.y]) {
            continue;
        }

        visited[curr.x][curr.y] = 1;

        if (curr.x == SIZE - 1 && curr.y == SIZE - 1) {
            break;
        }

        for (int k = 0; k < 4; k++) {
            int x = curr.x + dx[k];
            int y = curr.y + dy[k];

            if (validMove(x, y) && !visited[x][y]) {
                int newG = g[curr.x][curr.y] + grid[x][y];

                if (newG < g[x][y]) {
                    g[x][y] = newG;
                    prev[x][y][0] = curr.x;
                    prev[x][y][1] = curr.y;
                    int newH = heuristic(x, y);
                    nodes[nodeCount++] = (AStarNode) {x, y, newG, newH, newG + newH};
                }
            }
        }
    }

    int x = SIZE - 1, y = SIZE - 1;
    while (x != 0 || y != 0) {
        path[x][y] = 1;
        int prevX = prev[x][y][0];
        int prevY = prev[x][y][1];
        x = prevX;
        y = prevY;
    }
    path[0][0] = 1;

    return g[SIZE - 1][SIZE - 1];
}


void printPath(int path[SIZE][SIZE], int fuelCost) {
    printf("Optimal path:\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (path[i][j]) {
                printf(RED "x " RESET);
            } else {
                printf(BLUE ". " RESET);
            }
        }
        printf("\n");
    }
}



int compareNodes(const void *a, const void *b) {
    const Node *nodeA = a;
    const Node *nodeB = b;

    return nodeA->dist - nodeB->dist;
}

int validMove(int x, int y) {
    return x >= 0 && x < SIZE && y >= 0 && y < SIZE;
}


int compareAStarNodes(const void *a, const void *b) {
    const AStarNode *nodeA = a;
    const AStarNode *nodeB = b;

    return nodeA->f - nodeB->f;
}

int heuristic(int x, int y) {
    return abs(x - (SIZE - 1)) + abs(y - (SIZE - 1));
}

