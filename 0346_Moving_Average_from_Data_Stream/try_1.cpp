class MovingAverage {
private:
    vector<int> data;
    int capacity;
    int length;
    int tail;
    double sum;
    
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        data = vector<int>(size);
        capacity = size;
        length = sum = 0;
        tail = -1;
    }
    
    bool append(int value){
        if (isFull()){
            tail = (tail+1) % capacity;
            sum -= data[tail];
            data[tail] = value;
            sum += data[tail];
        }
        else{
            tail = (tail+1) % capacity;
            data[tail] = value;
            sum += data[tail];
            length++;
        }
        
        return true;
    }
    
    bool isFull(){
        if (length == capacity){
            return true;
        }
        else{
            return false;
        }
    }
    
    double next(int val) {
        append(val);
        return sum / length;
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */