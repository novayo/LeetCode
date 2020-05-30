class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_table = collections.defaultdict(set)
        ans = 0
        
        for email in emails:
            local_name, domain_name = email.split("@")
            filtered_local_name = ""
            for n in local_name:
                if n == "+":
                    break
                elif n != ".":
                    filtered_local_name += n
            
            if filtered_local_name not in hash_table[domain_name]:
                hash_table[domain_name].add(filtered_local_name)
                ans += 1
        
        return ans
