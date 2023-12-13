class Node {
    val: number;
    next: Node | null;

    constructor(val: number = -1, next: Node | null = null) {
        this.val = val;
        this.next = next;
    }
}

class MyLinkedList {
    head: Node;

    constructor() {
        this.head = new Node();
    }

    printNode(): void {
        let ptr: Node | null = this.head;
        while (ptr) {
            console.log(ptr.val, "->");
            ptr = ptr.next;
        }
        console.log();
    }

    // O(n)
    get(index: number): number {
        let ptr: Node | null = this.head;
        for (let i = 0; i < index + 1; i++) {
            if (!ptr) {
                break;
            }
            ptr = ptr.next;
        }

        if (!ptr) {
            return -1;
        }
        return ptr.val;
    }

    // O(1)
    addAtHead(val: number): void {
        const tmp: Node | null = this.head.next;
        this.head.next = new Node(val, tmp);
    }

    // O(n)
    addAtTail(val: number): void {
        let ptr: Node | null = this.head;
        while (ptr && ptr.next) {
            ptr = ptr.next;
        }

        if (ptr) {
            ptr.next = new Node(val);
        }
    }

    // O(n)
    addAtIndex(index: number, val: number): void {
        let ptr: Node | null = this.head;
        for (let i = 0; i < index; i++) {
            if (!ptr) {
                break;
            }
            ptr = ptr.next;
        }

        if (!ptr) {
            return;
        }

        const tmp: Node | null = ptr.next;
        ptr.next = new Node(val, tmp);
    }

    // O(n)
    deleteAtIndex(index: number): void {
        let ptr: Node | null = this.head;
        for (let i = 0; i < index; i++) {
            if (!ptr) {
                break;
            }
            ptr = ptr.next;
        }

        if (ptr && ptr.next) {
            ptr.next = ptr.next.next;
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
