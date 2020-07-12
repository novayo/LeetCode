class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        Sieve of Eratosthenes : https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/sieve-of-eratosthenes-prime-adventure-part-4
        
        0~N 找質數的方法
        步驟：建表2~N，
        從2開始，把2平方與之後跟2的乘積，都標示為marked
        一直做下去，直到某數的平方大於N就可以停止
        在這之中unmarked的數就是prime
        '''
        
        if n < 2:
            return 0
        table = [1] * n # 把marked變成0, unmarked維持1，這樣找完之後，直接sum看個數即可
        table[0] = table[1] = 0 # 因為要配合答案，因此先把這兩個設成0
        
        for i in range(2, int(sqrt(n))+1): # 從2到開根號
            if table[i] == 1: 
                # 如果是質數
                # 讓 i*i~N的 i的倍數（也就是i*i  ;  i*i+i  ;  i*i+i+i ....）
                
                # 去等於對應個數的 0
                # 個數就是：(n個 - i*i個 - 1(剪掉N))
                # //i 代表有幾組（可以間隔幾個i）
                # 最後+1代表 有幾個數字
                
                # strikes[2*2:11:2]  = [0] * ((11-1-2*2)//2 + 1
                # strikes[4:11:2]    = [0] * 4
                # s[4], s[6], s[8], s10] = 0, 0, 0, 0
                table[i*i:n:i] = [0] * ((n-i*i-1)//i+1)
        return sum(table)
