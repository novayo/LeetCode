/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* ans = NULL;
    struct ListNode* temp = NULL;
    struct ListNode* p = NULL;
    int carry = 0;
    
    while(l1 != NULL && l2 != NULL){
        temp = (struct ListNode*)malloc(sizeof(struct ListNode));
        temp->next = NULL;
        temp->val = l1->val + l2->val + carry;
        carry = temp->val / 10;
        temp->val -= carry * 10;
        
        if (ans == NULL) {
            ans = temp;
        } else {
            p = ans;
            while(p->next != NULL){
                p = p->next;
            }
            p->next = temp;
        }
        
        l1 = l1->next;
        l2 = l2->next;
    }
    
    if (l1 == NULL && l2 != NULL){ // l2 is not empty
        p = ans;
        while(p->next != NULL){
            p = p->next;
        }
        while(l2 != NULL){
            p->next = l2;
            p = p->next;
            p->val = l2->val + carry;
            carry = p->val / 10;
            p->val -= carry * 10;
            l2 = l2->next;
        }
    } else if (l1 != NULL && l2 == NULL){ // l1 is not empty
        p = ans;
        while(p->next != NULL){
            p = p->next;
        }
        while(l1 != NULL){
            p->next = l1;
            p = p->next;
            p->val = l1->val + carry;
            carry = p->val / 10;
            p->val -= carry * 10;
            l1 = l1->next;
        }
    } 
    if (carry != 0){
        p = ans;
        while(p->next != NULL){
            p = p->next;
        }
        temp = (struct ListNode*)malloc(sizeof(struct ListNode));
        temp->next = NULL;
        temp->val = carry;
        p->next = temp;
    }
    
    return ans;
}


