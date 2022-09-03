class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                
        
        result = 0
        found_odd = False
        for key, value in d.items():
            if value % 2 == 0:
                result += value
            else:
                # 3, 5, 7과 같이 홀수개인 문자의 짝수만큼은 더해준다 (3이면 2, 5이면 4 ...)
                # 1개만 존재하는 문자는 다른 1개만 존재하는 문자들을 포함해서 
                # 총 1개만 존재해야되기 때문에 아래의 계산에서는 빼고
                # 반복문 밖에서 따로 계산한다
                result += value - 1
                found_odd = True
                
        if found_odd:
            # 1개만 존재하는 문자가 있으면 회문의 길이에 1을 더한다.
            # 1개만 존재하는 문자는 다른 1개만 존재하는 문자를 포함해서 총 1개만 존재해야되기 때문이다.
            result += 1
        
        return result
        
                
        
        
                
            