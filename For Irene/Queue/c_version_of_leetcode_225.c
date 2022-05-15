
typedef struct {
    int *data;
    int front;
    int rear;
    int size;
} MyStack;


MyStack* myStackCreate() {
    MyStack *stack = malloc(sizeof(MyStack)) ;
    stack->front = 0;
    stack->rear = 0;
    stack->data = malloc(100*sizeof(int));
    stack->size = 100;
    memset(stack->data, 0, 100*sizeof(int));
    return stack;
}

void myStackPush(MyStack* obj, int x) {
    obj->data[obj->rear] = x;
    obj->rear = obj->rear+1;
}

int myStackPop(MyStack* obj) {
    int pop = 0;
    pop = obj->data[obj->rear-1];
    obj->rear = obj->rear-1;
    return pop;
}

int myStackTop(MyStack* obj) {
    return obj->data[obj->rear-1]; 
}
