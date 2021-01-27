class pair{
    Integer key;
    String value;
    
    public pair(int key, String value){
        this.key = key;
        this.value = value;
    }
}

class PrioityQueue{
    public List<pair> queue;
    
    public PrioityQueue(){
        this.queue = new ArrayList<pair>();
    }
    
    public void Push(String target){
        if (this.queue.size() == 0){
            this.queue.add(new pair(0, target));
        } else{
            int tmp = Contains(target);
            if (tmp > -1){
                this.queue.set(tmp, new pair(this.queue.get(tmp).key+1, target));
                Swap(tmp, this.queue.size()-1);
            } else{
                this.queue.add(new pair(0, target));
            }
            HeapifyAll(this.queue.size()-1);            
        }
    }
    
    public String Pop(){
        String ret = this.queue.get(0).value;
        Swap(0, this.queue.size()-1);
        this.queue.remove(this.queue.size()-1);
        HeapifyAll(this.queue.size()-1);
        return ret;
    }
    
    private void Heapify(int index){
        int largest = index;
        int left = 2*index;
        int right = 2*index+1;
        
        if (left < this.queue.size()){
            if (this.queue.get(largest).key < this.queue.get(left).key){
                largest = left;
                
                //lower alphabetical order comes first.
            } else if (this.queue.get(largest).key == this.queue.get(left).key){
                if (this.queue.get(largest).value.compareTo(this.queue.get(left).value) > 0){
                    largest = left;
                }
            }
        }
        
        if (right < this.queue.size()){
            if (this.queue.get(largest).key < this.queue.get(right).key){
                largest = right;
            } else if (this.queue.get(largest).key == this.queue.get(right).key){
                if (this.queue.get(largest).value.compareTo(this.queue.get(right).value) > 0){
                    largest = right;
                }
            }
        }
        
        if (largest != index){
            Swap(largest, index);
            Heapify(largest);
        }
    }
    
    private void HeapifyAll(int index){
        for (int i=index/2; i>=0; i--){
            Heapify(i);
        }
    }
    
    private void Swap(int index1, int index2){
        pair tmp = this.queue.get(index1);
        this.queue.set(index1, this.queue.get(index2));
        this.queue.set(index2, tmp);
    }
    
    
    private int Contains(String target){
        for (int i=0; i<this.queue.size(); i++){
            if (this.queue.get(i).value.equals(target)){
                return i;
            }
        }
        return -1;
    }
}


class Solution {
    
    
    public List<String> topKFrequent(String[] words, int k) {
        PrioityQueue queue = new PrioityQueue();
        
        for (String tmp : words){
            queue.Push(tmp);
        }
        
        List<String> ans = new ArrayList<String>();
        while (k-- > 0){
            ans.add(queue.Pop());
        }
        
        return ans;
    }
    
    
}
